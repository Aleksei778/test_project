import psycopg2
from psycopg2.extras import RealDictCursor

from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

create_table_query = """
CREATE TABLE IF NOT EXISTS ids (
    pr SERIAL PRIMARY KEY,
    id INTEGER
    -- Add other columns as needed
);
"""

insert_query = """
INSERT INTO ids(id) VALUES(0);
"""

update_query = """
UPDATE ids SET id = 10;
"""

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

def change_data():
    conn = get_db_conn()

    try:
        cursor = conn.cursor()
        
        cursor.execute(create_table_query)
        cursor.execute(insert_query)
        cursor.execute(update_query)

    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    change_data()

if __name__ == "__main__":
    main()