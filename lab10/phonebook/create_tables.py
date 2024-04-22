import psycopg2
from lab10.phonebook.config import load_config

def create_tables():
    commands = [
        """CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(100),
                phone_number VARCHAR(20)
        )"""
    ]
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cursor = conn.cursor()
        for command in commands:
            cursor.execute(command)
        conn.commit()
    except psycopg2.Error as error:
        print("Ошибка при выполнении запроса:", error)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    create_tables()
