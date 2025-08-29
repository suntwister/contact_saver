#  Contact Saver Project

This is a Python project to collect and store participant details (Name, Age, Phone, Track) into a CSV file.  
The program validates user inputs, prevents duplicate phone numbers, and allows multiple participants to be registered.  

---

##  Features
- Save participant details into a CSV file
- Input validation:
  - Name must contain only letters and spaces
  - Age must be a positive number
  - Phone number must be exactly 11 digits
- Prevents duplicate phone numbers
- Displays all registered participants

---

##  Project Structure

│── participant_pkg/
│── main.py # Entry point, collects user input
│ ├── file_ops.py # Handles saving and loading participants
│ ├── contacts.csv # Stores participant records
│── README.md # Project documentation

## Contributors
- @cheryvmak – main.py
- @Meritus3266 – contacts.csv
- @Meritus3266 - file_ops.py
- @suntwister – GitHub Master (merging and repo management)
