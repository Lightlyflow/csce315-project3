//Input forms
let usageDate1 = null;
let usageDate2 = null;
let pairDate1 = null;
let pairDate2 = null;
let salesDate1 = null;
let salesDate2 = null;

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

    salesHistoryTable = $('#salesHistoryTable').DataTable({
        "scrollY": "65vh",
        "scrollCollapse": true,
        select: true,
        order: [[1, 'desc']],
        paging: false,
        dom: '<"dt_row"rif>t',
    });

    $('.dataTables_length').addClass('bs-select');

    usageDate1 = $('#usageDate1').get()[0];
    usageDate2 = $('#usageDate2').get()[0];
    pairDate1 = $('#pairDate1').get()[0];
    pairDate2 = $('#pairDate2').get()[0];
    salesDate1 = $('#salesDate1').get()[0];
    salesDate2 = $('#salesDate2').get()[0];


    // =================== Button/Table Functions ====================

    $('#updateUsage').click(async function() {
        let data = {};
        data['startDate'] = usageDate1.value;
        data['endDate'] = usageDate2.value;
        await refreshUsage(data);
    });

    $('#updatePair').click(async function() {
        let data = {};
        data['startDate'] = pairDate1.value;
        data['endDate'] = pairDate2.value;
        await refreshPair(data);
    });

    $('#updateSales').click(async function() {
        let data = {};
        data['startDate'] = salesDate1.value;
        data['endDate'] = salesDate2.value;
        await refreshSales(data);
    });


    // =================== Fetch/Post Data ======================

    async function updateUsagePeriod(data) {
        const resp = await fetch(`/manager/analytics/usage?method=UPDATE`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return resp.json();
    }

    async function updatePairPeriod(data) {
        const resp = await fetch(`/manager/analytics/pair?method=UPDATE`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return resp.json();
    }

    async function updateSalesPeriod(data) {
        const resp = await fetch(`/manager/analytics/sales?method=UPDATE`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return resp.json();
    }


    // =================== Call These =====================
    
    async function refreshUsage(inputData) {
        productUsageTable.clear();
        let data = await updateUsagePeriod(inputData);
        productUsageTable.rows.add(data).draw();
    }

    async function refreshPair(inputData) {
        pairFrequencyTable.clear();
        let data = await updatePairPeriod(inputData);
        pairFrequencyTable.rows.add(data).draw();
    }

    async function refreshSales(inputData) {
        salesHistoryTable.clear();
        let data = await updateSalesPeriod(inputData);
        salesHistoryTable.rows.add(data).draw();
    }
});