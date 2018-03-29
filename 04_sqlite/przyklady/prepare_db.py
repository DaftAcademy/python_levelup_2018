import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

with open('sqlite-sakila-schema.sql', 'r', encoding='utf-8') as create_file:
    create_query = create_file.read()
with open('sqlite-sakila-insert-data.sql', 'r', encoding='utf-8') as insert_file:
    insert_query = insert_file.read()

c.executescript(create_query)
c.executescript(insert_query)

conn.commit()
conn.close()
