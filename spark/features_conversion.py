from pyspark.ml.feature import VectorAssembler, OneHotEncoder

#source count for all values in the column
new_df.groupBy('Source').count().orderBy('count', ascending=False).show()

# Encode property_type
from pyspark.sql.functions import when , col

# List of distinct property types
source_values = ['House', 'Apartment', 'Townhouse', 'Condominium', 'Bed & Breakfast',
                  'Loft', 'Cabin', 'Other', 'Camper/RV', 'Boat', 'Tent', 'Bungalow',
                  'Treehouse', 'Dorm', 'Chalet']

# Loop through each property type and create a new column for each
for source in source_values:
    new_df = new_df.withColumn(source.replace(" ", "_").lower(), when(col("Source") == source, 1).otherwise(0))

# Drop the original 'Source' column
new_df = new_df.drop("Source")



# Define the columns to be included in the feature vector
input_columns = ['Source', 'Start_Time', 'End_Time', 'Street', 'City', 'County', 'State', 'Wind_Direction', 'Weather_Condition', 'Sunrise_Sunset']

# Apply one-hot encoding to string index columns
encoders = [OneHotEncoder(inputCol=column+"_index", outputCol=column+"_encoded") for column in input_columns if classification_df.schema[column].dataType == "string"]

# Assemble the remaining columns (numeric columns) into a vector
numeric_columns = [column for column in classification_df.columns if column not in input_columns]
assembler = VectorAssembler(inputCols=numeric_columns, outputCol="numeric_features")

# Combine all features into a single vector
final_assembler = VectorAssembler(inputCols=[column+"_encoded" for column in input_columns if classification_df.schema[column].dataType == "string"] + ["numeric_features"], outputCol="features")

# Pipeline stages
stages =  encoders + [assembler, final_assembler]

# Create a pipeline
from pyspark.ml import Pipeline
pipeline = Pipeline(stages=stages)

# Fit the pipeline to the data
pipeline_model = pipeline.fit(classification_df)

# Transform the data
output = pipeline_model.transform(classification_df)
