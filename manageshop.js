document.getElementById('navbar-icon').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
});

document.getElementById('close-icon').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.remove('active');
});

var salesData = {
    'Product 1': [30, 20, 30, 30, 20, 30, 30, 50, 30, 40],
    'Product 2': [10, 40, 25, 35, 45, 50, 20, 30, 40, 20],
    'Product 3': [15, 30, 40, 45, 30, 25, 50, 35, 20, 10]
};

var productTitles = {
    'Product 1': 'فروش نوشیدنی گرم',
    'Product 2': 'فروش نوشیدنی سرد',
    'Product 3': 'فروش کیک'
};

var ctx = document.getElementById('salesChart').getContext('2d');
var salesChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['April 1', 'April 2', 'April 3', 'April 4', 'April 5', 'April 6', 'April 7', 'April 8', 'April 9', 'April 10'],
        datasets: [{
            data: salesData['Product 1'],
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: productTitles['Product 1'],
                font: {
                    size: 20
                }
            }
        }
    }
});

document.querySelectorAll('input[name="product"]').forEach((radio) => {
    radio.addEventListener('change', function() {
        var selectedProduct = this.value;
        salesChart.data.datasets[0].data = salesData[selectedProduct];
        salesChart.options.plugins.title.text = productTitles[selectedProduct];
        salesChart.update();
    });
});
