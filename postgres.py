import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres',
password='Master00', 
dbname='example', port=5432)

cur = conn.cursor()
cur.execute(
"""
create table todos (
id serial primary key,
description varchar not null);
""")

conn.commit()
cur.close()
conn.close()
