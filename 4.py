import sqlite3 

conn = sqlite3.connect('db.sqlite')
c = conn.cursor()

'''
SELECT <what>
FROM <where>
WHERE <условие>
GROUP BY <условие>
HAVING <условие>
ORDER BY <id>
'''

