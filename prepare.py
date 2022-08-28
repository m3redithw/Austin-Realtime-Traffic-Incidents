import pandas as pd
import numpy as np

def prep_data(df):
    '''
    This function takes in a dataframe and returns the cleaned dataframe
    '''
    # Drop unsueful column
    df.drop(columns = 'Traffic Report ID', inplace = True)

    # Change data to datetime object
    df['Published Date'] = pd.to_datetime(df['Published Date'], infer_datetime_format=True)

    # Set date to index of DataFrame
    df = df.set_index(df['Published Date'])

    # Replace nulls with latitude and longitude
    df.Location.fillna("("+str(df.Latitude)+","+str(df.Longitude)+")", inplace = True)

    # Drop the null values in latitude and longitude
    df = df.dropna(subset = ['Latitude', 'Longitude'])

    return df