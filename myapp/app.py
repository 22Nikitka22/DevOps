import os
import psycopg2
from psycopg2 import OperationalError

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname=os.getenv("DB_NAME")
        )
        print("Подключение к PostgreSQL установлено!")
    except OperationalError as e:
        print(f"Ошибка '{e}' при подключении к PostgreSQL")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запрос выполнен успешно")
    except OperationalError as e:
        print(f"Ошибка '{e}' при выполнении запроса")
    finally:
        cursor.close()

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
        """
        execute_query(connection, create_table_query)

        insert_user_query = "INSERT INTO users (name) VALUES ('John Doe');"
        execute_query(connection, insert_user_query)

        select_users_query = "SELECT * FROM users;"
        cursor = connection.cursor()
        cursor.execute(select_users_query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        connection.close()