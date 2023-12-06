let employeeID = null;
let billingPeriodSelect = null;

$(document).ready(async function() {
    billingPeriodSelect = $("#billingPeriodSelect")[0];

    week1Table = $("#week1Table").DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'asc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });
    week2Table = $("#week2Table").DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'asc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });

    employeeID = document.getElementById("currentUser").dataset.id;

    billingPeriodSelect.onchange = async function() {
        await refreshTables();
    }

    // =================== Button/Table Functions =====================

    $('#clockInButton').click(async function() {
        let data = {};
        data['employeeid'] = employeeID;
        data['activity'] = "Front";
        await clockIn(data);
        await refreshTables();
    });

    $('#clockOutButton').click(async function() {
        let data = {};
        data['employeeid'] = employeeID;
        await clockOut(data);
        await refreshTables();
    });

    await refreshTables();
});

// ===================== Fetch/Post Data =====================

async function getWeekTable(data) {
    const resp = await fetch(`/employee/timesheet/week`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}

async function clockIn(data) {
    const resp = await fetch(`/employee/timesheet/clockIn`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function clockOut(data) {
    const resp = await fetch(`/employee/timesheet/clockOut`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

async function refreshWeek1Table() {
    let data = {
        'employeeid': employeeID,
        'billingperiod': billingPeriodSelect.value
    };

    week1Table.clear();
    let result = await getWeekTable(data);
    week1Table.rows.add(result).draw();
}

async function refreshWeek2Table() {
    let startDate = new Date(billingPeriodSelect.value);
    startDate.setDate(startDate.getDate() + 7);

    let data = {
        'employeeid': employeeID,
        'billingperiod': startDate.toISOString().split("T")[0]
    };

    week2Table.clear();
    let result = await getWeekTable(data);
    week2Table.rows.add(result).draw();
}

async function refreshTables() {
    await refreshWeek1Table();
    await refreshWeek2Table();
}

function scaleText(pixelIncrement){
    currentSize = parseFloat(window.getComputedStyle(document.documentElement).fontSize);
    document.documentElement.style.fontSize = (currentSize + pixelIncrement) + 'px';
}