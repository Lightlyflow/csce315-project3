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
    let iceOptions = getElementsByName("iceOptions");
    for (let i = 0; i < iceOptions.length; i++) {
        if (iceOptions[i].contains(checked)) {
            var iceLevel = iceOptions[i].textContent;
        }
    }

    var savedItems = JSON.parse(localStorage.getItem("savedItems")) || [];
    var heldItem = JSON.parse(localStorage.getItem("heldItem"));
    var savedIces = JSON.parse(localStorage.getItem("savedIces")) || [];

    savedItems.push(heldItem);
    savedIces.push(iceLevel);

    localStorage.setItem("savedItems", JSON.stringify(savedItems));
    localStorage.setItem("savedIces", JSON.stringify(savedIces));
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

    resetCustomization(); //Resets modal
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

function resetCustomization() {
    //Resetting the customization menu after clicking add to cart
    //Topping dropdowns, reset to empty
    document.getElementById("topping1Dropdown").innerText = "Topping 1";
    document.getElementById("topping2Dropdown").innerText = "Topping 2";
    document.getElementById("topping3Dropdown").innerText = "Topping 3";

    //Radio buttons for ice reset to regular, the default
    var ele = document.getElementsByName("iceOptions");
    for(var i = 0; i < ele.length; i++)
        ele[i].checked = false;
    ele[0].checked = true;

    //Slider for sweetness level reset to default value 50
    document.getElementById('sweetnessLevel').value = 50;
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