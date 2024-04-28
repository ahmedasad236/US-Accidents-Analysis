from mage_ai.io.file import FileIO
import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Template for loading data from filesystem.
    Load data from 1 file or multiple file directories.

    For multiple directories, use the following:
        FileIO().load(file_directories=['dir_1', 'dir_2'])

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    filepath = '/home/src/US_Accidents_March23.csv'
    us_acc_dt = {
        'ID': str,
        'Source':str,
        'Severity':str,
        'Start_Lat': float,
        'Start_Lng': float,
        'Start_Time':str,
        'End_Time': str,
        'Weather_Timestamp': str,
        'Distance(mi)': float,
        'Description': str,
        'Street': str,
        'City': str,
        'County': str,
        'State': str,
        'Zipcode': str,
        'Country': str,
        'Airport_Code': str,
        'Temperature(F)': float,
        'Wind_Chill(F)': float,
        'Humidity(%)': float,
        'Pressure(in)': float,
        'Visibility(mi)': float,
        'Wind_Direction': str,
        'Wind_Speed(mph)': float,
        'Precipitation(in)': float,
        'Weather_Condition': str,
        'Amenity': bool,
        'Bump': bool,
        'Crossing': bool,
        'Give_Way': bool,
        'Junction': bool,
        'No_Exit': bool,
        'Railway': bool,
        'Roundabout': bool,
        'Station': bool,
        'Stop': bool,
        'Traffic_Calming': bool,
        'Traffic_Signal': bool,
        'Turning_Loop': bool,
        'Sunrise_Sunset': str, 
        'Civil_Twilight': str,
        'Nautical_Twilight': str,
        'Astronomical_Twilight': str
    }



    df = pd.read_csv(filepath, sep=",", dtype=us_acc_dt)
    print(df.head(1))
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
