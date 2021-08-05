#create_tables.py



import psycopg2


# Create database connection

try:
    conn = psycopg2.connect(database="postgres", user="postgres", password="password", host="127.0.0.1", port="5432")
except:
    print("I am unable to connect to the database")
conn.autocommit = True

# Create a cursor

cur = conn.cursor()


# Create table queries

# tweets

cur.execute("DROP TABLE IF EXISTS tweets;")
cur.execute(
"""
CREATE TABLE tweets (
        id SERIAL,
        created_at Date,
        positive INTEGER,
        negative INTEGER,
        neutral INTEGER

)
""")

# tweets_location

cur.execute("DROP TABLE IF EXISTS tweets_location;")
cur.execute(
"""
CREATE TABLE tweets_location (
        id SERIAL,
        created_at Date,
        location TEXT,
        coordinates TEXT,
        geo FLOAT,
        place TEXT
)
""")

## recommendations

cur.execute("DROP TABLE IF EXISTS recommendations;")
cur.execute(
"""
CREATE TABLE recommendations (
        id SERIAL,
        created_at Date,
        recommendation TEXT,
        price DOUBLE PRECISION 
)
""")

# bt_price

cur.execute("DROP TABLE IF EXISTS bt_price;")
cur.execute(
"""
CREATE TABLE bt_price (
        id SERIAL,
        created_at Date,
        price DOUBLE PRECISION 
)
""")

# btc_price_prediction

cur.execute("DROP TABLE IF EXISTS btc_price_prediction;")
cur.execute(
"""
CREATE TABLE btc_price_prediction (
        id SERIAL,
        created_at Date,
        price DOUBLE PRECISION 
)
""")

# btc_price_prediction_rf

cur.execute("DROP TABLE IF EXISTS btc_price_prediction_rf;")
cur.execute(
"""
CREATE TABLE btc_price_prediction_rf (
        id SERIAL,
        created_at Date,
        price DOUBLE PRECISION 
)
""")

# btc_price_prediction_ses

cur.execute("DROP TABLE IF EXISTS btc_price_prediction_ses;")
cur.execute(
"""
CREATE TABLE btc_price_prediction_ses (
        id SERIAL,
        created_at Date,
        price DOUBLE PRECISION 
)
""")

# btc_price_prediction_varmax

cur.execute("DROP TABLE IF EXISTS btc_price_prediction_varmax;")
cur.execute(
"""
CREATE TABLE btc_price_prediction_varmax (
        id SERIAL,
        created_at Date,
        price DOUBLE PRECISION 
)
""")

# btc_price_prediction_overall

cur.execute("DROP TABLE IF EXISTS btc_price_prediction_overall;")
cur.execute(
"""
CREATE TABLE btc_price_prediction_overall (
        id SERIAL,
        created_at Date,
        price DOUBLE PRECISION 
)
""")


# Commit the changes

conn.commit()

# Close the database connection

conn.close()

# Close communication with the PostgreSQL database server

cur.close()
