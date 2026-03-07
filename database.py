import sqlite3
import hashlib

class Database():
    def __init__(self):
        self.con = sqlite3.connect("inventory.db")
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
                        role TEXT 
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
        items = res.fetchall()
        if not items:
            print("\nInventory is empty")
        else:
            for item in items:
                print("")
                print(item)
        
    
    def close(self):
        self.con.close()
        
        
    def add_user(self, username, password, role):
        try:
            self.cur.execute("INSERT INTO users(username, password, role) VALUES (?, ?, ?)", 
                            (username.lower(),hashlib.sha256(password.encode()).hexdigest(), role.lower()))
            self.con.commit()
        except sqlite3.IntegrityError:
            print(f"{username} already exists")
            
    def get_user(self, username):
        res = self.cur.execute("SELECT username, password, role FROM users WHERE username = ?",
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
