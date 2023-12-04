let timesheetTable = null;
let lastSelected = null;

let entryEmployeeInput = null;
let entryActivityInput = null;
let entryClockInInput = null;
let entryClockOutInput = null;

$(document).ready(async function() {
    entryEmployeeInput = $("#entryEmployeeInput")[0];
    entryActivityInput = $("#entryActivityInput")[0];
    entryClockInInput = $("#entryClockInInput")[0];
    entryClockOutInput = $("#entryClockOutInput")[0];

    timesheetTable = $("#timesheetTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    timesheetTable.on('click', 'tbody tr', async function() {
        selectedItem = timesheetTable.row(this).data();
    });

    $("#deleteEntry").click(async function() {});
    $("#updateEntry").click(async function() {});
    $("#addEntry").click(async function() {});

    $("#entryModalSubmit").click(async function() {});
})