# 🏠 Home Expense Tracker (DBMS Project)

## 📌 Overview

The **Home Expense Tracker** is a database-driven project designed to manage and analyze daily expenses efficiently.
It uses core **DBMS concepts** such as tables, relationships, constraints, and views to store and process financial data.

---

## 🎯 Features

* Add and manage daily expenses
* Categorize expenses (Food, Transport, etc.)
* Maintain data consistency using **Foreign Keys**
* Generate **monthly expense summaries**
* Simple and structured database design

---

## 🧱 Database Design

### 🟢 Tables Used:

1. **Category Table**

   * Stores expense categories
2. **Expenses Table**

   * Stores transaction details
   * Linked with category using Foreign Key

---

## 🔗 Relationships

* One Category → Many Expenses (**1:N Relationship**)
* Implemented using **Foreign Key constraint**

---

## 📊 View Used

### `monthly_summary`

* Calculates total expenses per month
* Uses:

  * `SUM()`
  * `COUNT()`
  * `GROUP BY`
  * `ORDER BY`

---

## 🧠 DBMS Concepts Covered

* DDL (CREATE DATABASE, TABLE, VIEW)
* DML (INSERT, SELECT)
* Constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL)
* Data Types (INT, VARCHAR, DECIMAL, DATE)
* Aggregate Functions
* Normalization
* Views

---

## ⚙️ Technologies Used

* MySQL
* SQL

---

## 🚀 How to Run

1. Open MySQL / MySQL Workbench
2. Copy and execute the SQL script
3. Database and tables will be created automatically
4. Insert sample data
5. Run queries or view:

   ```sql
   SELECT * FROM monthly_summary;
   ```

---

## 📌 Example Use Case

* Track daily spending
* Analyze monthly expenses
* Manage personal finances

---

## 🔮 Future Improvements

* Add user login system
* Build frontend (Java / Web)
* Add budget alerts
* Add graphical reports

---

## 👨‍💻 Author

Ansh Verma

---

## ⭐ Conclusion

This project demonstrates how **DBMS concepts** can be applied to solve real-world problems like expense tracking using structured data and efficient queries.
