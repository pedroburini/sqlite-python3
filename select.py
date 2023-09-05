import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME} ORDER BY weight DESC')

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

print()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE weight = 5'
)
row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

cursor.close()
connection.close()
