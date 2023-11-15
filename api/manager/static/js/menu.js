let selectedItem = null;
let menuItemMode = null;
let ingredientMode = null;

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

    // =================== Button/Table Functions ===================

    menuItemTable.on('click', 'tbody tr', async function() {
        let menuItemID = menuItemTable.row(this).data()[3];
        await refreshIngredients(menuItemID);
    });

    $('.nav-tabs a').click(function() {
        $(this).tab('show');
    })

    $('#deleteMenuItem').click(async function() {
        await delMenuItem({});
    })

    $('#editMenuItem').click(function() {
        menuItemMode = "edit";
        $('#menuItemModalTitle')[0].innerText = "Edit Menu Item";
    })

    $('#addMenuItem').click(function() {
        menuItemMode = "add";
        $('#menuItemModalTitle')[0].innerText = "Add Menu Item";
    })

    $('#editIngredient').click(function() {
        ingredientMode = "edit";
        $('#ingredientModalTitle')[0].innerText = 'Edit Ingredient';
    })

    $('#addIngredient').click(function() {
        ingredientMode = "add";
        $('#ingredientModalTitle')[0].innerText = 'Add Ingredient';
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
