
var dataFromPython = {
    labels: ["A", "B", "C", "D", "E"],
    datasets: [{
        label: "ML Scores",
        data: [80, 60, 75, 90, 85],
        backgroundColor: 'rgba(75, 192, 75, 0.2)',
        borderColor: 'rgba(75, 192, 75, 1)',
        borderWidth: 1
    }]
};

var ctx = document.getElementById('ml-scores').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: dataFromPython,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Verileri güncellemek için bu fonksiyonu kullanabilirsiniz.
// function updateChart(newData) {
//     chart.data = newData;
//     chart.update();
// }

// Örnek olarak her 2 saniyede bir veriyi güncelleyin:
// setInterval(function () {
//     // Yeni verileri alın, örneğin WebSocket veya HTTP ile Python'dan alın.
//     // updateChart(newData); // Yeni verileri kullanarak grafik nesnesini güncelle
// }, 2000);

var eventSource = new EventSource('/api_serial');

eventSource.onmessage = function (event) {
    var newData = JSON.parse(event.data); // SSE aracılığıyla gelen veriyi ayrıştırın
    updateChart(newData); // Grafik nesnesini güncelleyin
};

// Verileri güncellemek için bu fonksiyonu kullanabilirsiniz
function updateChart(newData) {
    console.log(newData);
    chart.data.datasets[0].data = newData.data; // Verileri güncelle
    chart.update(); // Grafik nesnesini güncelle
}
