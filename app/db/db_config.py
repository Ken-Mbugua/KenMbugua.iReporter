import os
import psycopg2

url = " dbname='km-ireporter', host='localhost', port='5432',\
      user='k-mbugua', password='k-mbugua54321' "

db_url = os.getenv('DATABASE_URL')

test_url = " dbname = 'test_km-ireporter', host = 'localhost', port = '5432',\
            user='k-mbugua', password='mbugu4K54321' "


def connection(url):
    conn = psycopg2.connect(url)
    return conn


def init_db(url):
    conn = connection(url)
    return conn


def init_test_db(test_url):
    conn = connection(test_url)
    return conn


def create_tables():
    conn = connection(url)
    cursor = conn.cursor()
    queries = tables()

    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    pass


def tables():
    users = """ CREATE TABLE IF NOT EXISTS users (
        user_id serial PRIMARY KEY NOT NULL,
        first_name character varying(50) NOT NULL,
        last_name character varying(50),
        username character varying(50) NOT NULL,
        email character varying(50) ,
        is_admin bolean,
        data_created timestamp with time zone DEFAULT ('now'::text),
        password_hash character varying(500) NOT NULL
    ) """
    incidents = """ CREATE TABLE IF NOT EXISTS users (
        incident_id serial PRIMARY KEY NOT NULL,
        created_on timestamp with time zone DEFAULT ('now'::text),
        created_by numeric NOT NULL,
        type character varying(20) NOT NULL,
        description character varying(200) NOT NULL,
        status character varying(50) NOT NULL,
        location character varying(200) NOT NULL
    ) """

    queries = [users, incidents]
    return queries
