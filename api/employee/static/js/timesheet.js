let currentUser = null;

$(document).ready(async function() {
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

    currentUser = document.getElementById("currentUser").innerHTML;
    let user = {};
    user['employeeid'] = currentUser;

    // =================== Button/Table Functions =====================

    $('#clockInButton').click(async function() {
        let data = {}
        data['employeeid'] = currentUser;
        data['activity'] = "Front";
        await clockIn(data);
        await refreshWeek1Table(data);
    });

    $('#clockOutButton').click(async function() {
        let data = {}
        data['employeeid'] = currentUser;
        await clockOut(data);
        await refreshWeek1Table(data);
    });

    refreshWeek1Table(user);
    refreshWeek2Table(user);
});

// ===================== Fetch/Post Data =====================

async function getWeek1Table(data) {
    const resp = await fetch(`/employee/timesheet/week1`, { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}

async function getWeek2Table(data) {
    const resp = await fetch(`/employee/timesheet/week2`, { 
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)});
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

async function refreshWeek1Table(user) {
    week1Table.clear();
    let data = await getWeek1Table(user);
    week1Table.rows.add(data).draw();
}

async function refreshWeek2Table(user) {
    week2Table.clear();
    let data = await getWeek2Table(user);
    week2Table.rows.add(data).draw();
}