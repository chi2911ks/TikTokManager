import sqlite3


conn = sqlite3.connect('data.db')
cursor = conn.cursor()
statement = '''SELECT DISTINCT type FROM accounts;'''

cursor.execute(statement)


output = cursor.fetchall()
print(output)