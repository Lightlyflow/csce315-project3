$(document).ready(async function() {
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

    menuItemTable.on('click', 'tbody tr', async function() {
        let menuItemID = menuItemTable.row(this).data()[3];
        await refreshIngredients(menuItemID);
    });

    $('.nav-tabs a').click(function() {
        $(this).tab('show');
    })

    await refreshMenuItems();
    hideCols();
});

function hideCols() {
    menuItemTable.column(3).visible(false);
}

async function getMenuItems() {
    const resp = await fetch(`/manager/menu/menuitems`, { method: 'GET' });
    return resp.json();
}

async function getIngredients(itemID) {
    const resp = await fetch(`/manager/menu/ingredients?menuitemid=${itemID}`, { method: 'GET' });
    return resp.json();
}

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
