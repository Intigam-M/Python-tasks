import psycopg2

conn = psycopg2.connect(user="postgres", password = "12345", host = "localhost", port = "5432", database = "store")
cursor = conn.cursor()

query = """
    CREATE TABLE film (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        stock INTEGER DEFAULT 0,
        views INTEGER DEFAULT 0,
        discount INTEGER NOT NULL,
        seller_id INTEGER NOT NULL,
        created_date TIMESTAMP NOT NULL,
        expiry_date TIMESTAMP NOT NULL,
        price INTEGER NOT NULL,
        number_of_sales INTEGER DEFAULT 0,
        barcode VARCHAR(50) NOT NULL,
    );

"""

cursor.execute(query)
conn.commit()
