import sqlite3
import datetime

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

def insert_films():
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
    conn.commit()
    print('Films written successfully!')

def insert_hall():
    while True:
        seats = input('Amount of seats: ')
        c.execute('''INSERT INTO hall (seats)
                  VALUES (?)
                  ''', (seats,))
        if seats == '':
            break
    conn.commit()
    print('Halls written successfully!')

def insert_seans():
    while True:
        hall_id = input('Hall number: ')
        film =  input('Film: ')
        film_id = [list(row) for row in c.execute('SELECT id FROM film WHERE film = ?', (film,))][0]
        if not film:
            film =  input('There is no such film. Try again: ')
        date = str(datetime.datetime.now().date())
        time = input('Time: ')
        while True:
            cost = input('Cost in RON: ')
            if not isinstance(cost, int):
                cost = input('Just write the number! ')
            else:
                break
        while True:
            tickets_sold = input('Amount of sold tickets: ')
            if not isinstance(tickets_sold, int):
                tickets_sold = input('Just write the number! ')
            else:
                break
        tickets = [list(row) for row in c.execute('SELECT seats FROM hall WHERE id = ?', (hall_id,))][0] - tickets_sold
        c.execute('''INSERT INTO seans (hall_id, film_id, date, time, cost, tickets)
                  VALUES (?, ?, ?, ?, ?, ?)
                  ''', (hall_id, film_id, date, time, cost, tickets))
        if hall_id == '':
            break
    conn.commit()
    print('Seansy written successfully!')

if __name__ == '__main__':
    insert_films()
    insert_hall()
    insert_seans()
