function toggleHeight(element) {
    element.classList.toggle("active");

    var menuDropDown = element.parentElement;

    if (menuDropDown && element !== menuDropDown) {
        menuDropDown.classList.toggle("active");
    }
}

function holdItem(item) {
    localStorage.setItem("heldItem", JSON.stringify(item));
}

function saveItem() {
    var savedItems = JSON.parse(localStorage.getItem("savedItems")) || [];
    var heldItem = JSON.parse(localStorage.getItem("heldItem"));
    savedItems.push(heldItem);
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

    //Resetting the customization menu after clicking add to cart
    //Topping dropdowns
    document.getElementById("topping1Dropdown").innerText = "Topping 1";
    document.getElementById("topping2Dropdown").innerText = "Topping 2";
    document.getElementById("topping3Dropdown").innerText = "Topping 3";

    //Radio buttons for ice
    var ele = document.getElementsByName("iceOptions");
    for(var i = 0; i < ele.length; i++)
        ele[i].checked = false;
    ele[0].checked = true;

    //Slider for sweetness level
    document.getElementById('sweetnessLevel').value = 50;
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

function dropdownFill(val, id) {
    var y = document.getElementById(id);
    var aNode = y.innerHTML = val + ' <span class="caret"></span>'; // Append 
}

function sendSavedItemsToServer() {
    var savedItems = JSON.parse(localStorage.getItem("savedItems"));

    if (savedItems && savedItems.length > 0) {
        var data = { savedItems: savedItems };

        fetch('/post_endpoint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        emptyCart();
    }
}