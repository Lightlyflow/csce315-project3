function toggleHeight(element) {
    element.classList.toggle("active");

    var menuDropDown = element.parentElement;

    if (menuDropDown && element !== menuDropDown) {
        menuDropDown.classList.toggle("active");
    }
}

function saveItem(item) {
    var savedItems = JSON.parse(localStorage.getItem("savedItems")) || [];
    savedItems.push(item);
    localStorage.setItem("savedItems", JSON.stringify(savedItems));
}

function populateCart() {
    var savedItems = JSON.parse(localStorage.getItem("savedItems"));
    var pageCartItems = document.getElementById("pageCartItems");

    while (pageCartItems.firstChild) {
        pageCartItems.removeChild(pageCartItems.firstChild);
    }

    if (savedItems && savedItems.length > 0) {
        savedItems.forEach(function(item) {
            var rowDiv = document.createElement("div");
            rowDiv.className = "row";
            rowDiv.textContent = item;
            pageCartItems.appendChild(rowDiv);
        });
    }
    else {
        var rowDiv = document.createElement("div");
        rowDiv.className = "row";
        rowDiv.textContent = "Your cart is empty.";
        pageCartItems.appendChild(rowDiv);
    }
}

function emptyCart() {
    var savedItems = JSON.parse(localStorage.getItem("savedItems")) || [];
    savedItems = "";
    localStorage.setItem("savedItems", JSON.stringify(savedItems));
    populateCart();
}

document.addEventListener("DOMContentLoaded", function() {
    populateCart();
});