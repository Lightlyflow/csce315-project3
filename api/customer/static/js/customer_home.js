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
    var iceOptions = document.getElementsByName("iceOptions");
    for (var i = 0; i < iceOptions.length; i++) {
        var currentOption = iceOptions[i];

        if (currentOption.checked) {
            var iceId = currentOption.getAttribute('id');
            if (iceId == "regularIce") {
                var iceLevel = "Regular";
            }
            else if (iceId == "lessIce") {
                var iceLevel = "Less";
            }
            else {
                var iceLevel = "None";
            }
        }
    }

    var savedItems = JSON.parse(localStorage.getItem("savedItems")) || [];
    var heldItem = JSON.parse(localStorage.getItem("heldItem"));
    var savedIces = JSON.parse(localStorage.getItem("savedIces")) || [];

    savedItems.push(heldItem);
    savedIces.push(iceLevel);

    localStorage.setItem("savedItems", JSON.stringify(savedItems));
    localStorage.setItem("savedIces", JSON.stringify(savedIces));
    alert(heldItem);
    alert(iceLevel);
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

//Resets modal to default values
function resetCustomization() {
    //Radio buttons for ice reset to regular, the default
    var ele = document.getElementsByName("iceOptions");
    for(var i = 0; i < ele.length; i++)
        ele[i].checked = false;
    ele[0].checked = true;

    //Slider for sweetness level reset to default value 50
    document.getElementById('sweetnessLevel').value = 100;

    //Reset of topping buttons
    toppings = document.querySelectorAll('input[name=toppingOptions]:checked');
    for (var i = 0; i < toppings.length; i++) {
        toppings[i].checked = false;
    }
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
function stopCheckTopping(element) {
    if (document.querySelectorAll('input[name=toppingOptions]:checked').length > 3) {
        element.checked = false;
    }
}

//Gets item name to populate customization modal
function setItemName(name) {
    document.getElementById("customizationName").innerHTML = name;
}