import psycopg2
from psycopg2 import sql

from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

DB_MAIN_USER = "postgres"
DB_MAIN_PASS = "postgres"

create_db_query = f"CREATE DATABASE {DB_NAME};"
create_user_query = f"CREATE USER {DB_USER} WITH ENCRYPTED PASSWORD '{DB_PASS}';"
grant_privileges_query = f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER};"

def create_db_user():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_MAIN_USER,
            password=DB_MAIN_PASS
        )
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
        db_exists = cursor.fetchone()

        if not db_exists:
            cursor.execute(create_db_query)
            print("DB created")

        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_roles WHERE rolname = '{DB_USER}';")
        user_exists = cursor.fetchone()

        if not user_exists:
            cursor.execute(create_db_user)
            print("User created")

        cursor.execute(grant_privileges_query)
        print("Привелегии выданы")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    create_db_user()