import sqlite3 

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

c.execute('''SELECT film.name, seans.time
          FROM film JOIN seans
          WHERE film.id = seans.film_id
          ORDER BY seans.time
          ''')

print(c.fetchall())

if __name__ == '__main__':
    print('\n!!!\nReady\n!!!')
