import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# crud - create read update delete
# sql - insert select update delete

# caution: delete without where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# delete with where
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# create table
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# register values in table columns
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:name, :weight)'
)

""" cursor.execute(sql, ['Joana', 4])
cursor.executemany(
    sql,
    (
        ('Joana', 4), ('Luiz', 5)
    )
) """
cursor.execute(sql, {'name': 'sem nome', 'weight': 3})
cursor.executemany(sql, (
    {'name': 'Joãozinho', 'weight': 3},
    {'name': 'Maria', 'weight': 2},
    {'name': 'Helena', 'weight': 4},
    {'name': 'Joana', 'weight': 5},
))
connection.commit()

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = 1'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} SET name="any", weight=67.89 '
        'WHERE id = 2'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
