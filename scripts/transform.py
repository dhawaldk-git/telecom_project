from scripts.extract import read_data
from pyspark.sql.functions import *
from logs.create_log import get_logger

def transform_data(spark):
    logger = get_logger()
    logger.info("Transform Started")
    customers,plans,usage,recharge = read_data(spark)
    
    revenue_df = usage.join(plans,'plan_id',"inner")

    revenue_df = revenue_df.withColumn("estimated_revenue",col("monthly_charge"))

    revenue_df.show()

    return revenue_df