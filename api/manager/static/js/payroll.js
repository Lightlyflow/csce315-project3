// Timesheet vars
let timesheetTable = null;
let lastSelected = null;

let entryModalTitle = null;

let entryEmployeeInput = null;
let entryActivityInput = null;
let entryClockInInput = null;
let entryClockOutInput = null;

let modalMode = null;

// Payment Vars
let paymentTable = null;

let billingPeriodSelect = null;
let employeeSelect = null;

$(document).ready(async function() {
    entryModalTitle = $("#entryModalTitle")[0];

    entryEmployeeInput = $("#entryEmployeeInput")[0];
    entryActivityInput = $("#entryActivityInput")[0];
    entryClockInInput = $("#entryClockInInput")[0];
    entryClockOutInput = $("#entryClockOutInput")[0];

    billingPeriodSelect = $("#billingPeriodSelect")[0];
    employeeSelect = $("#employeeSelect")[0];

    timesheetTable = $("#timesheetTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    timesheetTable.on('click', 'tbody tr', async function() {
        lastSelected = timesheetTable.row(this).data();
    });

    paymentTable = $("#paymentTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    $("#deleteEntry").click(async function() {
        if (lastSelected == null) { return }

        let data = {};
        data['entryid'] = lastSelected[0];

        if (confirm(`Delete entry for employee ID ${lastSelected[1]}?`)) {
            await deleteEntry(data);
            await refreshTimesheet();
        }
    });
    $("#updateEntry").click(async function() {
        entryModalTitle.innerText = "Edit Entry";
        modalMode = "update";

        entryEmployeeInput.value = lastSelected[1];
        entryActivityInput.value = lastSelected[2];
        entryClockInInput.value = lastSelected[3];
        entryClockOutInput.value = lastSelected[4];
    });
    $("#addEntry").click(async function() {
        entryModalTitle.innerText = "Add Entry";
        modalMode = "add";
        clearTimesheetModal();
    });

    $("#entryModalSubmit").click(async function() {
        let data = {};
        data['employeeid'] = entryEmployeeInput.value;
        data['activity'] = entryActivityInput.value;
        data['clockin'] = entryClockInInput.value;
        data['clockout'] = entryClockOutInput.value;

        if (modalMode === "add") {
            await addEntry(data);
            await refreshTimesheet();
        } else if (modalMode === "update") {
            if (lastSelected == null) { return }

            data['entryid'] = lastSelected[0];

            await updateEntry(data);
            await refreshTimesheet();
        }
    });

    billingPeriodSelect.onchange = async function() {
        await refreshEmployeeTimesheet();
    };
    employeeSelect.onchange = async function() {
        await refreshEmployeeTimesheet();
    }

    $("#paymentBtn").click(async function() {
        let data = {
            'employeeid': employeeSelect.value,
            'billingperiod': billingPeriodSelect.value
        };

        console.log(data);
    });

    await refreshTimesheet();
})


// =================== Fetch/Post data ===================
async function getTimesheet() {
    const resp = await fetch(`/manager/payroll/timesheet`, { method: 'GET' });
    return resp.json();
}
async function getEmployeeTimesheet(data) {
    const resp = await fetch(`/manager/payroll/timesheet`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}
async function addEntry(data) {
    const resp = await fetch(`/manager/payroll/add`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function updateEntry(data) {
    const resp = await fetch(`/manager/payroll/update`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function deleteEntry(data) {
    const resp = await fetch(`/manager/payroll/delete`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

// =================== Call these ===================
async function refreshTimesheet() {
    timesheetTable.clear();
    let data = await getTimesheet();
    timesheetTable.rows.add(data).draw();
    timesheetTable.columns.adjust().draw();
}
async function refreshEmployeeTimesheet() {
    if (employeeSelect.value === "" || billingPeriodSelect.value === "") {
        console.log("skipping");
        return;
    }

    let data = {
        'employeeid': employeeSelect.value,
        'billingperiod': billingPeriodSelect.value
    };

    paymentTable.clear();
    let result = await getEmployeeTimesheet(data);
    paymentTable.rows.add(result).draw();
    paymentTable.columns.adjust().draw();
}
function clearTimesheetModal() {
    entryEmployeeInput.value = "";
    entryActivityInput.value = "";
    entryClockInInput.value = "";
    entryClockOutInput.value = "";
}