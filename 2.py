import sqlite3
import datetime

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

query = """SELECT film_id
        FROM Seans
        WHERE date LIKE '2018%'"""
x = c.execute(query)
print(x.fetchall())

if __name__ == '__main__':
    print('\n!!!\nReady\n!!!')
 
