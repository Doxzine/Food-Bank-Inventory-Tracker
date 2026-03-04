#from classes.inventory import Inventory -- Superseded
from classes.user import User
from database import Database

db = Database()

user = User("admin", "password123", "admin") #authorization & authentication change role to admin, viewer, scanner, or stocker for differernt permissions

while True:
    print("\n1. List items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Find item")
    print("5. Quit")

    
    choice = input("What do you want to do? ")
    
    if choice == "1":
        db.list_all()
    elif choice == "2":
        if user.can_do("scan_add"):
            name = input("Item name: ")
            quantity = int(input("Quantity: "))
            type = input("Type: ")
            db.add_item(name, quantity, type)
        else:
            print("You don't have permission to do that")
    elif choice == "3":
        if user.can_do("scan_remove"):
            print("You have: \n")
            db.list_all()
            name = input("Item name: ")
            db.remove_item(name)
        else:
            print("You don't have permission")
    elif choice == "4":
        found_item = input("\nWhat item do you want to find? ")
        result = db.find_item(found_item)
    elif choice == "5":
        break