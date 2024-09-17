import sqlite3
import logging

class DBManager:
    def __init__(self, db_name="mgTorrent.db"):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler("mgTorrent.log"), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        self.conn = sqlite3.connect(db_name)
        self.create_tables()
        self.logger = logging.getLogger(__name__)

    def create_tables(self):
        try:
            with self.conn:
                self.conn.execute("""
                                CREATE TABLE IF NOT EXISTS users (
                                  id INTEGER PRIMARY KEY,
                                  username TEXT,
                                  password TEXT,
                                  email TEXT
                                )
                                """)
        except sqlite3.Error as e:
            self.logger.error("Error creating users table: {}".format(e))

    def add_user(self, username, password, email):
        try:
            with self.conn:
                self.conn.execute("""
                              INSERT INTO users (username, password, email)
                              VALUES (?, ?, ?)
                                """, (username.lower(), password.lower(), email.lower()))
            self.logger.debug("User added with username: {}, password: {}, email{}".format(username, password, email))
            print("User added Succesfully")
        except sqlite3.Error as e:
            self.logger.error("Error adding user: {}".format(e))

    def get_users(self):
        try:
            with self.conn:
                return self.conn.execute("SELECT * FROM users").fetchall()
        except sqlite3.Error as e:
            self.logger.error("Error finding users: {}".format(e))

    def user_exists(self, user_or_email):
        try:
            with self.conn:
                user_or_email = user_or_email.lower()
                cursor = self.conn.execute("SELECT 1 FROM users WHERE username = ? OR email = ?", (user_or_email, user_or_email))
                return cursor.fetchone() is not None
        except sqlite3.Error as e:
            self.logger.error("Error checking if user exists: {}".format(e))
            return False


    def check_password(self, username_or_email, password):
        try:
            with self.conn:
                username_or_email = username_or_email.lower()
                cursor = self.conn.execute("SELECT password FROM users WHERE username = ? OR email = ?", (username_or_email, username_or_email))
                stored_password = cursor.fetchone()
                if stored_password:
                    return stored_password[0] == password.lower()
                return False
        except sqlite3.Error as e:
            self.logger.error("Error checking password: {}".format(e))
            return False
  