let orderTable = null;

$(document).ready(async function() {
    orderTable = $("#orderTable").DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'desc']],
        dom: '<"dt_row"rif>t',
    })
});


// =================== Call these ===================
async function refreshOrders(startDate, endDate) {
    let data = {};
    data['startdate'] = startDate;
    data['enddate'] = endDate;

    orderTable.clear();
    let result = await getMenuItems(data);
    orderTable.rows.add(result).draw();
}

// =================== Fetch/Post data ===================
async function getOrders(data) {
    const resp = await fetch("/manager/orders/data", {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}