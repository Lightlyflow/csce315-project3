$(document).ready(function () {
    $('#inventoryTable').DataTable({
        "scrollY": "80vh",
        "scrollCollapse": true,
        order: [[0, 'asc']],
    });
    $('.dataTables_length').addClass('bs-select');
});