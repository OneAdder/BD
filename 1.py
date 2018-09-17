import sqlite3

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

def drop_all():
    c.execute('DROP TABLE IF EXISTS film')
    c.execute('DROP TABLE IF EXISTS seans')
    c.execute('DROP TABLE IF EXISTS zal')

def create_film():
    c.execute('''CREATE TABLE film (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              length INTEGER,
              abstract TEXT,
              rating TEXT,
              age TEXT)
              ''')
    conn.commit()
    print('"film" created;')

def create_seans():
    c.execute('''CREATE TABLE seans (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              hall_id INTEGER,
              film_id INTEGER,
              date TEXT,
              time TEXT,
              cost INTEGER,
              tickets INTEGER)
              ''')
    conn.commit()
    print('"seans" created;')

def create_hall():
    c.execute('''CREATE TABLE hall (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              seats INTEGER)
              ''')
    conn.commit()
    print('"zal" created;')

def create_all():
    drop_all()
    create_film()
    create_seans()
    create_hall()
    print('\nAll tables created!')

def insert():
    while True:
        name = input('Film name: ')
        length = input('Length: ')
        abstract = input('Abstract: ')
        rating = input('Rating: ')
        age = input('PEGI: ')
        c.execute('''INSERT INTO film (name, length, abstract, rating, age)
                  VALUES (?, ?, ?, ?, ?)
                  ''', (name, length, abstract, rating, age))
        if name == '':
            break
    print('Films written successfully!')

if __name__ == '__main__':
    insert()
