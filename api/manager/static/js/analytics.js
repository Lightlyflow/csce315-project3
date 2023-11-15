$(document).ready(function () {
    // Data Tables
    pairFrequencyTable = $('#pairReportTable').DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[2, 'desc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });

    $('.dataTables_length').addClass('bs-select');
});