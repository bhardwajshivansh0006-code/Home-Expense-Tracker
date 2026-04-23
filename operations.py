# operations.py - All Database Operations

from db import get_connection


def add_expense(date, name, amount, category_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO expenses (date, name, amount, category_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (date, name, amount, category_id))
    conn.commit()
    cursor.close()
    conn.close()


def get_all_expenses():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT e.id, e.date, e.name, e.amount, c.category_name AS category
        FROM expenses e
        JOIN category c ON e.category_id = c.category_id
        ORDER BY e.date DESC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in rows:
        row['date'] = str(row['date'])
        row['amount'] = float(row['amount'])
    return rows


def update_expense(expense_id, new_amount):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE expenses SET amount = %s WHERE id = %s"
    cursor.execute(query, (new_amount, expense_id))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected > 0


def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM expenses WHERE id = %s"
    cursor.execute(query, (expense_id,))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected > 0


def get_monthly_total():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT DATE_FORMAT(date, '%Y-%m') AS month,
               SUM(amount) AS total,
               COUNT(*) AS count
        FROM expenses
        GROUP BY DATE_FORMAT(date, '%Y-%m')
        ORDER BY month DESC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in rows:
        row['total'] = float(row['total'])
    return rows


def get_category_total():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT c.category_name AS category,
               SUM(e.amount) AS total,
               COUNT(*) AS count
        FROM expenses e
        JOIN category c ON e.category_id = c.category_id
        GROUP BY c.category_name
        ORDER BY total DESC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in rows:
        row['total'] = float(row['total'])
    return rows


def get_monthly_summary_view():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM monthly_summary")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in rows:
        row['total_amount'] = float(row['total_amount'])
    return rows


def get_categories():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT category_id, category_name FROM category")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows