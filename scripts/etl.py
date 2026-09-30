import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from pyspark.sql import SparkSession
from scripts.validate import validate_data
from scripts.transform import transform_data
from scripts.load import laod_data

spark = SparkSession.builder.appName("ETL data").getOrCreate()

validate_data(spark)

revenue_df = transform_data(spark)

laod_data(revenue_df)

spark.stop()
