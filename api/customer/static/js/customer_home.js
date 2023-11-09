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

function resetCustomization() {
    //Radio buttons for ice reset to regular, the default
    var ele = document.getElementsByName("iceOptions");
    for(var i = 0; i < ele.length; i++)
        ele[i].checked = false;
    ele[0].checked = true;

    //Slider for sweetness level reset to default value 50
    document.getElementById('sweetnessLevel').value = 50;

    //TO DO: reset of topping buttons
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

//Checks if 3 toppings are selected to limit topping boxes
function stopCheckIf(element) {
    if (document.querySelectorAll('input[name=toppingOptions]:checked').length > 3) {
        element.checked = false;
    }
}