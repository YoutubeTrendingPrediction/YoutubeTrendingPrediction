"""
This module is used to analysis the trending categoriy along with 
the time variation. The time steps can be daily and monthly.
"""

import pandas as pd

df_category=pd.read_csv('../data/US_category_id.csv')
df=pd.read_csv('../data/US_youtube_trending_data.csv')

def timesplit(data):
    """
    This function is used to extract detailed time information, such
    as hour, year, month and so on, from the original time column.
    Input: The original dataFrame.
    Output: The new dataFrame with added columns in various time steps.
    """
    data['date']=pd.to_datetime(data['trending_date']).dt.date
    data['month']=pd.to_datetime(data['trending_date']).dt.month
    data['year']=pd.to_datetime(data['trending_date']).dt.year
    return data


def dataframecombine(dataframea,dataframeb):
    """
    This function is used to combine two different dataframe based on same 
    column valu额。
    Input: Two dataframe needed to be combined.
    Output: A new combined dataframe
    """
    dataframea1=dataframea.rename({'Id':'categoryId'},axis=1)
    df1=dataframeb.merge(dataframea1,left_on='categoryId',right_on='Id')
    return df1


def splitcategory(df1):
    """
    This function is used to sort the dataframe in terms of various data and
    title, suming up the result.
    Input:The previous conbined dataframe
    Output:A dataframe showing various title corresponding to their total
    aomount in chronological order.
    """
    df2=df1.groupby(['date','Title','month','year']).size()
    df3=df2.reset_index(name='Amount')
    df4=df3.sort_values(by=['date','Amount'])
    df5=df4.reset_index()
    df6=df5.drop(['index'],axis=1)
    return df6




