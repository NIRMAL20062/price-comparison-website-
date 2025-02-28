async function searchProduct() {
    const product = document.getElementById("product").value;
    if (!product) {
        alert("Please enter a product name");
        return;
    }

    // Fetch search results
    const response = await fetch(`http://127.0.0.1:5000/search?product=${product}`);
    const results = await response.json();
    displayResults(results);

    // Fetch price history
    const historyResponse = await fetch(`http://127.0.0.1:5000/price-history?product=${product}`);
    const history = await historyResponse.json();
    displayPriceHistory(history);
}

function displayResults(results) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = results.map(result => `
        <div>
            <strong>${result.Website}</strong>: ${result.Product} - ${result.Price}
        </div>
    `).join("");
}

function displayPriceHistory(history) {
    const ctx = document.getElementById("priceChart").getContext("2d");
    new Chart(ctx, {
        type: "line",
        data: {
            labels: history.map(h => h.Date),
            datasets: [{
                label: "Price History",
                data: history.map(h => h.Price),
                borderColor: "blue",
                fill: false
            }]
        }
    });
}