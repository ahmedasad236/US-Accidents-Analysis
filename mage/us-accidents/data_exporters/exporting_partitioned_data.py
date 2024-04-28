import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/gcp_credentials.json'
bucket_name = 'us-accidents-bucket'
project_id = 'us-accidents-421114'
table_name = 'us_accidents_data'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    
    transformed_df = data  

    # Create a new column "Start_Year" containing the year extracted from "Start_Time"
    transformed_df['Start_Year'] = transformed_df['Start_Time'].str[:4]

    table = pa.Table.from_pandas(transformed_df)

    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['Start_Year'],
        filesystem=gcs
    )


