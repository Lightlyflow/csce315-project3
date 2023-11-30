let orderTable = null;

$(document).ready(async function() {
    orderTable = $("#orderTable").DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'desc']],
        dom: '<"dt_row"rif>t',
    });

    await initOrders();
});


// =================== Call these ===================
async function refreshOrders(startDate, endDate) {
    let endDatePlusDay = new Date(endDate);
    endDatePlusDay.setDate(endDatePlusDay.getDate() + 1);

    let data = {};
    data['startdate'] = startDate;
    data['enddate'] = endDate;

    orderTable.clear();
    console.log(data);
    let result = await getOrders(data);
    orderTable.rows.add(result).draw();
}
async function initOrders() {
    let today = new Date();
    let prevWeek = new Date();

    prevWeek.setDate(today.getDate() - 7);

    await refreshOrders(prevWeek.toLocaleDateString(), today.toLocaleDateString());
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