//Input forms
let usageDate1 = null;
let usageDate2 = null;

$(document).ready(function () {
    // ====================== Initializing Elements ========================
    productUsageTable = $('#productUsageTable').DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[1, 'desc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });

    pairFrequencyTable = $('#pairFrequencyTable').DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[2, 'desc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });

    $('.dataTables_length').addClass('bs-select');

    usageDate1 = $('#usageDate1').get()[0];
    usageDate2 = $('#usageDate2').get()[0];


    // =================== Button/Table Functions ====================

    $('#updateUsage').click(async function() {
        let data = {};
        data['startDate'] = usageDate1.value;
        data['endDate'] = usageDate2.value;
        await updateUsage(data);
        await refreshUsage();
    });


    // =================== Fetch/Post Data ======================

    async function getUsageReport() {
        const resp = await fetch(`/manager/analytics/usage`, { method: 'GET' });
        return resp.json();
    }

    async function updateUsage(data) {
        const resp = await fetch(`/manager/analytics/usage?method=UPDATE`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
    }


    // =================== Call These =====================
    
    async function refreshUsage() {
        productUsageTable.clear();
        let data = await getUsageReport();
        productUsageTable.rows.add(data).draw();
    }
});