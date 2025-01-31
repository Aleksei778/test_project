import psycopg2
from psycopg2 import sql

from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

create_db_query = f"CREATE DATABASE {DB_NAME};"

def create_db_user():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
        db_exists = cursor.fetchone()

        if not db_exists:
            cursor.execute(create_db_query)
            print("DB created")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Ошибка в init_db: {e}")

if __name__ == "__main__":
    create_db_user()