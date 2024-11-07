# from pyspark.sql import SparkSession
# from pyspark.sql.functions import *

# Initialize Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Sample data
data = [("a", "aa", 1), ("a", "aa", 2), ("b", "bb", 5), ("b", "bb", 3), ("b", "bb", 4)]

# Define schema
schema = ["col1", "col2", "col3"]

# Create DataFrame
df = spark.createDataFrame(data, schema=schema)

# Show result
df_grouped.show()

# Stop the Spark session
spark.stop()
