document.addEventListener('DOMContentLoaded', function() {
    const inventory = [
        { name: 'شکر', quantity: 0 },
        { name: 'آرد', quantity: 0 },
        { name: 'قهوه', quantity:0 },
        { name: 'شکلات', quantity: 0},
    ];

    const inventoryTable = document.getElementById('inventory-table').getElementsByTagName('tbody')[0];

    function updateTable() {
        inventoryTable.innerHTML = '';
        inventory.forEach((item, index) => {
            const row = inventoryTable.insertRow();
            row.innerHTML = `
                <td>${item.name}</td>
                <td>${item.quantity}</td>
                <td>
                    <button onclick="editItem(${index})">ویرایش</button>
                    <button onclick="deleteItem(${index})">حذف</button>
                </td>
            `;
        });
    }

    document.getElementById('add-item-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const newName = document.getElementById('new-item-name').value;
        const newQuantity = document.getElementById('new-item-quantity').value;
        inventory.push({ name: newName, quantity: parseInt(newQuantity) });
        updateTable();
        this.reset();
    });

    window.editItem = function(index) {
        const newName = prompt('Enter new name:', inventory[index].name);
        const newQuantity = prompt('Enter new quantity:', inventory[index].quantity);
        if (newName !== null && newQuantity !== null) {
            inventory[index].name = newName;
            inventory[index].quantity = parseInt(newQuantity);
            updateTable();
        }
    };

    window.deleteItem = function(index) {
        if (confirm('Are you sure you want to delete this item?')) {
            inventory.splice(index, 1);
            updateTable();
        }
    };

    updateTable();
});
