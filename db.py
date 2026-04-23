# db.py - Database Connection

import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",           # ← your MySQL password
        database="expense_tracker"
    )
    return connection