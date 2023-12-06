let orderTable = null;
let orderItemsTable = null;
let deleteBtn = null;

$(document).ready(async function() {
    orderTable = $("#orderTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
        order: [[2, 'asc']]
    });
    orderItemsTable = $("#orderItemsTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    orderTable.on('click', 'tbody tr', async function() {
        selectedItem = orderTable.row(this).data();
        await refreshOrderParts(selectedItem[0]);
    });

    $("#prepareBtn").click(async function() {
        let data = {
            'orderid': selectedItem[0],
            'status': "preparing"
        };

        await markOrder(data);
        await refreshOrders();
    });

    $("#fulfillBtn").click(async function() {
        let data = {
            'orderid': selectedItem[0],
            'status': "fulfilled"
        };

        await markOrder(data);
        await refreshOrders();
        clearOrderParts();
    });

    $("#deleteBtn").click(async function() {
        let data = {
            'orderid': selectedItem[0],
        };

        await deleteOrder(data);
        await refreshOrders();
        clearOrderParts();
    });

    await refreshOrders();
})

async function getOrders() {
    const resp = await fetch("/employee/orders/data", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify("")
    });
    return resp.json();
}
async function getOrderParts(data){
    const resp = await fetch("/employee/orders/parts", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}
async function markOrder(data) {
    const resp = await fetch("/employee/orders/mark", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function deleteOrder(data) {
    const resp = await fetch("/employee/orders/delete", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}


async function refreshOrders() {
    orderTable.clear();
    let result = await getOrders();
    orderTable.rows.add(result).draw();
    orderTable.columns.adjust();
}
async function refreshOrderParts() {
    let data = {
        'orderid': selectedItem[0]
    };

    orderItemsTable.clear();
    let result = await getOrderParts(data);
    orderItemsTable.rows.add(result).draw();
    orderItemsTable.columns.adjust();
}
function clearOrderParts() {
    orderItemsTable.clear().draw();
}