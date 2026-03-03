from .item import Item

class Inventory():
    def __init__(self):
        self.items = [] ##  <-- Where items are stored during duration of the code
        
    def add_item(self, name, quantity, type):
        new_item = Item(name, quantity, type)
        self.items.append(new_item)
        
    def remove_item(self, name):
        self.items = [i for i in self.items if i.name != name]
        
    def get_item(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None
    def display_all(self):
        for item in self.items:
            print(item)