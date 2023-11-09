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

    // Buttons
    $("#orderSelected1").click(function() {
        console.log("orderSelected1");
        refreshLowTable();
    });

    $("#orderAll1").click(function() {
        console.log("orderAll1");
        refreshLowTable();
    });

    $("#updateThreshold1").click(function() {
        console.log("updateThreshold1");
        refreshLowTable();
    });

    $("#orderSelected2").click(function() {
        console.log("orderSelected2");
        refreshAllTable();
    });

    $("#orderAll2").click(function() {
        console.log("orderAll2");
        refreshAllTable();
    });

    $("#updateThreshold2").click(function() {
        console.log("updateThreshold2");
        refreshAllTable();
    });

    $("#testbutton").click(async function() {
        refreshLowTable();
    });
});


async function refreshAllTable() {
    inventoryTable.clear().draw();
    let content = await getStock(false);
    inventoryTable.rows.add(content).draw();
}

async function refreshLowTable() {
    lowStockTable.clear().draw();
    let content = await getStock(false);
    lowStockTable.rows.add(content).draw();
}

async function getStock(lowStock) {
    const resp = await fetch(`/manager/inventory/stock?low=${lowStock}`, {method: 'GET'});
    const content = await resp.json();
    return content;
}