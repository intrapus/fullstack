import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres',
password='Master00', 
dbname='example', port=5432)

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')
cursor.execute(
"""
create table table2 (
id serial primary key,
completed boolean not null);
""")

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
print(result)

cursor.execute('INSERT INTO table2 (id, completed) VALUES (3,True);')

cursor.execute('SELECT * from table2;')
#---
result2 = cursor.fetchone()
print('fetchone ' , result2)
#---
result = cursor.fetchmany(2)
print('fetchmany ' , result)
#---
result3 = cursor.fetchone()
print('fetchone ' , result3)

conn.commit()
cursor.close()
conn.close()
