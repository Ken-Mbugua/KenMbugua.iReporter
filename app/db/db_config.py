import os
import psycopg2
from flask import current_app


class DbModel():
    def __init__(self, app=None):
        """
        import variables from current context
        set by Config class
        """

        self.app = app
        current_context = self.context_switcher()
        self.db_name = current_context.config['DB_NAME']
        self.db_user = current_context.config['DB_USERNAME']
        self.db_password = current_context.config['DB_PASSWORD']
        self.db_host = current_context.config['DB_HOST']
        # password = self.db_password, host = self.db_host
        self.conn = psycopg2.connect(
            database=self.db_name, user=self.db_user,
            password=self.db_password,
            host=self.db_host
        )
        try:
            self.cur = self.conn.cursor()
            print("CONNECTION_SUCCESS!!")
        except:
            print("CONNECTION_ERROR!!")

        self.table_names = ["users", "incidents"]

    def context_switcher(self):
        """get current passed context to the dbModel"""
        if current_app:
            return current_app
        else:
            return self.app

    def query(self, query, data=None):
        """ pass query statements for execution """
        self.cur.execute(query, data or ())

    def find_all(self):
        """method to return all table data"""
        return self.cur.fetchall()

    def find_one(self):
        """method to return all table data"""
        return self.cur.fetchone()

    def find_fields(self):
        """ return fields of the queried table"""

        fields = [field[0] for field in self.cur.description]
        return fields

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
        # self.close()

    def drop(self, tbl_name):
        """drop table by name"""
        self.query("DROP TABLE IF EXISTS " + tbl_name+" CASCADE")
        self.save()

    def truncate(self, tbl_name):
        """truncate table by name"""
        self.query("TRUNCATE " + tbl_name+" RESTART IDENTITY CASCADE")
        self.save()

    def destroy_tables(self):
        """
        Loop through tbl_names to drop them all
        """
        tables = self.table_names
        for table in tables:
            self.drop(table)
            self.save()
        self.close()

    def truncate_tables(self):
        """
        Loop through tbl_names to truncate them all
        """
        tables = self.table_names
        for table in tables:
            self.truncate(table)
            self.save()
        self.close()

    def tables(self):
        # users table
        self.table_names[0] = """ CREATE TABLE IF NOT EXISTS users (
                user_id serial PRIMARY KEY NOT NULL,
                username character varying(50) NOT NULL,
                email character varying(50) NOT NULL,
                password_hash character varying(500) NOT NULL,
                first_name character varying(50),
                last_name character varying(50),
                phone_number character varying(50) ,
                is_admin BOOLEAN,
                date_created timestamp with time zone
                 DEFAULT (now() at time zone 'utc')
            ) """

        # incidents table
        self.table_names[1] = """ CREATE TABLE IF NOT EXISTS incidents (
                incident_id serial PRIMARY KEY NOT NULL,
                created_on timestamp with time zone
                 DEFAULT (now() at time zone 'utc'),
                created_by int NOT NULL,
                title character varying (200) NOT NULL,
                incident_type character varying(20) NOT NULL,
                description character varying(200) NOT NULL,
                incident_status character varying(50) NOT NULL,
                image character varying(500)[],
                video character varying(500)[],
                location character varying(200),
                comment character varying(512)
            ) """

        queries = [self.table_names[0], self.table_names[1]]
        return queries

    def seed_admin_user(self):
        """method to seed admin"""

        create_admin = """ INSERT INTO users (
            username,
            email,
            password_hash,
            is_admin
        )
        SELECT
            'k_mbugua',
            'kmbugua@mail.com',
            '$2b$12$ydWOi22vO4KKnbsp8s5Z.O1tqErTN2pj1wuaEawYEIWLQVEKBi9xq',
            TRUE
        WHERE
            NOT EXISTS (
                 SELECT email FROM users WHERE email = 'kmbugua@mail.com'
            ) """

        self.query(create_admin)
        self.save()
        self.close()
