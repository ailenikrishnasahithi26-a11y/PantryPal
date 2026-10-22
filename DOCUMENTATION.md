# PantryPal – Smart Home Inventory Tracker
## Complete Project Report & Detailed Code Documentation

---

### 1. Executive Summary
- **Project Name:** PantryPal – Smart Home Inventory Tracker
- **Domain:** Python Programming & Basic Web Development
- **Purpose:** To maintain records of household groceries and essential items, monitor stock levels, identify products that need restocking, calculate total inventory value, and perform CRUD operations.
- **Data Model:** In-memory storage using nested **Dictionaries** and persistent storage using a plain **Text File (`inventory.txt`)** with zero third-party libraries or JSON.

---

### 2. Core Concepts & How They Are Used

| Concept | Implementation in PantryPal | Code Example |
| :--- | :--- | :--- |
| **Functions** | Used to make code modular, reusable, and organized into individual tasks. | `def add_item():`, `def view_items():`, `def save_data():` |
| **Dictionaries** | Main storage structure. Keys represent the item name, and values are inner dictionaries holding `quantity` and `price`. | `inventory[name] = {"quantity": quantity, "price": price}` |
| **Lists** | Created dynamically when reading the text file using string splitting. | `parts = line.split(",")` -> `['Milk', '1', '30.0']` |
| **Conditional Statements** | `if`, `elif`, `else` evaluate menu choices, validate inputs, and detect low stock (`quantity <= 2`). | `if qty <= 2: status = "Low Stock!" else: status = "In Stock"` |
| **File Handling** | Reads from and writes to `inventory.txt` using Python's built-in `open()`, `.write()`, and `for line in file:`. | `file = open("inventory.txt", "w")` / `file = open("inventory.txt", "r")` |
| **CRUD Operations** | Complete lifecycle management: **C**reate (add), **R**ead (view/search), **U**pdate (change qty), **D**elete (remove). | `inventory[name] = {...}`, `del inventory[name]` |
| **Exception Handling** | Prevents program crashes when file is missing or user enters letters instead of numbers. | `try: int(input()) except ValueError:` and `except FileNotFoundError:` |

---

### 3. Detailed File-by-File Breakdown

#### File 1: `main.py` (Python Console Program)
- **Role:** The core backend application that runs inside the terminal.
- **Key Variables:**
  - `inventory = {}`: The master dictionary where keys are item names (e.g. `"Milk"`) and values are sub-dictionaries `{"quantity": 1, "price": 30.0}`.
- **Key Functions:**
  1. `load_data()`: Opens `inventory.txt` in read mode (`"r"`). Reads line-by-line, strips trailing whitespace, splits by comma (creating a list), and populates `inventory`. Wrapped in `try...except FileNotFoundError`.
  2. `save_data()`: Opens `inventory.txt` in write mode (`"w"`). Iterates over `inventory` keys and writes lines formatted as `Name,Quantity,Price\n`.
  3. `add_item()`: Asks for item name, quantity, and price. Checks if the item already exists in the dictionary (`if name in inventory:`). Validates numbers with `try...except ValueError`.
  4. `view_items()`: Iterates through each item in the dictionary. Calculates item status (`Low Stock!` if `quantity <= 2`, else `In Stock`).
  5. `update_quantity()`: Looks up an item by key (`if name in inventory:`), prompts for new quantity, updates the value, and calls `save_data()`.
  6. `delete_item()`: Deletes a key from the dictionary using Python's built-in `del inventory[name]` keyword.
  7. `search_item()`: Uses a `for` loop to check if the search keyword is a substring of the item name (`if search_name in name.lower():`).
  8. `show_low_stock()`: Filters and prints items whose quantity is less than or equal to 2 units.
  9. `show_total_value()`: Iterates through all items, multiplies `quantity * price`, and accumulates the sum into `total`.
  10. `main()`: Contains the `while True:` loop displaying the 1–8 numeric menu.

---

#### File 2: `inventory.txt` (Data Storage)
- **Role:** Plain text file storing data persistently across program restarts.
- **Format:** Comma-separated values:
  ```text
  Milk,1,30.0
  Rice,5,50.0
  Sugar,1,40.0
  Eggs,6,6.0
  ```

---

#### File 3: `index.html` (User Interface)
- **Role:** Web page structure for the visual interface.
- Summary cards, Add Item form inputs, Search & Filter controls, and standard HTML `<table>`.

---

#### File 4: `style.css` (Visual Styling)
- **Role:** Clean, readable visual design without external CSS frameworks.
- Clean container, button states, `.low-stock` red highlight, `.in-stock` green indicator.

---

#### File 5: `script.js` (Web Logic)
- **Role:** Client-side JavaScript using an in-memory dictionary/object:
  ```javascript
  let inventory = {
      "Milk": { quantity: 1, price: 30 },
      "Rice": { quantity: 5, price: 50 },
      "Sugar": { quantity: 1, price: 40 },
      "Eggs": { quantity: 6, price: 6 }
  };
  ```
- Functions for `displayItems()`, `addItem()`, `updateItem()`, `deleteItem()`, `searchItem()`, and `showLowStock()`.

---

### 4. Step-by-Step Execution Guide

#### Running the Python Terminal Program
```powershell
python main.py
```

#### Running the Web Application
Double-click `index.html` to open in any web browser.
