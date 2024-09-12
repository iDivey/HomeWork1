import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')


initiate_db()
#for i in range(1, 5):
    #cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (f'Продукт {i}', f'Описание {i}', f'Цена {i * 100}'))


def get_all_products():
    products_dict = []
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    for product in products:
        products_dict.append({'title': str(product[1]), 'description': str(product[2]), 'price': str(product[3])})
    return products_dict


connection.commit()
connection.close()
