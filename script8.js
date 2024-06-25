$(document).ready(function() {

    function displayPurchaseHistory(date, productName, quantity, totalPrice) {
        var newRow = $('<tr>');
        newRow.append('<td>' + date + '</td>');
        newRow.append('<td>' + productName + '</td>');
        newRow.append('<td>' + quantity + '</td>');
        newRow.append('<td>' + totalPrice + '</td>');
        $('#purchase-history').append(newRow);
    }

   
    function getPurchaseHistory() {
   
        var purchaseData = [
            { date: '1399/05/12', productName: 'کیک شکلاتی', quantity: 2, totalPrice: 60000 },
            { date: '1399/06/03', productName: 'کلوچه خرمایی', quantity: 1, totalPrice: 25000 }
        ];

        purchaseData.forEach(function(item) {
            displayPurchaseHistory(item.date, item.productName, item.quantity, item.totalPrice);
        });
    }

    
    getPurchaseHistory();
});

