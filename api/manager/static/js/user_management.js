// noinspection JSJQueryEfficiency

let userTable = null;
let employeeTable = null;

let employeeModalTitle = null;
let employeeNameInput = null;
let employeeEmailInput = null;
let employeeManagerInput = null;
let employeeModalSubmit = null;

let selectedItem = null;
let employeeMode = null;


$(document).ready(async function() {
    employeeModalTitle = $("#employeeModalTitle")[0];
    employeeNameInput = $("#employeeNameInput")[0];
    employeeEmailInput = $("#employeeEmailInput")[0];
    employeeManagerInput = $("#employeeManagerInput")[0];
    employeeModalSubmit = $("#employeeModalSubmit")[0];

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

    employeeTable.on('click', 'tbody tr', async function() {
        selectedItem = employeeTable.row(this).data();
    });

    $("#editEmployee").click(function() {
        employeeMode = "edit";

        employeeModalTitle.innerText = "Edit Employee";
        employeeModalSubmit.innerText = "Update";

        employeeNameInput.value = selectedItem[1];
        employeeManagerInput.checked = selectedItem[2];
        employeeEmailInput.value = selectedItem[3];
    });

    $("#addEmployee").click(function() {
        employeeMode = "add";

        clearEmployeeModal();
        employeeModalTitle.innerText = "Add Employee";
        employeeModalSubmit.innerText = "Add";
    });

    $("#deleteEmployee").click(async function() {
        let data = {};

        data['employeeid'] = selectedItem[0];

        await deleteEmployee(data);
        await refreshEmployees();
    });

    $("#employeeModalSubmit").click(async function() {
        let data = {};

        if (employeeMode === "edit") {
            data['employeeid'] = selectedItem[0];
            data['name'] = employeeNameInput.value;
            data['ismanager'] = employeeManagerInput.checked;
            data['email'] = employeeEmailInput.value;

            await updateEmployee(data);
            await refreshEmployees();
        } else if (employeeMode === "add") {
            data['name'] = employeeNameInput.value;
            data['ismanager'] = employeeManagerInput.checked;
            data['email'] = employeeEmailInput.value;

            await addEmployee(data);
            await refreshEmployees();
        }
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
async function updateEmployee(data) {
    const resp = await fetch("/manager/user_management/employees/update", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function addEmployee(data) {
    const resp = await fetch("/manager/user_management/employees/add", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function deleteEmployee(data) {
    const resp = await fetch("/manager/user_management/employees/delete", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
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
function clearEmployeeModal() {
    employeeNameInput.value = "";
    employeeEmailInput.value = "";
    employeeManagerInput.checked = false;
}
