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
        self.db_password = current_app.config['DB_PASSWORD']
        self.db_host = current_app.config['DB_HOST']
        # password = self.db_password, host = self.db_host

        self.conn = psycopg2.connect(
            database=self.db_name, user=self.db_user,
            password=self.db_password,
            host=self.db_host
        )
        self.cur = self.conn.cursor()

    def query(self, query):
        """ pass query statements for execution """
        result = self.cur.execute(query)
        return result

    def save(self):
        """ pass method to commit record """
        self.conn.commit()

    def close(self):
        """ close db connectiion """
        self.cur.close()  # close cursor connection
        self.conn.close()  # close db connection

    def create_tables(self):
        """
        Loop through tbl_names to create them all
        """
        queries = self.tables()
        for query in queries:
            self.query(query)  # execute queries
            self.save()  # commit changes to db
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
            self.save()
        self.close()

    def tables(self):
        """('now'::text)"""
        users = """ CREATE TABLE IF NOT EXISTS users (
                user_id serial PRIMARY KEY NOT NULL,
                auth_token character varying(256) NOT NULL,
                first_name character varying(50) NOT NULL,
                last_name character varying(50),
                username character varying(50) NOT NULL,
                email character varying(50) ,
                is_admin BOOLEAN,
                date_created timestamp with time zone
                 DEFAULT (now() at time zone 'utc'),
                password_hash character varying(500) NOT NULL
            ) """
        incidents = """ CREATE TABLE IF NOT EXISTS incidents (
                incident_id serial PRIMARY KEY NOT NULL,
                created_on timestamp with time zone
                 DEFAULT (now() at time zone 'utc'),
                created_by numeric NOT NULL,
                type character varying(20) NOT NULL,
                description character varying(200) NOT NULL,
                incident_status character varying(50) NOT NULL,
                location character varying(200),
                comment character varying(512)
            ) """

        queries = [users, incidents]
        return queries
