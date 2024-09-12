import sqlite3

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


def add_user(username, email, age):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', '1000'))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    user = cursor.execute('SELECT * FROM Users WHERE username=?', (username,))
    if user.fetchone() is None:
        return False
    else:
        return True
    connection.commit()


connection.commit()
connection.close()


# Продуктовые функции
def initiate_db_product():
    connection_p = sqlite3.connect('database.db')
    cursor_p = connection_p.cursor()
    cursor_p.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    connection_p.commit()
    connection_p.close()


#for i in range(1, 5):
#cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (f'Продукт {i}', f'Описание {i}', f'Цена {i * 100}'))


def get_all_products():
    products_dict = []
    connection_p = sqlite3.connect('database.db')
    cursor_p = connection_p.cursor()
    cursor_p.execute('SELECT * FROM Products')
    products = cursor_p.fetchall()
    for product in products:
        products_dict.append({'title': str(product[1]), 'description': str(product[2]), 'price': str(product[3])})
    connection_p.commit()
    return products_dict
