# Class that handles Database operations.

import sqlite3

class DBHandler:
    def __init__(self, db_name="mgTorrent.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
            
    def create_tables(self): #TODO: implementar Try-Catch. 
        try:
            with self.conn:
            #Create user table if it doesn't exist
                self.conn.execute("""
                                CREATE TABLE IF NOT EXISTS users (
                                  id INTEGER PRIMARY KEY,
                                  username TEXT,
                                  password TEXT,
                                  email TEXT
                                )
                                """)
        except:
            print("Error Creating the usernames Table")        

    def add_user(self, username, password, email):
        try: 
            with self.conn:
                self.conn.execute("""
                              INSERT INTO users (username, password, email)
                              VALUES (?, ?, ?)
                                """, (username, password, email))    
        except: 
            print("Error adding user")
            
    def get_users(self):
        try:
            with self.conn:
                return self.conn.execute("SELECT * FROM users").fetchall()
        except:
            print("Error Finding User")            