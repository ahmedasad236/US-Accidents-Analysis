from pyspark.ml.feature import VectorAssembler, OneHotEncoder
from pyspark.sql import DataFrame
from pyspark.sql.functions import when , col

def convert_string_data(df: DataFrame, column_name: str) -> DataFrame:
    
    # Count the occurrences of each unique value
    value_counts = df.groupBy(column_name).count()

    # Sort by count in descending order and take the top 20
    top_20_values = value_counts.orderBy(col('count').desc()).limit(20)

    # Collect the top 20 values
    top_20_values_list = top_20_values.select(column_name).rdd.flatMap(lambda x: x).collect()

    # Create a new DataFrame to accumulate transformations
    new_df = df

    # Loop through each unique value and create a new column for each
    for source in top_20_values_list:
        new_column_name = source.replace(" ", "_").lower() + "_" + column_name
        # Accumulate transformations by using the new DataFrame
        new_df = new_df.withColumn(new_column_name, when(col(column_name) == source, 1).otherwise(0))

    # Drop the original column
    new_df = new_df.drop(column_name)

    return new_df


def convert_boolean_data(df: DataFrame, column_name: str) -> DataFrame:
    new_df = df
    new_df = new_df.withColumn(column_name, when(col(column_name), 1).otherwise(0))
    return new_df