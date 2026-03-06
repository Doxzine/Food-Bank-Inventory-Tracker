# Food Bank Inventory System

An inventory management multi-role system made for food banks to track supply with different user permissions based on job roles.

### Tech Stack
- Python | Core Logic (Current)
- C++ | Backend & API (Planned)
- SQL | Database (Current)
- Java | QR Code generation (Planned)

### Features
- Role-based access with 4 current roles (Viewer, scanner, stocker, & admin).
- Real time inventory tracking.
- Stock management with the ability to add/remove items.

### Planned Features
- QR Code scanning
- Nutritional value threshold system (Must meet a certain nutritional score).
- Demand prediction with pandas based on upcoming holidays or days of the week.
- Web frontend


## How to run
1) Run the main.py file
2) Login for default account is admin for username & password
3) Roles for creating a new user is (Viewer, Stocker, Scanner, Admin)
   - Viewer can only view
   - Stocker can add and remove inventory
   - Scanner can only add
   - Admin has full permission
4) Reset data by deleting the inventory.db file 
