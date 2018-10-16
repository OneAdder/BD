import sqlite3
import datetime

conn = sqlite3.connect('db.sqlite', check_same_thread=False)
c = conn.cursor()

def log_writer(s):
    noww = datetime.datetime.now()
    with open("sql_log", 'a', encoding = "UTF-8") as f:
        f.write(str(noww) + ' - ' + s)


def show_all():
    return c.execute('''
                     SELECT workers.id,
                     workers.name,
                     workers.patronymic,
                     workers.surename,
                     rooms.id
                     FROM workers
                     JOIN rooms 
                     WHERE workers.room_id = rooms.id
                     ''').fetchall()

def add_worker(info):
    room = 0
    for roome in c.execute('''
                           SELECT id, seats
                           FROM rooms
                           '''):
        if roome[1] > 0:
            room = roome[0]
    if room == 0:
        return 1
    c.execute('''
              UPDATE rooms
              SET seats = seats - 1
              WHERE id = ?
              ''', (room,))
    c.execute('''
              INSERT INTO workers
              (name, patronymic, surename, room_id)
              VALUES (?, ?, ?, ?)
              ''', (info['name'], info['patronymic'], info['surename'], room))
    conn.commit()
    log_writer('Worker ' + info['patronymic'] + ' added to room ' + str(room) + '\n')
    return

def delete_worker(worker_id):
    patr = c.execute('''
                     SELECT patronymic
                     FROM workers
                     WHERE id = ?
                     ''', (worker_id,)).fetchone()[0]
    room_id = c.execute('''
                        SELECT room_id
                        FROM workers
                        WHERE id = ?
                        ''', (worker_id,)).fetchone()[0]
    c.execute('''
              DELETE FROM workers
              WHERE id = ?
              ''', (worker_id,))
    c.execute('''
              UPDATE rooms
              SET seats = seats + 1
              WHERE id = ?
              ''', (room_id,))
    conn.commit()
    log_writer('Worker ' + patr + ' deleted\n')
