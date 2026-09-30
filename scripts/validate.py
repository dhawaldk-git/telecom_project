from scripts.extract import read_data
from logs.create_log import get_logger

def validate_data(spark):
    logger = get_logger()
    customers,plans,usage,recharge = read_data(spark)
    logger.info("validate start")
    print("customer count",customers.count())

    print("usage count:", usage.count())

    customers.dropDuplicates(['customer_id'])
    customers.show()

    return True