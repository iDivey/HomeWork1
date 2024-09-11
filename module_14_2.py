import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# - комментировал при новых запусках
#for i in range(1, 11):
    #cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', f'{1000}'))

# - комментировал при новых запусках
#for i in range(1, 11, 2):
    #ursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, f'{i}'))

#for i in range(1, 11, 3):
    #cursor.execute('DELETE FROM Users WHERE id = ?', (f'{i}',))

#cursor.execute('DELETE FROM Users WHERE id = ?', (f'6',))

cursor.execute('SELECT COUNT(*) FROM Users')
all_ = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]
print(sum_balance/all_)


connection.commit()
connection.close()
