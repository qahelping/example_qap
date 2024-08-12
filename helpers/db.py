import sqlite3

import pytest


@pytest.fixture
def prepare_db():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS address (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_id INTEGER,
        address TEXT NOT NULL,
        FOREIGN KEY (contact_id) REFERENCES contacts (id)
    )
    """
    )
    contacts = [
        ("AliceMany", "123-456-7890", "alice@example.com"),
        ("BobMany", "234-567-8901", "bob@example.com"),
        ("CharlieMany", "345-678-9012", "charlie@example.com"),
    ]

    cursor.executemany(
        "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", contacts
    )
    conn.commit()

    cursor.execute("select id, name from contacts")
    rows = cursor.fetchall()
    map = {name: contact_id for contact_id, name in rows}

    address = [
        (map["AliceMany"], "123 Maple St"),
        (map["BobMany"], "456 Maple St"),
        (map["CharlieMany"], "90 Maple St"),
    ]

    cursor.executemany(
        "INSERT INTO address (contact_id, address) VALUES (?, ?)", address
    )
    conn.commit()

    cursor.execute(
        """select c.name, c.phone, c.email from contacts as c
                INNER JOIN address as a
                ON c.id=a.contact_id
                WHERE c.name='CharlieMany'
                """
    )
    yield cursor.fetchall()

    cursor.close()
    conn.close()


@pytest.fixture
def get_connection():
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()

    yield cursor

    cursor.close()
    conn.close()
