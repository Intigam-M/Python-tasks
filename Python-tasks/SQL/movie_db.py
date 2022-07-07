import psycopg2

conn = psycopg2.connect(user="postgres", password = "12345", host = "localhost", port = "5432", database = "movie_db")
cursor = conn.cursor()

query = """
    CREATE TABLE film (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        description TEXT,
        views INTEGER DEFAULT 0,
        category_id INTEGER NOT NULL,
        created_date TIMESTAMP NOT NULL,
        has_fragmant BOOLEAN DEFAULT FALSE,
    );

"""

cursor.execute(query)
conn.commit()
