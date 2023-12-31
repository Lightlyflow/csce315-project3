class MenuItem {
    constructor(name, iceLevel, sweetness, topping1, topping2, topping3, quantity, price) {
        this._name = name;
        this._iceLevel = iceLevel;
        this._sweetness = sweetness;
        this._topping1 = topping1;
        this._topping2 = topping2;
        this._topping3 = topping3;
        this._quantity = quantity;
        this._price = price;
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
    get price() {
        return this._price;
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
    //Quantity
    let quantity = document.getElementById('quantityPicker').value;
    if (quantity == "") {
        return;
    }


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

    //Price
    let price = parseFloat(document.getElementById("customizePrice").textContent.substring(1)) / parseInt(quantity);

    //Local Storage List
    var savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems")) || [];
    var newItem = new MenuItem(menuItemName, iceLevel, sweetnessLevel, toppingList[0], toppingList[1], toppingList[2], quantity, price);
    savedMenuItems.push(newItem);
    localStorage.setItem("savedMenuItems", JSON.stringify(savedMenuItems));

    localStorage.setItem("editedItem", JSON.stringify(""));
}

function populateCart() {
    var savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems"));
    var editedItem = JSON.parse(localStorage.getItem("editedItem")) || "";
    if (editedItem != "") {
        savedMenuItems.push(editedItem);
        localStorage.setItem("savedMenuItems", JSON.stringify(savedMenuItems));
        localStorage.setItem("editedItem", JSON.stringify(""));
    }
    var pageCartItems = document.getElementById("pageCartItems");

    while (pageCartItems.firstChild) {
        pageCartItems.removeChild(pageCartItems.firstChild);
    }

    if (savedMenuItems && savedMenuItems.length > 0) {
        //Add elements to page
        var colDiv;
        let i = 0;
        var orderTotal = 0.0;
        savedMenuItems.forEach(function(item) {
            var totalRowDiv = document.createElement("div");
            totalRowDiv.className = "row";
            pageCartItems.appendChild(totalRowDiv);
    
            var leftColDiv = document.createElement("div");
            leftColDiv.className = "col";
            totalRowDiv.appendChild(leftColDiv);

            var rowDiv1 = document.createElement("div");
            rowDiv1.className = "row firstCartEntry";
            colDiv = document.createElement("div");
            colDiv.className = "col menuItemCart";
            colDiv.textContent = item._name;
            rowDiv1.appendChild(colDiv);
            leftColDiv.appendChild(rowDiv1);

            var rowDiv2 = document.createElement("div");
            rowDiv2.className = "row";
            colDiv = document.createElement("div");
            colDiv.className = "col";
            colDiv.textContent = "Ice: " + item._iceLevel;
            rowDiv2.appendChild(colDiv);
            leftColDiv.appendChild(rowDiv2);

            var rowDiv3 = document.createElement("div");
            rowDiv3.className = "row";
            colDiv = document.createElement("div");
            colDiv.className = "col";
            colDiv.textContent = "Sweetness: " + item._sweetness + "%";
            rowDiv3.appendChild(colDiv);
            leftColDiv.appendChild(rowDiv3);

            let toppingList = [];
            toppingList.push(item._topping1);
            toppingList.push(item._topping2);
            toppingList.push(item._topping3);

            let toppingText = "Toppings: ";
            if (toppingList[0] == "null") {
                toppingText += "None";
            }
            else if (toppingList[1] == "null") {
                toppingText += toppingList[0];
            }
            else if (toppingList[2] == "null") {
                toppingText += toppingList[0] + ", " + toppingList[1];
            }
            else {
                toppingText += toppingList[0] + ", " + toppingList[1] + ", " + toppingList[2];
            }

            var rowDiv4 = document.createElement("div");
            rowDiv4.className = "row";
            colDiv = document.createElement("div");
            colDiv.className = "col";
            colDiv.textContent = toppingText;
            rowDiv4.appendChild(colDiv);
            leftColDiv.appendChild(rowDiv4);

            var rowDiv5 = document.createElement("div");
            rowDiv5.className = "row";
            colDiv = document.createElement("div");
            colDiv.className = "col";
            colDiv.textContent = "Quantity: " + item._quantity;
            rowDiv5.appendChild(colDiv);
            leftColDiv.appendChild(rowDiv5);

            var rowDiv6 = document.createElement("div");
            rowDiv6.className = "row finalCartEntry";
            colDiv = document.createElement("div");
            colDiv.className = "col";
            colDiv.textContent = "$" + (parseFloat(item._price) * parseFloat(item._quantity)).toFixed(2);
            orderTotal += parseFloat(item._price) * parseFloat(item._quantity)
            rowDiv6.appendChild(colDiv);
            leftColDiv.appendChild(rowDiv6);

            var rowDiv7 = document.createElement("div");
            rowDiv7.className = "row";
            let buttonDiv1 = document.createElement("button");
            buttonDiv1.className = "btn btn-primary";
            buttonDiv1.textContent = "Delete Item";
            buttonDiv1.setAttribute("onclick", "removeFromCart(" + i.toString() + ")")
            let colDiv1 = document.createElement("div");
            colDiv1.className = "col";
            let colDiv2 = document.createElement("div");
            colDiv2.className = "col";
            rowDiv7.appendChild(colDiv1);
            rowDiv7.appendChild(colDiv2);

            colDiv1.appendChild(buttonDiv1);

            let buttonDiv2 = document.createElement("button");
            buttonDiv2.className = "btn btn-primary";
            buttonDiv2.textContent = "Edit Item";
            buttonDiv2.setAttribute("onclick", "editFromCart(" + i.toString() + ")")
            buttonDiv2.setAttribute("data-bs-toggle", "modal");
            buttonDiv2.setAttribute("data-bs-target", "#customizationModal");
            colDiv2.appendChild(buttonDiv2);
            leftColDiv.appendChild(rowDiv7);

            i++;
        });
        document.getElementById("orderTotal").innerText = "Total: $" + (orderTotal).toFixed(2);
    }
    else {
        var rowDiv = document.createElement("div");
        rowDiv.className = "row";
        let colDiv = document.createElement("col");
        colDiv.className = "col";
        colDiv.textContent = "Your cart is empty.";
        rowDiv.appendChild(colDiv);
        pageCartItems.appendChild(rowDiv);
        document.getElementById("orderTotal").innerText = "Total: $0.00";
    }
    let line = document.createElement("hr");
    pageCartItems.appendChild(line);
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
    var toppings = document.querySelectorAll('input[name=toppingOptions]:checked');
    for (var i = 0; i < toppings.length; i++) {
        toppings[i].checked = false;
    }

    document.getElementById("quantityPicker").value = 1;

    //Price
    let customizePrice = document.getElementById("customizePrice");
    let savedItemPrice = parseFloat(localStorage.getItem("currentItemPrice"));
    customizePrice.textContent = "$" + savedItemPrice.toFixed(2);    
}

function sendSavedItemsToServer() {
    var savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems"));

    if (savedMenuItems && savedMenuItems.length > 0) {
        var data = { savedMenuItems: savedMenuItems };
        data.orderDate = "current";

        fetch('/employee/post_endpoint', {
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
function setItemName(name, price) {
    document.getElementById("customizationName").innerHTML = name;

    let currentItemPrice = localStorage.getItem("currentItemPrice") || 0;
    currentItemPrice = parseFloat(price)
    localStorage.setItem("currentItemPrice", currentItemPrice);
}

function setCustomizationPrice() {
    let toppingBoxes = document.getElementsByClassName('topping-col');
    let currentItemPrice = parseFloat(localStorage.getItem("currentItemPrice"));

    for (let i = 0; i < toppingBoxes.length; i++) {
        let childElements = toppingBoxes[i].getElementsByClassName('topping-col-child');
        if (childElements[0].checked) {
            currentItemPrice += parseFloat(childElements[1].id);
        }
    }
    let quantity = document.getElementById('quantityPicker').value;
    if (quantity != "1" && quantity != "2" && quantity != "3" && quantity != "4" && quantity != "5") {
        quantity = "1";
    }

    document.getElementById("customizePrice").textContent = "$" + (currentItemPrice * parseInt(quantity)).toFixed(2);
}

function removeFromCart(rowNum) {
    let savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems"));
    savedMenuItems.splice(rowNum, 1);
    localStorage.setItem("savedMenuItems", JSON.stringify(savedMenuItems));
    populateCart();
}

function editFromCart(rowNum) {
    let savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems"));
    let editedItem = savedMenuItems[rowNum];
    localStorage.setItem("editedItem", JSON.stringify(editedItem));
    savedMenuItems.splice(rowNum, 1);
    localStorage.setItem("savedMenuItems", JSON.stringify(savedMenuItems));


    document.getElementById("customizationName").innerHTML = editedItem._name;
    //Radio buttons for ice reset to regular, the default
    var ele = document.getElementsByName("iceOptions");
    for(var i = 0; i < ele.length; i++)
        ele[i].checked = false;
    if (editedItem._iceLevel == "Regular") {
        ele[0].checked = true;
    }
    else if (editedItem._iceLevel == "Less") {
        ele[1].checked = true;
    }
    else {
       ele[2].checked = true;
    }
    //Slider for sweetness level reset to default value 50
    document.getElementById('sweetnessLevel').value = editedItem._sweetness;

    //Reset of topping buttons
    var toppings = document.querySelectorAll('input[name=toppingOptions]:checked');
    for (let i = 0; i < toppings.length; i++) {
        toppings[i].checked = false;
    }
    let newPrice = parseFloat(editedItem._price);
    toppings = document.querySelectorAll('input[name=toppingOptions]')
    for (let i = 0; i < toppings.length; i++) {
        if (toppings[i].getAttribute("id") == editedItem._topping1) {
            toppings[i].checked = true;
            newPrice -= parseFloat(toppings[i].getAttribute("price"));
        }
        if (toppings[i].getAttribute("id") == editedItem._topping2) {
            toppings[i].checked = true;
            newPrice -= parseFloat(toppings[i].getAttribute("price"));
        }
        if (toppings[i].getAttribute("id") == editedItem._topping3) {
            toppings[i].checked = true;
            newPrice -= parseFloat(toppings[i].getAttribute("price"));
        }
    }

    document.getElementById("quantityPicker").value = editedItem._quantity;

    localStorage.setItem("currentItemPrice", JSON.stringify(newPrice));

    setCustomizationPrice();
}

function scaleText(pixelIncrement){
    currentSize = parseFloat(window.getComputedStyle(document.documentElement).fontSize);
    document.documentElement.style.fontSize = (currentSize + pixelIncrement) + 'px';
}


// create clock 
function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';

    hours = hours % 12 || 12;

    var timeString = (hours < 10 ? '' : '') + hours + ':' + (minutes < 10 ? '0' : '') + minutes + ' ' + ampm;

    document.getElementById('clock').innerHTML = timeString;
}
window.onload = function() {
    updateClock();
}
setInterval(updateClock, 1000);



var isExpanded = true;
 function minimizeButton(event) {
    event.target.classList.toggle("active");
    var checkout = document.getElementById('checkout');
    var menuItemsContainer = document.getElementById('menuItemsContainer');

    if (isExpanded) {
        checkout.style.display = 'none'; 
        menuItemsContainer.style.width = '100%'; 
        isExpanded = false; 
    } else {
        checkout.style.display = 'flex';
        menuItemsContainer.style.width = '70%'; 

        isExpanded = true; 
    }
}