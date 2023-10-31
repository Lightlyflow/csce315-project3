$(document).ready(function () {
    $('#inventoryTable').DataTable({
        "scrollY": "75vh",
        "scrollCollapse": true,
        select: true,
        order: [[0, 'asc']],
        paging: false,
    });
    $('.dataTables_length').addClass('bs-select');
});