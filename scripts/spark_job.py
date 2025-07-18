# This script reads a CSV using PySpark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
df = spark.read.csv("data/sample.csv", header=True, inferSchema=True)
df.show()
spark.stop()