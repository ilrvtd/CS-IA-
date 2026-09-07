import sqlite3
from Product import Product
from SalesRecord import SalesRecord


class DatabaseManager:
    def __init__(self):

        self.connection = sqlite3.connect("inventory.db")
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):

        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Products (
                        product_ID TEXT PRIMARY KEY, 
                        name TEXT, 
                        selling_price REAL,
                        cost REAL
                            
                    )
                        """)

        self.connection.commit()

        self.cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS SalesRecords(
        record_ID TEXT PRIMARY KEY,
        product_ID TEXT,
        date TEXT ,
        quantity INT ,
        FOREIGN KEY(product_ID) REFERENCES Products(product_ID)) """)

        self.connection.commit()



    def add_product(self, product):

        self.cursor.execute("""
                 INSERT INTO Products 
                 VALUES (?, ?, ?, ?)""",
    (
                 product.product_ID,
                 product.name,
                 product.selling_price,
                 product.cost
        ))
        self.connection.commit()

    def add_sales_record(self, sales_record):

        self.cursor.execute("""
        INSERT INTO SalesRecords 
        VALUES (?, ?, ?, ?)""",
    (
                sales_record.record_ID,
                sales_record.product_ID,
                sales_record.date,
                sales_record.quantity

                ))
        self.connection.commit()



    def get_all_products(self):

        self.cursor.execute("""
        SELECT * FROM Products""")

        rows = self.cursor.fetchall()

        products = []

        for row in rows:
          product = Product(row[0], row[1], row[2], row[3])
          products.append(product)

        return products

    def get_all_sales_records(self):
        self.cursor.execute("""
        SELECT * FROM SalesRecords""")
        rows = self.cursor.fetchall()
        sales_records = []
        for row in rows:
            sales_record = SalesRecord(row[0], row[1], row[2], row[3])
            sales_records.append(sales_record)
        return sales_records


    def delete_product(self, product_ID):

        self.cursor.execute("""
        DELETE FROM Products
        WHERE product_ID = ?
        """, (product_ID,))
        self.connection.commit()


    def update_product_name(self, product_ID, new_name):

        self.cursor.execute("""
        UPDATE Products
        SET name = ?
        WHERE product_ID = ?
        """, (new_name, product_ID))

        self.connection.commit()


    def update_product_selling_price(self, product_ID,new_selling_price):

        self.cursor.execute("""
        UPDATE Products
        SET selling_price = ?
        WHERE product_ID = ?
        """, (new_selling_price, product_ID))

        self.connection.commit()


    def update_product_cost(self, product_ID, new_cost):

        self.cursor.execute("""
        UPDATE Products
        SET cost = ?
        WHERE product_ID = ?
        """, (new_cost,product_ID))
        self.connection.commit()

    def update_sales_record_date(self, record_ID,date):

        self.cursor.execute("""
        UPDATE SalesRecords
        SET date = ?
        WHERE record_ID = ?
        """, (date,record_ID))

        self.connection.commit()


    def update_sales_record_quantity(self, record_ID, quantity):

        self.cursor.execute("""
        UPDATE SalesRecords
        SET quantity = ?
        WHERE record_ID = ?
        """, (quantity,record_ID))
        self.connection.commit()

    def update_sales_record_product (self,record_ID, product_ID):

        self.cursor.execute("""
        UPDATE SalesRecords
        SET product_ID = ?
        WHERE record_ID = ? """, (product_ID,record_ID))
        self.connection.commit()

    def delete_sales_record(self, record_ID):

        self.cursor.execute("""
        DELETE FROM SalesRecords
        WHERE record_ID = ?
            """, (record_ID,))

        self.connection.commit()

    def delete_all_sales_records_by_product_ID(self, product_ID):

        self.cursor.execute("""
        DELETE FROM SalesRecords
        WHERE product_ID = ?
            """, (product_ID,))

        self.connection.commit()


    def get_product_by_id(self, product_ID):

        self.cursor.execute("""
        SELECT * FROM Products
        WHERE product_ID = ?
        """, (product_ID,))

        row = self.cursor.fetchone()

        if row is not None:
            product = Product(row[0], row[1], row[2], row[3])
            return product

        return None

    def get_sales_record_by_id(self, record_ID):

        self.cursor.execute("""
        SELECT * FROM SalesRecords
        WHERE record_ID = ?
        """, (record_ID,))

        row = self.cursor.fetchone()

        if row is not None:
            sales_record = SalesRecord(row[0], row[1], row[2], row[3])
            return sales_record
        return None
    
    def close_connection(self):
        self.connection.close()


