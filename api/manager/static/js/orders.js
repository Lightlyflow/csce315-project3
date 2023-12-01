let orderTable = null;
let orderTimeInterval = null;
let orderItemsTable = null;
let orderItemsLabel = null;

let startDateInput = null;
let endDateInput = null;

let lastSelected = null;

$(document).ready(async function() {
    orderTimeInterval = $("#orderTimeInterval")[0];
    orderItemsLabel = $("#orderItemsLabel")[0];

    startDateInput = $("#startDateInput")[0];
    endDateInput = $("#endDateInput")[0];

    orderTable = $("#orderTable").DataTable({
        "scrollY": "65vh",
        "scrollCollapse": false,
        select: true,
        order: [[0, 'desc']],
        dom: '<"dt_row"prif>t',
        paging: true,
    });

    orderItemsTable = $("#orderItemsTable").DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'desc']],
        dom: '<"dt_row"prif>t',
    });

    orderTable.on('click', 'tbody tr', async function() {
        selectedItem = orderTable.row(this).data();
        await refreshOrderParts(selectedItem[0]);
    });

    $("#orderModalSubmit").click(async function() {
        let startDate = new Date(startDateInput.value);
        let endDate = new Date(endDateInput.value);

        await refreshOrders(startDate.toISOString().split('T')[0], endDate.toISOString().split('T')[0]);
    });

    await initOrders();
});


// =================== Call these ===================
async function refreshOrders(startDate, endDate) {
    let endDatePlusDay = new Date(endDate);
    endDatePlusDay.setDate(endDatePlusDay.getDate() + 1);

    let data = {};
    data['startdate'] = startDate;
    data['enddate'] = endDatePlusDay.toLocaleDateString();

    orderTable.clear();
    let result = await getOrders(data);
    orderTable.rows.add(result).draw();
    orderTable.columns.adjust();

    orderTimeInterval.innerText = `(from ${startDate} to ${endDate})`;
}
async function initOrders() {
    let today = new Date();
    let prevWeek = new Date();

    prevWeek.setDate(today.getDate() - 7);

    await refreshOrders(prevWeek.toLocaleDateString(), today.toLocaleDateString());
    orderTimeInterval.innerText = "(for last 7 days)"
}
async function refreshOrderParts(orderID) {
    let data = {};
    data['orderid'] = orderID;

    orderItemsTable.clear();
    let result = await getOrderParts(data);
    orderItemsTable.rows.add(result).draw();

    orderItemsTable.columns.adjust();
    orderItemsLabel.innerText = `(for order ID: ${orderID})`
}

// =================== Fetch/Post data ===================
async function getOrders(data) {
    const resp = await fetch("/manager/orders/data", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}
async function getOrderParts(data) {
    const resp = await fetch("/manager/orders/parts", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}
