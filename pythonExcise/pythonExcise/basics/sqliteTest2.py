import sqlite3

conn = sqlite3.connect("C:\\ying\\python3\\trunk\\pythonExcise\\pythonExcise\\db\\example.db")
c = conn.cursor()

# refer to sqliteTest1.py for creation of db and table . 


t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print (c.fetchone())


'''
# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

'''

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)