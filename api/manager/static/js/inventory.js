$(document).ready(function () {
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
        refreshLowTable();
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
        console.log("updateThreshold2");
        refreshAllTable();
    });
});


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