"""
This module is for predicting the future view counts
and trending tendency of the current trending videos.
"""

import pandas as pd
from scipy import interpolate

df = pd.read_csv('./data/US_youtube_trending_data.csv')


def df_cleaning(df_raw):
    """
    Note
    -------
    This function removes the unnecessary columns in the dataframe, formats the date time column,
    clears bad data, and filters out the suitable data for training the prediction model.

    Parameters:
    -------
    df: a pandas DataFrame

    Returns
    -------
    Return a pandas DataFrame after data cleaning.
    """

    if isinstance(df_raw, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')

    df_cleaned = df_raw.drop(columns=['channelId', 'channelTitle', 'tags', 'thumbnail_link',
                            'comments_disabled', 'ratings_disabled', 'description',
                            'publishedAt', 'likes', 'dislikes', 'comment_count'], axis=1)
    df_cleaned = df_cleaned[df_cleaned['view_count'] > 0]
    df_cleaned['trending_date'] = pd.to_datetime(df_cleaned.trending_date)
    df_cleaned = df_cleaned.groupby(['video_id']).filter(lambda x: len(x) > 4)
    return df_cleaned


def get_video_ids(df_cleaned):
    """
    Note
    -------
    This function gets the unique video IDs in the cleaned DataFrame, and store them into
    a numpy array.

    Parameters:
    -------
    df_cleaned: a pandas DataFrame, after cleaning

    Returns
    -------
    Return a numpy array of the unique video IDs.
    """

    if isinstance(df_cleaned, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')
    if df_cleaned.equals(df):
        raise ValueError('DataFrame not cleaned!')

    video_ids = df_cleaned.video_id.unique()
    return video_ids


def output_video_dict(df_cleaned):
    """
    Note
    -------
    This function output a dictionary that is ready for training a large prediction model,
    the dictionary contains all the data of the cleaned DataFrame grouped by the video IDs.

    Parameters:
    -------
    df_cleaned: a pandas DataFrame, after cleaning

    Returns
    -------
    Return a dictionary containing all the data for training and using a prediction model.
    """

    if isinstance(df_cleaned, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')
    if df_cleaned.equals(df):
        raise ValueError('DataFrame not cleaned!')

    video_ids = get_video_ids(df_cleaned)
    df_grouped = df_cleaned.groupby(['video_id'])
    video_dict = {}
    for i in video_ids:
        video_dict[i] = df_grouped.get_group(i)
    return video_dict


def get_current_trending(df_cleaned):
    """
    Note
    -------
    This function gets a DataFrame containing information of the current trending videos, including
    the ones on trends within the past five days.
    This function also removes the videos having only 3 days on trends or less, in order to
    implement the spline curve interpolation and fit.

    Parameters:
    -------
    df_cleaned: a pandas DataFrame, after cleaning

    Returns
    -------
    Return a pandas DataFrame of information from videos on trends within the last five days.
    """

    if isinstance(df_cleaned, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')
    if df_cleaned.equals(df):
        raise ValueError('DataFrame not cleaned!')

    start_date = df_cleaned['trending_date'].max() + pd.DateOffset(-4)
    end_date = df_cleaned['trending_date'].max()
    current_trending = df_cleaned[df_cleaned['trending_date'].between(start_date, end_date)]
    current_trending = current_trending.groupby(['video_id']).filter(lambda x: len(x) > 3)
    return current_trending


def get_current_ids(df_cleaned):
    """
    Note
    -------
    This function gets the unique video IDs in the videos of the current trending DataFrame,
    and store them into a numpy array.

    Parameters:
    -------
    df_cleaned: a pandas DataFrame, after cleaning

    Returns
    -------
    Return a numpy array of the unique video IDs which are currently on trends.
    """

    if isinstance(df_cleaned, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')
    if df_cleaned.equals(df):
        raise ValueError('DataFrame not cleaned!')

    current_trending = get_current_trending(df_cleaned)
    current_ids = current_trending.video_id.unique()
    return current_ids


def output_current_dict(df_cleaned):
    """
    Note
    -------
    This function output a dictionary that is ready for training a small prediction model, or to
    simply interpolate and fit the relationship between date and view count, or to just showcase.
    The dictionary contains data of the current trending videos DataFrame grouped by the video IDs.

    Parameters:
    -------
    df_cleaned: a pandas DataFrame, after cleaning

    Returns
    -------
    Return a dictionary containing videos' data that currently trending for
    a small prediction model, or to just showcase.
    """

    if isinstance(df_cleaned, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')
    if df_cleaned.equals(df):
        raise ValueError('DataFrame not cleaned!')

    current_trending = get_current_trending(df_cleaned)
    current_ids = current_trending.video_id.unique()
    current_trending_group = current_trending.groupby(['video_id'])
    current_dict = {}
    for i in current_ids:
        current_dict[i] = current_trending_group.get_group(i).reset_index(drop=True)
    return current_dict


def pred_current_dict(df_cleaned):
    """
    Note
    -------
    This function predict the future view counts and trending tendency for one day in advance,
    and updated the current_dict with the predicted values.

    Parameters:
    -------
    df_cleaned: a pandas DataFrame, after cleaning

    Returns
    -------
    Return a dictionary with predicted values updated.
    """

    if isinstance(df_cleaned, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')
    if df_cleaned.equals(df):
        raise ValueError('DataFrame not cleaned!')

    current_dict = output_current_dict(df_cleaned)
    current_ids = get_current_ids(df_cleaned)
    for i in current_ids:
        category = int(current_dict[i].categoryId.unique())
        title = str(current_dict[i].title.unique()[0])
        trending_date = current_dict[i].trending_date.max() + pd.DateOffset(1)
        last_view_count = current_dict[i].view_count.max()
        x_points = list(current_dict[i].index)
        y_points = list(current_dict[i].view_count)
        tck = interpolate.splrep(x_points, y_points)
        view_count_pred = int(interpolate.splev(max(x_points) + 1, tck))
        if view_count_pred < last_view_count:
            view_count_pred = last_view_count + last_view_count - view_count_pred
        current_dict[i].loc[len(current_dict[i].index)] = [i, title, category,
                                                           trending_date, view_count_pred]
    return current_dict


def output_prediction(df_cleaned):
    """
    Note
    -------
    This function transfer the dictionary with prediction values to a DataFrame,
    and output that DataFrame into a csv file.

    Parameters:
    -------
    df_cleaned: a pandas DataFrame, after cleaning
    """

    if isinstance(df_cleaned, pd.core.frame.DataFrame) is False:
        raise TypeError('Input is not a DataFrame!')
    if df_cleaned.equals(df):
        raise ValueError('DataFrame not cleaned!')

    prediction_dict = pred_current_dict(df_cleaned)
    current_ids = get_current_ids(df_cleaned)
    df_output = pd.DataFrame(columns=['video_id', 'title', 'categoryId',
                            'trending_date', 'view_count'])
    for i in current_ids:
        df_output = df_output.append(prediction_dict[i], ignore_index=True)
    return df_output
