// noinspection JSJQueryEfficiency

let userTable = null;
let employeeTable = null;

let employeeModalTitle = null;
let employeeNameInput = null;
let employeeEmailInput = null;
let employeeManagerInput = null;
let employeeAdminInput = null;
let phoneNumberInput = null;
let altEmailInput = null;
let prefNameInput = null;
let addressInput = null;
let eContactInput = null;
let payRateInput = null;
let employeeModalSubmit = null;

let selectedItem = null;
let employeeMode = null;


$(document).ready(async function() {
    employeeModalTitle = $("#employeeModalTitle")[0];
    employeeNameInput = $("#employeeNameInput")[0];
    employeeEmailInput = $("#employeeEmailInput")[0];
    employeeManagerInput = $("#employeeManagerInput")[0];
    employeeAdminInput = $("#employeeAdminInput")[0];
    employeeModalSubmit = $("#employeeModalSubmit")[0];
    phoneNumberInput = $('#phoneNumberInput')[0];
    altEmailInput = $('#altEmailInput')[0];
    prefNameInput = $('#prefNameInput')[0];
    addressInput = $('#addressInput')[0];
    eContactInput = $('#eContactInput')[0];
    payRateInput = $('#payRateInput')[0];

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

    employeeTable.on('click', 'tbody tr', async function() {
        selectedItem = employeeTable.row(this).data();
    });

    $("#editEmployee").click(function() {
        employeeMode = "edit";

        employeeModalTitle.innerText = "Edit Employee";
        employeeModalSubmit.innerText = "Update";

        employeeNameInput.value = selectedItem[1];
        employeeManagerInput.checked = selectedItem[2];
        employeeAdminInput.checked = selectedItem[3];
        employeeEmailInput.value = selectedItem[4];
        phoneNumberInput.value = selectedItem[5];
        altEmailInput.value = selectedItem[6];
        prefNameInput.value = selectedItem[7];
        addressInput.value = selectedItem[8];
        eContactInput.value = selectedItem[9];
        payRateInput.value = selectedItem[10];
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

        let doDelete = confirm(`Delete employee ${selectedItem[1]}?`)

        if (doDelete) {
            await deleteEmployee(data);
            await refreshEmployees();
        }
    });

    $("#employeeModalSubmit").click(async function() {
        let data = {};

        if (employeeMode === "edit") {
            data['employeeid'] = selectedItem[0];
            data['name'] = employeeNameInput.value;
            data['ismanager'] = employeeManagerInput.checked;
            data['email'] = employeeEmailInput.value;
            data['phonenumber'] = phoneNumberInput.value;
            data['altemail'] = altEmailInput.value;
            data['prefname'] = prefNameInput.value;
            data['address'] = addressInput.value;
            data['econtact'] = eContactInput.value;
            data['payrate'] = payRateInput.value;
            data['isadmin'] = employeeAdminInput.checked;

            await updateEmployee(data);
            await refreshEmployees();
        } else if (employeeMode === "add") {
            data['name'] = employeeNameInput.value;
            data['ismanager'] = employeeManagerInput.checked;
            data['email'] = employeeEmailInput.value;
            data['phonenumber'] = phoneNumberInput.value;
            data['altemail'] = altEmailInput.value;
            data['prefname'] = prefNameInput.value;
            data['address'] = addressInput.value;
            data['econtact'] = eContactInput.value;
            data['payrate'] = payRateInput.value;
            data['isadmin'] = employeeAdminInput.checked;

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
