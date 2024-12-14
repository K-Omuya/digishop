// Hardcoded data for platforms and product prices
const platforms = [
    {
        platform: "Jumia",
        url: "https://jumia.com",
        price: "KSh 1,000",
        image: "assets/images/jumia_product.jpg", // Hardcoded image URL
    },
    {
        platform: "Kilimall",
        url: "https://kilimall.com",
        price: "KSh 1,200",
        image: "assets/images/kilimall_product.jpg", // Hardcoded image URL
    },
    {
        platform: "Copia",
        url: "https://copia.com",
        price: "KSh 1,150",
        image: "assets/images/copia_product.jpg", // Hardcoded image URL
    },
];

// Function to handle the search and display results
function searchProduct() {
    const searchQuery = document.getElementById("searchInput").value.trim().toLowerCase();

    if (!searchQuery) {
        alert("Please enter a product name.");
        return;
    }

    // Format the product name and map the hardcoded data to the results
    const results = platforms.map((p) => ({
        product: searchQuery.charAt(0).toUpperCase() + searchQuery.slice(1), // Capitalize first letter of search query
        platform: p.platform,
        price: p.price,
        link: p.url,
        image: p.image,
    }));

    const tableBody = document.querySelector("#priceTable tbody");
    tableBody.innerHTML = ""; // Clear previous results

    // Check if no results found, otherwise display results in the table
    if (results.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="5">No results found for "${searchQuery}"</td></tr>`;
        return;
    }

    results.forEach((result) => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td><img src="${result.image}" alt="${result.product}" class="product-image"></td>
            <td>${result.product}</td>
            <td>${result.platform}</td>
            <td>${result.price}</td>
            <td><a href="${result.link}" target="_blank">View</a></td>
        `;
        tableBody.appendChild(row);
    });
}
