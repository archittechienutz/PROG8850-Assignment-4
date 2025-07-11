import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='flyway',
    password='flywaypass',
    database='subscribers'
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
tables = [row[0] for row in cursor.fetchall()]
assert 'subscriber' in tables, "Table 'subscriber' does not exist!"

cursor.execute("DESCRIBE subscriber;")
columns = [col[0] for col in cursor.fetchall()]
required_columns = ['email', 'subscription_date']

for col in required_columns:
    assert col in columns, f"Missing column: {col}"

print("✅ Schema validation passed.")
