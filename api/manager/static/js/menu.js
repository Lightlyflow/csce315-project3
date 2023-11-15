let selectedItem = null;
let lastSelectedIngredient = null;
let menuItemMode = null;
let ingredientMode = null;

let menuNameInput = null;
let menuPriceInput = null;
let menuCategoryInput = null;
let menuCalorieInput = null;
let menuInStockInput = null;

let ingredientNameInput = null;
let ingredientQuantityInput = null;

$(document).ready(async function() {
    // =================== Initialize Elements ===================
    menuItemTable = $("#menuItemTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    ingredientTable = $("#ingredientTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    menuNameInput = $('#menuItemNameInput')[0];
    menuPriceInput = $('#menuItemPriceInput')[0];
    menuCategoryInput = $('#menuItemCategoryInput')[0];
    menuCalorieInput = $('#menuItemCaloriesInput')[0];
    menuInStockInput = $('#menuItemStockInput')[0];

    ingredientNameInput = $('#ingredientNameInput')[0];
    ingredientQuantityInput = $('#ingredientQuantityInput')[0];

    // =================== Button/Table Functions ===================

    menuItemTable.on('click', 'tbody tr', async function() {
        selectedItem = menuItemTable.row(this).data();
        await refreshIngredients(selectedItem[3]);
    });

    ingredientTable.on('click', 'tbody tr', async function() {
        lastSelectedIngredient = ingredientTable.row(this).data();
    });

    $('.nav-tabs a').click(function() {
        $(this).tab('show');
    })

    $('#deleteMenuItem').click(async function() {
        let data = {};
        data['itemid'] = selectedItem[3];
        await delMenuItem(data);
        await refreshMenuItems();
    })

    $('#editMenuItem').click(function() {
        menuItemMode = "edit";
        $('#menuItemModalTitle')[0].innerText = "Edit Menu Item";

        menuNameInput.value = selectedItem[0];
        menuPriceInput.value = selectedItem[1];
        menuInStockInput.value = selectedItem[2];
        menuCategoryInput.value = selectedItem[4];
        menuCalorieInput.value = selectedItem[5];
    })

    $('#addMenuItem').click(function() {
        menuItemMode = "add";
        $('#menuItemModalTitle')[0].innerText = "Add Menu Item";
    })

    $('#deleteIngredient').click(async function() {
        let data = {};
        // await delIngredient({});
    })

    $('#editIngredient').click(function() {
        ingredientMode = "edit";
        $('#ingredientModalTitle')[0].innerText = 'Edit Ingredient';

        ingredientNameInput.value = lastSelectedIngredient[0];
        ingredientQuantityInput.value = lastSelectedIngredient[1];
    })

    $('#addIngredient').click(function() {
        ingredientMode = "add";
        $('#ingredientModalTitle')[0].innerText = 'Add Ingredient';
    })

    $('#menuModalSubmit').click(async function() {
        if (menuItemMode === "edit") {
            console.log("edit menu");
        } else if (menuItemMode === "add") {
            console.log("add menu");
        }
    })

    $('#ingredientModalSubmit').click(async function() {
        if (ingredientMode === "edit") {
            console.log("edit ingredient");

        } else if (ingredientMode === "add") {
            console.log("add ingredient");

        }
    })

    await refreshMenuItems();
    hideCols();
});

function hideCols() {
    menuItemTable.column(3).visible(false);
    ingredientTable.column(2).visible(false);
    ingredientTable.column(3).visible(false);
}

// =================== Fetch/Post data ===================

async function getMenuItems() {
    const resp = await fetch(`/manager/menu/menuitems`, { method: 'GET' });
    return resp.json();
}

async function getIngredients(itemID) {
    const resp = await fetch(`/manager/menu/ingredients?menuitemid=${itemID}`, { method: 'GET' });
    return resp.json();
}

async function addMenuItem(data) {
    const resp = await fetch(`/manager/menu/menuitems?method=ADD`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function delMenuItem(data) {
    const resp = await fetch(`/manager/menu/menuitems?method=DEL`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function updateMenuItem(data) {
    const resp = await fetch(`/manager/menu/menuitems?method=UPDATE`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function addIngredient(data) {
    const resp = await fetch(`/manager/menu/ingredients?method=ADD`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function delIngredient(data) {
    const resp = await fetch(`/manager/menu/ingredients?method=DEL`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function updateIngredient(data) {
    const resp = await fetch(`/manager/menu/ingredients?method=UPDATE`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

// =================== Call these ===================

async function refreshMenuItems() {
    menuItemTable.clear();
    let data = await getMenuItems();
    menuItemTable.rows.add(data).draw();
}

async function refreshIngredients(itemID) {
    ingredientTable.clear();
    let data = await getIngredients(itemID);
    ingredientTable.rows.add(data).draw();
}
