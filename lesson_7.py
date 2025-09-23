import sqlite3

def create_tables():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INT,
        city TEXT,
        )
    """)

def add_student(name, age, city):
    conn.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)"
    )
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect('datebase.db')
    create_tables()
    add_student('John', '25', city='New York')
    