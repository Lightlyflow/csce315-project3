let userTable = null;
let employeeTable = null;

$(document).ready(async function() {
    userTable = $("#userTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    employeeTable = $("#employeeTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    $('.nav-tabs a').click(function() {
        $(this).tab('show');
    });

    await refreshEmployees();
    await refreshUsers();
});

// =================== Fetch/Post data ===================
async function getUsers() {
    const resp = await fetch(`/manager/user_management/users`, { method: 'GET' });
    return resp.json();
}
async function getEmployees() {
    const resp = await fetch(`/manager/user_management/employees`, { method: 'GET' });
    return resp.json();
}

// =================== Call these ===================
async function refreshUsers() {
    userTable.clear();
    let data = await getUsers();
    userTable.rows.add(data).draw();
}
async function refreshEmployees() {
    employeeTable.clear();
    let data = await getEmployees();
    employeeTable.rows.add(data).draw();
}
