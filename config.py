import psycopg2

def connection():
    connection = psycopg2.connect(
        user="postgres",
        password="6309121028",
        host="localhost",
        port="5432",
        database="employess")
    return connection

