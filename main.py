import psycopg2
from psycopg2.extras import RealDictCursor

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

def get_db_conn():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            cursor_factory=RealDictCursor
        )
        return conn
    except Exception as e:
        print(f"Exception: {e}")

def change_data(table_name: str):
    conn = get_db_conn()

    try:
        cursor = conn.cursor()
        query = f"UPDATE {table_name} SET id = 10"

        cursor.execute(query)
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    change_data("ids")

if __name__ == "__main__":
    main()