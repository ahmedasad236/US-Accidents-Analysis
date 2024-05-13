from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
import pandas as pd
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    # Renaming the columns to match BigQuery restrictions
    df.rename(columns={
        'Distance(mi)' : 'Distance',
        'Precipitation(in)' : 'Precipitation',
        'Wind_Speed(mph)' : 'Wind_Speed',
        'Visibility(mi)' : 'Visibility',
        'Pressure(in)' : 'Pressure',
        'Humidity(%)' : 'Humidity',
        'Wind_Chill(F)' : 'Wind_Chill',
        'Temperature(F)' : 'Temperature'
    }, inplace=True)

    # Convert 'Time' column to datetime
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])

    # Create new columns for day and month
    df['Day_Of_Acc'] = df['Start_Time'].dt.day.astype(str)
    df['Month_Of_Acc'] = df['Start_Time'].dt.month.astype(str)

    # Convert 'Severity' column to numbers
    df['Severity'] = df['Severity'].astype(int)

    # drop null values
    df.dropna()
    
    table_id = 'us-accidents-421114.us_accidents_analytics.accidents'
    
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    
    config_profile = 'default'

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )
