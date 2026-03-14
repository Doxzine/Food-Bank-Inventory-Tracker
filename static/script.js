async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const response = await fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });
    const data = await response.json();
    if (data.message) {
        window.location.href = "/dashboard";
    } else {
        alert(data.error);
    }
}

function showSection(section) {
    document.getElementById("inventory").style.display = "none";
    document.getElementById("scanner").style.display = "none";
    document.getElementById("admin").style.display = "none";
    document.getElementById(section).style.display = "block";
    if (section === "inventory") {
        getTable();
    }
}

async function getTable() {
    const response = await fetch("/inventory");
    const data = await response.json();
    const table = document.getElementById("inventoryTable");
    
    // Clear old rows except header
    while (table.rows.length > 1) {
        table.deleteRow(1);
    }

    for (const item of data) {
        const row = table.insertRow();
        row.insertCell(0).textContent = item[0];
        row.insertCell(1).textContent = item[1];
        row.insertCell(2).textContent = item[2];
    }
}

async function addItem() {
    const itemName = document.getElementById("itemName").value;
    const quantity = document.getElementById("itemQuantity").value;
    const itemType = document.getElementById("itemType").value;
    const response = await fetch("/inventory", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name: itemName, quantity: quantity, type: itemType})
    });
    const data = await response.json();
    alert(data.message);
    getTable();
}

function logout() {
    window.location.href = "/logout";
}