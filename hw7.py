import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(error)
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def insert_products(connection, products):
    try:
        sql = '''
            INSERT INTO products 
            (product_title, price, quantity)
            VALUES 
            (?, ?, ?)
        '''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

def update_products(connection, products):
    try:
        sql = '''
            UPDATE products SET price = ?
            WHERE id = ?            
        '''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(error)

def delete_products(connection, id):
    try:
        sql = '''
            DELETE FROM products WHERE id = ?            
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(error)

def select_all_products(connection):
    try:
        sql = '''
            SELECT * FROM products
        '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def select_products_below_price_and_above_quantity_limit(connection, price_limit, quantity_limit):
    try:
        sql = '''
            SELECT * FROM products WHERE price < ? AND quantity > ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def search_products_by_title(connection, search_term):
    try:
        sql = '''
            SELECT * FROM products WHERE product_title LIKE ?
        '''
        cursor = connection.cursor()
        cursor.execute(sql, ('%'+search_term+'%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

sql_to_create_products_table = ''' 
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''


my_connection = create_connection('hw.db')
if my_connection:
    print("Connected successfully to database")
    create_table(my_connection, sql_to_create_products_table)
    # insert_products(my_connection, ('banana', 200.0, 6))
    # insert_products(my_connection, ('milk', 150.0, 2))
    # insert_products(my_connection, ('bread', 50.0, 2))
    # insert_products(my_connection, ('chocolate', 400.0, 3))
    # insert_products(my_connection, ('curd', 260.0, 2))
    # insert_products(my_connection, ('orange', 360.0, 7))
    # insert_products(my_connection, ('soap', 180.0, 3))
    # insert_products(my_connection, ('Liquid soap with vanilla scent', 255.5, 3))
    # insert_products(my_connection, ('Baby soap', 360.0, 4))
    # insert_products(my_connection, ('oil', 620, 3))
    # insert_products(my_connection, ('juice', 275.0, 5))
    # insert_products(my_connection, ('lemon', 290.0, 9))
    # insert_products(my_connection, ('ice cream', 300, 6))
    # insert_products(my_connection, ('mango', 700.0, 7))
    # insert_products(my_connection, ('yogurt', 400.0, 8))
    # update_products(my_connection, (266, 2))
    delete_products(my_connection, 15)
    select_all_products(my_connection)
    select_products_below_price_and_above_quantity_limit(my_connection, 100, 5)
    my_connection.close()