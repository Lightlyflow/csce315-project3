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
    // scroll to clicked category
    element.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
    let price = parseFloat(document.getElementById("customizePrice").textContent) / parseInt(quantity);

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
        savedMenuItems.forEach(function(item) {
            var totalRowDiv = document.createElement("div");
            totalRowDiv.className = "row";
            pageCartItems.appendChild(totalRowDiv);
    
            var leftColDiv = document.createElement("div");
            leftColDiv.className = "col";
            totalRowDiv.appendChild(leftColDiv);
    
            var rightColDiv = document.createElement("div");
            rightColDiv.className = "col";
            totalRowDiv.appendChild(rightColDiv);

            var rowDiv1 = document.createElement("div");
            rowDiv1.className = "row";
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
            rowDiv6.className = "row";
            colDiv = document.createElement("div");
            colDiv.className = "col finalCartEntry";
            colDiv.textContent = "$" + (parseFloat(item._price) * parseFloat(item._quantity)).toFixed(2);
            rowDiv6.appendChild(colDiv);
            leftColDiv.appendChild(rowDiv6);

            var rowDiv7 = document.createElement("div");
            rowDiv7.className = "row";
            let buttonDiv1 = document.createElement("button");
            buttonDiv1.className = "btn btn-primary";
            buttonDiv1.textContent = "Delete Item";
            buttonDiv1.setAttribute("onclick", "removeFromCart(" + i.toString() + ")")
            rowDiv7.appendChild(buttonDiv1);
            rightColDiv.appendChild(rowDiv7);

            var rowDiv8 = document.createElement("div");
            rowDiv8.className = "row";
            let buttonDiv2 = document.createElement("button");
            buttonDiv2.className = "btn btn-primary";
            buttonDiv2.textContent = "Edit Item";
            buttonDiv2.setAttribute("onclick", "editFromCart(" + i.toString() + ")")
            buttonDiv2.setAttribute("data-bs-toggle", "modal");
            buttonDiv2.setAttribute("data-bs-target", "#customizationModal");
            rowDiv8.appendChild(buttonDiv2);
            rightColDiv.appendChild(rowDiv8);
            //data-bs-toggle="modal" data-bs-target="#customizationModal"

            i++;
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
    var toppings = document.querySelectorAll('input[name=toppingOptions]:checked');
    for (var i = 0; i < toppings.length; i++) {
        toppings[i].checked = false;
    }

    document.getElementById("quantityPicker").value = 1;

    //Price
    let customizePrice = document.getElementById("customizePrice");
    let savedItemPrice = parseFloat(localStorage.getItem("currentItemPrice"));
    customizePrice.textContent = savedItemPrice.toFixed(2);    


}

function sendSavedItemsToServer() {
    var savedMenuItems = JSON.parse(localStorage.getItem("savedMenuItems"));

    if (savedMenuItems && savedMenuItems.length > 0) {
        var data = { savedMenuItems: savedMenuItems };

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

    document.getElementById("customizePrice").textContent = (currentItemPrice * parseInt(quantity)).toFixed(2);
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
    toppings = document.querySelectorAll('input[name=toppingOptions]')
    for (let i = 0; i < toppings.length; i++) {
        if (toppings[i].getAttribute("id") == editedItem._topping1) {
            toppings[i].checked = true;
        }
    }

    document.getElementById("quantityPicker").value = editedItem._quantity;

    localStorage.setItem("currentItemPrice", editedItem._price);

    setCustomizationPrice();
}