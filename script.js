// PantryPal - Basic JavaScript
// Stores inventory directly in a Dictionary / Object (No JSON used)

let inventory = {
    "Milk": { quantity: 1, price: 30 },
    "Rice": { quantity: 5, price: 50 },
    "Sugar": { quantity: 1, price: 40 },
    "Eggs": { quantity: 6, price: 6 }
};

let lowStockLimit = 2;

// Function to display items from dictionary in the table
function displayItems(dict) {
    let tableBody = document.getElementById("tableBody");
    tableBody.innerHTML = "";

    let totalStockValue = 0;
    let lowStockCount = 0;
    let itemCount = 0;

    // Loop through dictionary keys
    for (let name in dict) {
        itemCount = itemCount + 1;
        let item = dict[name];
        let itemTotal = item.quantity * item.price;
        totalStockValue = totalStockValue + itemTotal;

        // Check if low stock using conditional statement
        let status = "";
        let statusClass = "";
        if (item.quantity <= lowStockLimit) {
            status = "Low Stock!";
            statusClass = "low-stock";
            lowStockCount = lowStockCount + 1;
        } else {
            status = "In Stock";
            statusClass = "in-stock";
        }

        // Add table row
        let row = "<tr>" +
            "<td>" + name + "</td>" +
            "<td>" + item.quantity + "</td>" +
            "<td>Rs. " + item.price + "</td>" +
            "<td>Rs. " + itemTotal + "</td>" +
            "<td class='" + statusClass + "'>" + status + "</td>" +
            "<td>" +
                "<button onclick='updateItem(\"" + name + "\")'>Update</button>" +
                "<button style=\"background-color:red;\" onclick='deleteItem(\"" + name + "\")'>Delete</button>" +
            "</td>" +
        "</tr>";

        tableBody.innerHTML += row;
    }

    // Update summary counters
    document.getElementById("totalItems").innerText = itemCount;
    document.getElementById("totalValue").innerText = totalStockValue;
    document.getElementById("lowCount").innerText = lowStockCount;
}

// Function to add new item into dictionary (Create)
function addItem() {
    let name = document.getElementById("itemName").value.trim();
    let qty = document.getElementById("itemQty").value;
    let price = document.getElementById("itemPrice").value;

    if (name === "" || qty === "" || price === "") {
        alert("Please fill all fields!");
        return;
    }

    // Check if key already exists in dictionary
    if (name in inventory) {
        alert("Item already exists in dictionary! Use Update to change quantity.");
        return;
    }

    // Store in dictionary
    inventory[name] = {
        quantity: Number(qty),
        price: Number(price)
    };

    // Clear input fields
    document.getElementById("itemName").value = "";
    document.getElementById("itemQty").value = "";
    document.getElementById("itemPrice").value = "";

    displayItems(inventory);
}

// Function to update quantity in dictionary (Update)
function updateItem(name) {
    let newQty = prompt("Enter new quantity for " + name + ":", inventory[name].quantity);

    if (newQty !== null && newQty !== "") {
        let converted = Number(newQty);
        if (converted >= 0) {
            inventory[name].quantity = converted;
            displayItems(inventory);
        } else {
            alert("Quantity cannot be negative!");
        }
    }
}

// Function to delete item from dictionary (Delete)
function deleteItem(name) {
    let confirmDelete = confirm("Do you want to delete " + name + "?");
    if (confirmDelete) {
        delete inventory[name];
        displayItems(inventory);
    }
}

// Function to search item in dictionary
function searchItem() {
    let search = document.getElementById("searchName").value.trim().toLowerCase();
    let searchResults = {};

    for (let name in inventory) {
        if (name.toLowerCase().includes(search)) {
            searchResults[name] = inventory[name];
        }
    }

    displayItems(searchResults);
}

// Function to show only low stock items
function showLowStock() {
    let lowStockDict = {};

    for (let name in inventory) {
        if (inventory[name].quantity <= lowStockLimit) {
            lowStockDict[name] = inventory[name];
        }
    }

    displayItems(lowStockDict);
}

// Load dictionary items on page start
displayItems(inventory);
