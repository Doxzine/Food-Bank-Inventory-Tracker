from classes.inventory import Inventory
from classes.user import User

inventory = Inventory()
user = User("admin", "password123", "viewer") #authorization & authentication change role to admin, viewer, scanner, or stocker for differernt permissions

while True:
    print("\n1. List items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Quit")
    
    choice = input("What do you want to do? ")
    
    if choice == "1":
        inventory.display_all()
    elif choice == "2":
        if user.can_do("scan_add"):
            name = input("Item name: ")
            quantity = int(input("Quantity: "))
            type = input("Type: ")
            inventory.add_item(name, quantity, type)
        else:
            print("You don't have permission to do that")
    elif choice == "3":
        if user.can_do("scan_remove"):
            print("You have: \n")
            inventory.display_all()
            name = input("Item name: ")
            inventory.remove_item(name)
        else:
            print("You don't have permission")
    elif choice == "4":
        break