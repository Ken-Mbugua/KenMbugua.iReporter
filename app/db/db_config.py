import os
import psycopg2
from flask import current_app


class DbModel():
    def __init__(self):
        """ 
        import variables from current context
        set by Config class
        """
        self.db_name = current_app.config['DB_NAME']
        self.db_user = current_app.config['DB_USERNAME']

        self.conn = psycopg2.connect(database=self.db_name, user=self.db_user)
        self.cur = self.conn.cursor()

    def query(self, query):
        """ pass query statements for execution """
        self.cur.execute(query)

    def save(self):
        """ pass method to commit record """
        self.conn.commit()

    def close(self):
        """ close db connectiion """
        self.cur.close()
        self.conn.close()

    def create_tables(self):
        """
        Loop through tbl_names to create them all
        """
        queries = self.tables()
        for query in queries:
            self.query(query)
        self.close()

    def drop(self, tbl_name):
        """drop table by name"""
        self.query("DROP TABLE IF EXISTS " + tbl_name)
        self.save()

    def destroy_tables(self):
        """
        Loop through tbl_names to drop them all
        """
        queries = self.tables()
        for query in queries:
            self.drop(query)
        self.close()

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
