from sql.create_database import get_db


def laod_data(df):
    engine = get_db()

    pandas_df = df.toPandas()


    pandas_df.to_sql("monthly_revenue",
                    engine,
                    if_exists="replace",
                    index=False)

    print("Data loaded")