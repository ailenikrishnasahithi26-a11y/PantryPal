# PantryPal - Simple Home Inventory Tracker

A simple household inventory tracker using **dictionaries** and plain **text file handling** (No JSON used).

---

## 💡 How Key Concepts Are Used

- **Dictionaries**: 
  - The inventory is stored as a dictionary:
    ```python
    inventory = {
        "Milk": {"quantity": 1, "price": 30.0},
        "Rice": {"quantity": 5, "price": 50.0}
    }
    ```
- **File Handling**: 
  - Reads and writes to a standard text file (`inventory.txt`) using `open()` without any JSON library.
- **Lists**: 
  - Created when splitting lines from the text file: `parts = line.split(",")`.
- **Functions**: 
  - `load_data()`, `save_data()`, `add_item()`, `view_items()`, `update_quantity()`, `delete_item()`, `search_item()`, `show_low_stock()`, `show_total_value()`.
- **Conditional Statements**: 
  - `if`, `elif`, `else` for menu choices, checking low stock (`qty <= 2`), and checking if an item exists (`if name in inventory:`).
- **CRUD Operations**: 
  - **Create**: `inventory[name] = {...}`
  - **Read**: `for name in inventory:`
  - **Update**: `inventory[name]["quantity"] = new_qty`
  - **Delete**: `del inventory[name]`
- **Exception Handling**: 
  - `try...except FileNotFoundError` when opening files, and `try...except ValueError` when entering numbers.

---

## 🚀 How to Run

1. **Web Version**:
   - Double-click `index.html` to open it directly in your browser.
2. **Python Version**:
   - Open terminal and run:
     ```bash
     python main.py
     ```
