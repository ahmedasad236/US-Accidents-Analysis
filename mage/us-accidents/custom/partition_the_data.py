import pandas as pd
if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@custom
def transform_custom(*args, **kwargs):
    
    transformed_df = args[0]  # Access the transformed DataFrame

    # Convert the "Start_Time" and "End_Time" columns to datetime
    transformed_df['Start_Time'] = pd.to_datetime(transformed_df['Start_Time'])
    transformed_df['End_Time'] = pd.to_datetime(transformed_df['End_Time'])

    # Group the DataFrame by year based on the "Start_Time" column
    grouped_by_year = transformed_df.groupby(transformed_df['Start_Time'].dt.year)
    
    # Initialize list to store DataFrame partitions
    partitions = []
    
    # Loop through each year group and save it as a Parquet file
    for year, group_df in grouped_by_year:
        group_df.to_parquet(f'partition_{year}.parquet', index=False)
        partitions.append(group_df)

    return partitions



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert len(output) == 8, 'The number of partitioned files is not correct'
