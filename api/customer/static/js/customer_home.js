class MenuItem {
    constructor(name, iceLevel, sweetness, topping1, topping2, topping3, quantity) {
        this._name = name;
        this._iceLevel = iceLevel;
        this._sweetness = sweetness;
        this._topping1 = topping1;
        this._topping2 = topping2;
        this._topping3 = topping3;
        this._quantity = quantity;
    }

    get name() {
        return this._name;
    }
    get iceLevel() {
        return this._iceLevel;
    }
    get sweetness() {
        return this.sweetness;
    }
    get topping1() {
        return this._topping1;
    }
    get topping2() {
        return this._topping2;
    }
    get topping3() {
        return this._topping3;
    }
    get quantity() {
        return this._quantity;
    }
}

function toggleHeight(element) {
    element.classList.toggle("active");

    var menuDropDown = element.parentElement;

    if (menuDropDown && element !== menuDropDown) {
        menuDropDown.classList.toggle("active");
    }
}

function saveItem() {
    //Ice Options
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
                var iceLevel = "No";
            }
        }
    }

    //Toppings
    let toppingList = [];
    let toppingBoxes = document.getElementsByClassName('topping-col');
    for (let i = 0; i < toppingBoxes.length; i++) {
        let childElements = toppingBoxes[i].getElementsByClassName('topping-col-child');
        if (childElements[0].checked) {
            toppingList.push(childElements[1].innerHTML);
        }
    }
    let unpickedToppings = 3 - toppingList.length;
    for (let i = 0; i < unpickedToppings; i++) {
        toppingList.push("null");
    }

    //Item Name
    let menuItemName = document.getElementById("customizationName").innerHTML;

    //Sweetness Level
    let sweetnessLevel = document.getElementById('sweetnessLevel').value;

    //Quantity
    let quantity = document.getElementById('quantityPicker').value;

    //Local Storage List
    var savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems")) || [];
    var newItem = new MenuItem(menuItemName, iceLevel, sweetnessLevel, toppingList[0], toppingList[1], toppingList[2], quantity);
    savedMenuItems.push(newItem);
    localStorage.setItem("savedMenuItems", JSON.stringify(savedMenuItems));
}

function populateCart() {
    var savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems"));
    var pageCartItems = document.getElementById("pageCartItems");

    while (pageCartItems.firstChild) {
        pageCartItems.removeChild(pageCartItems.firstChild);
    }

    if (savedMenuItems && savedMenuItems.length > 0) {
        savedMenuItems.forEach(function(item) {
            var rowDiv = document.createElement("div");
            rowDiv.className = "row";
            pageCartItems.appendChild(rowDiv);

            var colDiv1 = document.createElement("div");
            colDiv1.className = "col";
            colDiv1.textContent = item._name;

            var colDiv2 = document.createElement("div");
            colDiv2.className = "col";
            colDiv2.textContent = item._iceLevel + " Ice";

            var colDiv3 = document.createElement("div");
            colDiv3.className = "col";
            colDiv3.textContent = item._sweetness;

            var colDiv4 = document.createElement("div");
            colDiv4.className = "col";
            let toppingList = [];
            toppingList.push(item._topping1);
            toppingList.push(item._topping2);
            toppingList.push(item._topping3);
            for (let i = 0; i < 3; i++) {
                if (toppingList[i] != "null") {
                    let toppingRow = document.createElement("div");
                    toppingRow.className = "row";
                    toppingRow.textContent = toppingList[i];
                    colDiv4.appendChild(toppingRow);
                }
            }

            var colDiv5 = document.createElement("div");
            colDiv5.className = "col";
            colDiv5.textContent = item._quantity;

            rowDiv.appendChild(colDiv1);
            rowDiv.appendChild(colDiv2);
            rowDiv.appendChild(colDiv3);
            rowDiv.appendChild(colDiv4);
            rowDiv.appendChild(colDiv5);
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
    var savedMenuItems = "";
    localStorage.setItem("savedMenuItems", JSON.stringify(savedMenuItems));
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

    document.getElementById("quantityPicker").value = 1;
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