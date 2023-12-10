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
let paymentLabel = null;
let hoursText = null;
let payRateText = null;
let modalPayRateText= null;
let modalHoursText = null;
let modalTotalText = null;
let paymentModalTitle = null;

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
    paymentLabel = $("#paymentLabel")[0];
    hoursText = $("#hoursText")[0];
    payRateText = $("#payRateText")[0];
    modalPayRateText = $("#modalPayRateText")[0];
    modalHoursText = $("#modalHoursText")[0];
    modalTotalText = $("#modalTotalText")[0];
    paymentModalTitle = $("#paymentModalTitle")[0];

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

    $("#paymentModalSubmit").click(async function() {
        let data = {
            'employeeid': employeeSelect.value,
            'total': modalTotalText.innerText
        };
        let resp = await pay(data);

        if (resp === "Payment succeeded!") {
            addAlert("success", `Payment successful for ${employeeSelect.options[employeeSelect.selectedIndex].innerText}!`);
        } else {
            addAlert("danger", `Payment failed for ${employeeSelect.options[employeeSelect.selectedIndex].innerText}!`);
        }
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

async function getTotalHours(data) {
    const resp = await fetch(`/manager/payroll/hours`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}
async function getPayRate(data) {
    const resp = await fetch(`/manager/payroll/payrate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
}
async function pay(data) {
    const resp = await fetch(`/manager/payroll/pay`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return resp.json();
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
        return;
    }

    let week1 = new Date(billingPeriodSelect.value);
    let week2 = new Date(billingPeriodSelect.value);
    week2.setDate(week1.getDate() + 7)
    week1 = week1.toISOString().split('T')[0];
    week2 = week2.toISOString().split('T')[0];

    paymentLabel.innerText = `For weeks of ${week1} and ${week2}`;

    let data = {
        'employeeid': employeeSelect.value,
        'billingperiod': billingPeriodSelect.value
    };

    paymentTable.clear();
    let result = await getEmployeeTimesheet(data);
    paymentTable.rows.add(result).draw();
    paymentTable.columns.adjust().draw();

    let totalHours = await getTotalHours(data);
    hoursText.innerText = `${totalHours}`;
    let payRate = await getPayRate(data);
    payRateText.innerText = `${payRate}`;

    paymentModalTitle.innerText = `Pay Employee: ${employeeSelect.options[employeeSelect.selectedIndex].text}`;
    modalHoursText.innerText = `${totalHours}`;
    modalPayRateText.innerText = `${payRate}`;
    modalTotalText.innerText = `${totalHours[0] * payRate[0]}`;
}
function clearTimesheetModal() {
    entryEmployeeInput.value = "";
    entryActivityInput.value = "";
    entryClockInInput.value = "";
    entryClockOutInput.value = "";
}
function addAlert(alertType, text) {
    let alert = document.createElement('div');
    alert.className = `alert alert-${alertType}`;
    alert.role = "alert";
    alert.innerText = text;

    $("#alerts")[0].appendChild(alert);
}
