class Item():
    def __init__(self, name, quantity, type):
        self.name = name
        self.quantity = quantity
        self.type = type
    
    def add_stock(self, amount):
        self.quantity += amount
        
    def remove_stock(self, amount):
        self.quantity -= amount
        
    def __str__(self):
        return (f"{self.name} - {self.quantity} in stock")
    
