import sqlite3

conn = sqlite3.connect('contact.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS contacts (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone TEXT NOT NULL,
#     email TEXT
# )
# ''')
#
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS address (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     contact_id INTEGER,
#     address TEXT NOT NULL,
#     FOREIGN KEY (contact_id) REFERENCES contacts (id)
# )
# ''')
# cursor.execute('select id, name from contacts')
# rows = cursor.fetchall()
# map = {name: contact_id for contact_id, name in rows}
#
# address = [(map['AliceMany'], '123 Maple St'),
#            (map['BobMany'], '456 Maple St'),
#            (map['CharlieMany'], '90 Maple St')]
#
# cursor.executemany("INSERT INTO address (contact_id, address) VALUES (?, ?)", address)
# conn.commit()

# contacts = [('AliceMany', '123-456-7890', 'alice@example.com'),
#             ('BobMany', '234-567-8901', 'bob@example.com'),
#             ('CharlieMany', '345-678-9012', 'charlie@example.com')]
#
# cursor.executemany("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", contacts)
# conn.commit()


# cursor.execute('select name, email from contacts')
# rows = cursor.fetchall()
#
# for name, email in rows:
#     print(f"{name} - {email}")

# cursor.execute('select name, email from contacts')
# name, email = cursor.fetchone()
# print(f"{name} - {email}")

# cursor.execute('''
# select c.name, c.phone, a.address from contacts as c, address as a
# WHERE c.name='CharlieMany' and c.id=a.contact_id
# ''')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# cursor.execute('''
# select c.name, c.phone, a.address from contacts as c
# INNER JOIN address as a
# ON c.id=a.contact_id
# WHERE c.name='CharlieMany'
# ''')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor.execute('''
# select c.name, c.phone, a.address from contacts as c, address as a
# ORDER BY c.name DESC
# ''')
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# cursor.execute('''
# DELETE FROM contacts
# WHERE name='Alice'
# ''')
# conn.commit()

cursor.execute('select * from contacts')
rows = cursor.fetchall()

for row in rows:
    print(f"{row}")

cursor.execute('UPDATE contacts SET name = "Kareem" WHERE id = 2')
conn.commit()

cursor.execute('select * from contacts')
rows = cursor.fetchall()

for row in rows:
    print(f"{row}")

# name, email = rows[0]
# print(rows[0])
# assert name == 'Alice'
# assert email == 'alice@example.com'

cursor.close()
conn.close()
