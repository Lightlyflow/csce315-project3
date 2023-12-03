let imageTable = null;

$(document).ready(async function() {
    imageTable = $("#imageTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    await refreshImages();
});

// =================== Fetch/Post data ===================
async function getImages() {
    const resp = await fetch(`/manager/images/get`, { method: 'GET' });
    return resp.json();
}

// =================== Call these ===================
async function refreshImages() {
    imageTable.clear();
    let data = await getImages();
    imageTable.rows.add(data).draw();
    imageTable.columns.adjust().draw();
}
