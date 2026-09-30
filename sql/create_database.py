from sqlalchemy import create_engine

def get_db():
    engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/telecom_db")

    return engine
