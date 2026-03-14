import sqlite3
import hashlib
import secrets
from datetime import datetime

class Database():
    def __init__(self):
        self.con = sqlite3.connect("inventory.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_table()
        
    
    def create_table(self): 
        new_table = self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS inventory(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE,
                        quantity INTEGER,
                        type TEXT  
                    )
                    """)
        self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE,
                        password TEXT,
                        salt TEXT,
                        role TEXT 
                    )
                    """)
        self.cur.execute("""
                    CREATE TABLE IF NOT EXISTS audit(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        action TEXT,
                        details TEXT,
                        timestamp TEXT 
                    )
                    """)

    ##Adding item    
    def add_item(self, name, quantity, type):
        try:
            self.cur.execute("INSERT INTO inventory (name, quantity, type) VALUES (?, ?, ?)", 
                            (name.lower(), quantity, type.lower()))
            self.con.commit()
        except sqlite3.IntegrityError:
            print(f"{name} already exists, updated quantity instead")
            self.update_quantity(name, quantity)
            
            
    def remove_item(self, name):
        self.update_quantity(name, 0)
         

    def find_item(self, name):
        res = self.cur.execute("SELECT name, quantity, type FROM inventory WHERE name = ?", (name.lower(),))
        return res.fetchone()

        
            
    def update_quantity(self, name, quantity):
        self.cur.execute("UPDATE inventory SET quantity = ? WHERE name = ?",
                         (quantity, name.lower()))
        self.con.commit()
    
    
    def list_all(self):
        res = self.cur.execute("SELECT name, quantity, type FROM inventory")
        return res.fetchall()
        
    
    def close(self):
        self.con.close()
        
        
    def add_user(self, username, password, role):
        try:
            salt = secrets.token_hex(16)
            hashed = hashlib.sha256((password + salt).encode()).hexdigest()
            self.cur.execute("INSERT INTO users(username, password, salt, role) VALUES (?, ?, ?, ?)", 
                            (username.lower(), hashed, salt, role.lower()))
            self.con.commit()
        except sqlite3.IntegrityError:
            print(f"{username} already exists")
            
    def get_user(self, username):
        res = self.cur.execute("SELECT username, password, salt, role FROM users WHERE username = ?",
                            (username.lower(),))
        return res.fetchone()
    
    def list_users(self):
        res = self.cur.execute("SELECT username, role FROM users")
        return res.fetchall()
    
    def remove_user(self, username):
        self.cur.execute("DELETE FROM users WHERE username = ?", (username.lower(),))
        self.con.commit()
    
    def admin(self):
        if not self.get_user("admin"):
            self.add_user("admin", "admin", "admin")


    def log_action(self, username, action, details):
        self.cur.execute("INSERT INTO audit(username, action, details, timestamp) VALUES (?, ?, ?, ?)",
                        (username, action, details, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.con.commit()
            

    def list_audit_log(self):
        res = self.cur.execute("SELECT username, action, details, timestamp FROM audit")
        return res.fetchall()
    