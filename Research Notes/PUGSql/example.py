import sqlite3
from pugsql import characters

conn = sqlite3.connect('sqlite:///users')
conn.character_by_id(conn, {'id':1})

# {'id': 1, 'name': 'Bruno Ribeiro', 'specialty': 'Backend Developer', 'created_at': datetime.datetime(2018, 6, 7, 2, 8, 5, 449020)}
