"""
This module is for tracking trending tags over time.
"""
import pandas as pd
import numpy as np

df = pd.read_csv("./data/US_youtube_trending_data.csv")


def time_fmt(tdf):
    """
    Note
    -------
    This function is to format date time coloumn to datetime64

    Parameters:
    -------
    df: a dataframe form

    Returns
    -------
    Return a dataframe after formating time 
    """

    tdf["trending_date"] = pd.to_datetime(tdf.trending_date)
    tdf["publishedAt"] = pd.to_datetime(tdf.publishedAt)
    return tdf


def split_tags():
    """
    Note
    -------
    This function is to split column["tags"]

    Parameters:
    -------
    None

    Returns
    -------
    Return a dataframe after spliting every tags
    """

    time_fmt_df = time_fmt(df)
    tag_slt_df = pd.concat([time_fmt_df["trending_date"], time_fmt_df["tags"]
                           .str.split(pat='|', expand=False)], axis=1)
    tag_df = pd.DataFrame([[x] + [z] for x, y in zip(tag_slt_df.index, tag_slt_df.tags) for z in y])
    tag_df = tag_df.merge(tag_slt_df, left_on=0, right_index=True)
    tag_df.rename(columns={1: "tag_name", 0: "frequency"}, inplace=True)
    return tag_df


def select_year_and_month(tag_df, y_1, y_2, m_1, m_2):
    """
    Note
    -------
    This function is to filter data over time.
    Selecting data from y1.m1 to y2.m2.
    If you want to select just one month, input same number of year and month.
    e.g.    y1=2021, y2=2021, m1=10, m2=10 stands for selecting data in Oct 2021
            y1=2020, y2=2021, m1=10, m2=10 stands for selecting data from Oct 2020 to Oct 2021

    Parameters:
    -------
    tag_df: a dataframe with index of indivisual tags
    y1: starts of year
    y2: ends of year
    m1: start of month
    m2: ends of month

    Returns
    -------
    Return a dataframe with top 20 tags in period of time
    """

    tag_y_df = tag_df[tag_df["trending_date"].dt.year.isin(np.arange(y_1, y_2+1))]
    tag_ym_df = tag_y_df[tag_y_df["trending_date"].dt.month.isin(np.arange(m_1, m_2+1))]
    tag_ym_df = tag_ym_df[["tag_name", "frequency"]].groupby(["tag_name"]).count()\
        .sort_values(["frequency"], ascending=False).drop(index="[None]")
    
    return tag_ym_df.head(20)


# tag_df = split_tags()
# print(select_year_and_month(tag_df,2021,2021,10,10))

