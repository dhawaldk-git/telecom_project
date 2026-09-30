from logs.create_log import get_logger
import os
def read_data(spark):
    logger = get_logger()
    logger.info("Extract_start")
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(project_root, "data")
    
    customers = spark.read.option('header',True).option("inferSchema", True).csv(os.path.join(data_path,"customers.csv"))

    plans = spark.read.option('header',True).option("inferSchema", True).csv(os.path.join(data_path,"plans.csv"))

    usage = spark.read.option('header',True).option("inferSchema", True).csv(os.path.join(data_path,"usage.csv"))

    recharge = spark.read.option('header',True).option("inferSchema", True).csv(os.path.join(data_path,"recharge.csv"))

    return customers,plans,usage,recharge

