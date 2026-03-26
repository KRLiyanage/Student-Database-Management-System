import mysql.connector
from tkinter import messagebox

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="user_db"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Check if the MySQL server is running.\nError: {err}")
        return None

def setup_database():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(100),
                    last_name VARCHAR(100),
                    email VARCHAR(150) UNIQUE,
                    password VARCHAR(255)
                )
            """)
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as e:
            print(f"Table creation error: {e}")
            
            

if __name__ == "__main__":
    setup_database()
    print("Table created successfully!")            