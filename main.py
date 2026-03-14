#from classes.inventory import Inventory -- Superseded
from classes.user import User
from database import Database
import hashlib

db = Database()


db.admin() #Creates a default admin login (admin, admin)


while True:
    username = input("Username: ")
    password = input("Password: ")
    row = db.get_user(username)
    if row and row[1] == hashlib.sha256((password + row[2]).encode()).hexdigest():
        user = User(row[0], row[1], row[3])
        print(f"Welcome {user.username}")
        break
    else:
        print("Invalid username or password, try again.\n")



while True:
    print("\n1. List items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Find item")
    print("5. Manage Users")
    print("6. Audit Log")
    print("7. Quit")

    
    choice = input("What do you want to do?\n")
    
    if choice == "1":
        items = db.list_all()
        if not items:
            print("\nInventory is empty")
        else:
            for item in items:
                print(item)
    elif choice == "2":
        if user.can_do("scan_add"):
            try:
                name = input("Item name: ")
                quantity = int(input("Quantity: "))
                if quantity < 0:
                    print("Quantity can't be negative")
                    continue
                type = input("Type: ")
            except ValueError:
                print("Please input numbers")
                continue
                
            db.add_item(name, quantity, type)
            db.log_action(user.username, "added item", f"{quantity} {name}")
        else:
            print("You don't have permission to do that")
    elif choice == "3":
        if user.can_do("scan_remove"):
            print("You have: \n")
            items = db.list_all()   
            name = input("Item name: ")
            db.remove_item(name)
            db.log_action(user.username, "removed item", f"{name}")
        else:
            print("You don't have permission")
    elif choice == "4":
        name = input("\nWhat item do you want to find? ")
        result = db.find_item(name)
        if not result:
            print(f"\n{name} not found")
        else: 
            name, quantity, type = result
            print(f"\n{name} - {quantity} in stock - {type}")
            
    elif choice == "5":
        if user.can_do("manage_users"):
            print("\n1. Add user")
            print("2. Remove user")
            print("3. List users")
            action = input("Choose: ")
            if action == "1":
                new_user = input("Username: ")
                new_pass = input("Password: ")
                new_role = input("Role: ")
                db.add_user(new_user, new_pass, new_role)
                db.log_action(user.username, "created user", f"{new_user} as {new_role}")
            elif action == "2":
                remove = input("Username to remove: ")
                if remove.lower() == user.username:
                    print("Can't remove yourself")
                elif db.get_user(remove):
                    confirm = input(f"Are you sure you want to remove {remove}? (1 = Yes, 2 = No): ")
                    if confirm == "1":
                        db.remove_user(remove)
                        db.log_action(user.username, "removed user", f"{remove}")
                        print(f"{remove} removed")
                    else:
                        print("Cancelled")
                else:
                    print(f"{remove} not found")
            elif action == "3":
                users = db.list_users()
                if not users:
                    print("No users found")
                else:
                    for u in users:
                        print(f"{u[0]} - {u[1]}")
        else:
            print("You don't have permission")
            
    elif choice == "6":
        if user.can_do("manage_users"):
            logs = db.list_audit_log()
            if not logs:
                print("\nNo actions have been taken.")
            else:
                for log in logs:
                    print(f"{log[3]} - {log[0]} - {log[1]} - {log[2]}")
        else:
            print("You don't have permission")
    
    elif choice == "7":
        db.close()
        break