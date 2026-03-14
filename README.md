# Food Bank Inventory System

An inventory management multi-role system made for food banks to track supply with different user permissions based on job roles.

### Tech Stack
- Python | Core Logic (Current)
- Flask | API (Current)
- HTML/JS/CSS | (In Progress)
- C++ | Barcode Processing (Planned)
- SQL | Database (Current)
- Java | QR Code generation (Planned)

### Features
- Role-based access with 4 current roles (Viewer, scanner, stocker, & admin).
- Real time inventory tracking.
- Stock management with the ability to add/remove items.
- User authentication with SHA-256 hashing + salting.
- Audit trail for actions with timestamps.
- API for frontend integration.

### Planned Features
- QR Code scanning
- Nutritional value threshold system (Must meet a certain nutritional score).
- Demand prediction with pandas based on upcoming holidays or days of the week.


## How to run 

### CLI Version
1) Run the main.py file
2) Login for default account is admin for username & password
3) Roles for creating a new user is (Viewer, Stocker, Scanner, Admin)
   - Viewer can only view
   - Stocker can add and remove inventory
   - Scanner can only add
   - Admin has full permission

### Web Version
1) Install Flask: "pip install flask"
2) Run app.py
3) Go to "http://localhost:5000"
4) Default login is admin admin unless editted in CLI.

### Reset
- Delete inventory.db file to reset data.



