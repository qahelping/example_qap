import pytest
import requests
from helpers.db import prepare_db, get_connection


def test_db_example(prepare_db):
    data_db = prepare_db

    for row in data_db:
        _, _, email = row
        assert '@' in email


def test_db_example2(get_connection):
    cursor = get_connection

    cursor.execute('''select c.name, c.phone, c.email from contacts as c
                INNER JOIN address as a
                ON c.id=a.contact_id
                WHERE c.name='CharlieMany'
                ''')
    data_db = cursor.fetchall()

    for row in data_db:
        _, _, email = row
        assert '@' in email
