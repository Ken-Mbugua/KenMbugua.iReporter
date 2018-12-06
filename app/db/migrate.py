import os
from .db_config import DbModel

db = DbModel()


def create_tables(self):
    queries = self.tables()
    for query in queries:
        db.query(query)
    db.close()


def destroy_tables(self):
    self.conn.commit()


def tables(self):
    users = """ CREATE TABLE IF NOT EXISTS users (
            user_id serial PRIMARY KEY NOT NULL,
            auth_token character varyin(256) NOT NULL,
            first_name character varying(50) NOT NULL,
            last_name character varying(50),
            username character varying(50) NOT NULL,
            email character varying(50) ,
            is_admin bolean,
            date_created timestamp with time zone DEFAULT ('now'::text),
            password_hash character varying(500) NOT NULL
        ) """
    incidents = """ CREATE TABLE IF NOT EXISTS users (
            incident_id serial PRIMARY KEY NOT NULL,
            created_on timestamp with time zone DEFAULT ('now'::text),
            created_by numeric NOT NULL,
            type character varying(20) NOT NULL,
            description character varying(200) NOT NULL,
            incident_status character varying(50) NOT NULL,
            location character varying(200),
            comment character varying(512)
        ) """

    queries = [users, incidents]
    return queries
