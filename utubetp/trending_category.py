"""
This module is used to analysis the trending category along with
the time variation. The time steps can be days and months.
"""

import pandas as pd

df_category=pd.read_csv('./data/US_category_id.csv')
df=pd.read_csv('./data/US_youtube_trending_data.csv')

def timesplit(data):
    """
    This function is used to extract detailed time information, such
    as hours, years, and months from time volumn.
    Input: A DataFrame
    Output: The new dataFrame with added columns in various time steps.
    """
    data=df
    data['date']=pd.to_datetime(data['trending_date']).dt.date
    data['month']=pd.to_datetime(data['trending_date']).dt.month
    data['year']=pd.to_datetime(data['trending_date']).dt.year
    return data

def dataframecombine(dataframea,dataframeb):
    """
    This function is used to combine two different dataframe based on 
    same column value
    Input: Two dataframes that can be combined
    Output: A new combined dataframe
    """
    dataframea=df_category
    dataframeb=timesplit(df)
    dataframea1=dataframea.rename({'Id':'categoryId'},axis=1)
    outcomedata=dataframeb.merge(dataframea1,left_on='categoryId',right_on='Id')
    return outcomedata


def splitcategory(df1):
    """
    This function is used to sort the dataframe in terms of various data and
    title, suming up the result.
    Input:A dataframe
    Output:A dataframe showing various title corresponding to their total
    aomount in chronological order.
    """
    dft= timesplit(df)
    df1=dataframecombine(df_category,dft)
    df2=df1.groupby(['date','Title','month','year']).size()
    df3=df2.reset_index(name='Amount')
    df4=df3.sort_values(by=['date','Amount'])
    df5=df4.reset_index()
    df6=df5.drop(['index'],axis=1)
    return df6


def detailtimesplit(df6):
    """
    This function is used to split the aforementioned dataframe into monthly data
    Input: The previous groupbyed dataframe
    Ouput: Seperated monthly data in a list
    """
    dft=timesplit(df)
    df1=dataframecombine(df_category,dft)
    df6=splitcategory(df1)
    yearnumber=df6.year.unique()
    monthnumber=df6.month.unique()
    set=[]
    for i in yearnumber:
         for j in range(1,13):
             if i==yearnumber[0] and j>=1 and j<monthnumber[0]:
                continue
             elif i==yearnumber[1] and j==12:
                continue
             else:
                data=df6[(df6.year==i)&(df6.month==j)]
                set.append(data)
    return set
