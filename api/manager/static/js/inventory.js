let inventoryModalTitle = null;
let inventoryNameInput = null;
let inventoryQuantityInput = null;
let inventoryRestockInput = null;

let mode = null;

$(document).ready(function () {
    inventoryModalTitle = $("#inventoryModalTitle")[0];
    inventoryNameInput = $("#inventoryNameInput")[0];
    inventoryQuantityInput = $("#inventoryQuantityInput")[0];
    inventoryRestockInput = $("#inventoryRestockInput")[0];

    // Data Tables
    inventoryTable = $('#inventoryTable').DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'asc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });
    lowStockTable = $('#lowStockTable').DataTable({
        "scrollY": "50vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'asc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });

    $('.dataTables_length').addClass('bs-select');

    // Form
    textInput1 = $("#textInput1").get()[0];
    textInput2 = $("#textInput2").get()[0];

    // Buttons
    $("#orderSelected1").click(async function() {
        let amount = textInput1.value;
        let selected = $.map(lowStockTable.rows({ selected: true }).data(), function(item) { return item[1]; } )
        let data = {};
        data['amount'] = amount;
        data['items'] = selected;
        await orderSelected(data);
        await refreshLowTable();
    });

    $("#orderAll1").click(async function() {
        let amount = textInput1.value;
        let selected = $.map(lowStockTable.rows().data(), function(item) { return item[1]; } )
        let data = {};
        data['amount'] = amount;
        data['items'] = selected;
        await orderSelected(data);
        await refreshLowTable();
    });

    $("#updateThreshold1").click(async function() {
        console.log("updateThreshold1");
        let amount = textInput1.value;
        let selected = $.map(lowStockTable.rows({ selected: true }).data(), function(item) { return item[1]; } )
        let data = {};
        data['threshold'] = amount;
        data['names'] = selected;
        await updateThreshold(data);
        await refreshLowTable();
    });

    $("#orderSelected2").click(async function() {
        let amount = textInput2.value;
        let selected = $.map(inventoryTable.rows({ selected: true }).data(), function(item) { return item[1]; } )
        let data = {};
        data['amount'] = amount;
        data['items'] = selected;
        await orderSelected(data);
        await refreshAllTable();
    });

    $("#orderAll2").click(async function() {
        let amount = textInput2.value;
        let data = {};
        data['amount'] = amount;
        await orderAll(data);
        await refreshAllTable();
    });

    $("#updateThreshold2").click(async function() {
        let amount = textInput2.value;
        let selected = $.map(inventoryTable.rows({ selected: true }).data(), function(item) { return item[1]; } )
        let data = {};
        data['threshold'] = amount;
        data['names'] = selected;
        await updateThreshold(data);
        await refreshAllTable();
    });

    $("#addInventoryBtn").click(async function() {
        inventoryModalTitle.innerText = "Add Inventory Item";
        clearModal();

        mode = "add";
    });
    $("#updateInventoryBtn").click(async function() {
        inventoryModalTitle.innerText = "Update Inventory Item";
        let selectedRow = inventoryTable.rows({ selected: true }).data()[0];

        inventoryNameInput.value = selectedRow[1];
        inventoryQuantityInput.value = selectedRow[2];
        inventoryRestockInput.value = selectedRow[3];

        mode = "update";
    });
    $("#deleteInventoryBtn").click(async function() {
        let selectedRow = inventoryTable.rows({ selected: true }).data()[0];
        let inventoryID = selectedRow[0];

        let data = {};
        data['inventoryid'] = inventoryID;

        if (confirm(`Delete item ${selectedRow[1]}?`)) {
            await deleteInventoryItem(data);
            await refreshAllTable();
            await refreshAllTable();
        }
    });

    $("#inventoryModalSubmit").click(async function() {
        let data = {};
        let selectedRow = inventoryTable.rows({ selected: true }).data()[0];
        console.log("clicked");

        if (mode === "update") {
            data['inventoryid'] = selectedRow[0];
            data['name'] = inventoryNameInput.value;
            data['quantity'] = inventoryQuantityInput.value;
            data['restockthreshold'] = inventoryRestockInput.value;

            await updateInventoryItem(data);
            await refreshAllTable();
            await refreshAllTable();
            console.log("edit");
        } else if (mode === "add") {
            data['name'] = inventoryNameInput.value;
            data['quantity'] = inventoryQuantityInput.value;
            data['restockthreshold'] = inventoryRestockInput.value;

            await addInventoryItem(data);
            await refreshAllTable();
            await refreshAllTable();
            console.log("add");
        }
    });
});


async function updateThreshold(data) {
    const resp = await fetch(`/manager/inventory/threshold`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function orderAll(data) {
    const resp = await fetch(`/manager/inventory/orderall`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
     });
}

async function orderSelected(data) {
     const resp = await fetch(`/manager/inventory/order`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
     });
}


async function addInventoryItem(data) {
    const resp = await fetch(`/manager/inventory/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function updateInventoryItem(data) {
    const resp = await fetch(`/manager/inventory/update`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function deleteInventoryItem(data) {
    const resp = await fetch(`/manager/inventory/delete`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}


async function refreshAllTable() {
    inventoryTable.clear();
    let content = await getStock(false);
    inventoryTable.rows.add(content).draw();
}

async function refreshLowTable() {
    lowStockTable.clear();
    let content = await getStock(true);
    lowStockTable.rows.add(content).draw();
}

async function getStock(lowStock) {
    let resp;
    if (lowStock) {
        resp = await fetch(`/manager/inventory/stock?low=True`, {method: 'GET'});
    } else {
        resp = await fetch(`/manager/inventory/stock`, {method: 'GET'});
    }
    const content = await resp.json();
    return content;
}

function clearModal() {
    inventoryNameInput.value = ""
    inventoryQuantityInput.value = ""
    inventoryRestockInput.value = ""
}