import sqlite3

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
        found_item = res.fetchone()
        if not found_item:
            print(f"\n{name} not found.")
        else:
            name, quantity, type = found_item
            print(f"\n{name} - {quantity} in stock - {type}")
        
            
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
        