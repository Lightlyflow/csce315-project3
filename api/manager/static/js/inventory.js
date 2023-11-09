$(document).ready(function () {
    // Data Tables
    $('#inventoryTable').DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'asc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });
    $('#lowStockTable').DataTable({
        "scrollY": "50vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'asc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });

    $('.dataTables_length').addClass('bs-select');

    // Buttons
    $("#orderSelected1").click(function() {
        console.log("orderSelected1");
    });

    $("#orderAll1").click(function() {
        console.log("orderAll1");
    });

    $("#updateThreshold1").click(function() {
        console.log("updateThreshold1");
    });

    $("#orderSelected2").click(function() {
        console.log("orderSelected2");
    });

    $("#orderAll2").click(function() {
        console.log("orderAll2");
    });

    $("#updateThreshold2").click(function() {
        console.log("updateThreshold2");
    });
});