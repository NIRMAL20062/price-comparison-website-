document.getElementById("searchForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const productName = document.getElementById("product_name").value;
    fetch("/search", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `product_name=${encodeURIComponent(productName)}`,
    })
        .then((response) => response.json())
        .then((data) => {
            displayResults(data);
            updateChart(data);
        });
});

function displayResults(results) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = "";
    results.forEach((item) => {
        const itemDiv = document.createElement("div");
        itemDiv.textContent = `${item.title} - ${item.price} (${item.source})`;
        resultsDiv.appendChild(itemDiv);
    });
}

let chart;
function updateChart(results) {
    const ctx = document.getElementById("priceChart").getContext("2d");
    if (chart) {
        chart.destroy();
    }
    chart = new Chart(ctx, {
        type: "bar",
        data: {
            labels: results.map((item) => item.source),
            datasets: [
                {
                    label: "Price",
                    data: results.map((item) => item.price),
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1,
                },
            ],
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                },
            },
        },
    });
}