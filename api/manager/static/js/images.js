// Elements
let imageTable = null;
let inventoryDescriptionInput = null;
let inventoryCategoryInput = null;

// Other global vars
let lastSelected = null;

$(document).ready(async function() {
    inventoryDescriptionInput = $("#inventoryDescriptionInput")[0];
    inventoryCategoryInput = $("#inventoryCategoryInput")[0];

    imageTable = $("#imageTable").DataTable({
        select: true,
        paging: false,
        dom: '<"dt_row"rif>t',
        "scrollCollapse": true,
        "scrollY": "65vh",
    });

    imageTable.on('click', 'tbody tr', async function() {
        lastSelected = imageTable.row(this).data();

        inventoryDescriptionInput.value = lastSelected[2];
        inventoryCategoryInput.value = lastSelected[3];
    })

    $("#deleteImageBtn").click(async function() {
        let data = {};
        data['imageid'] = lastSelected[0];
        data['publicid'] = lastSelected[1];

        if (confirm(`Delete image: ${lastSelected[2]}?`)) {
            await deleteImage(data);
            await refreshImages();
        }
    });

    $("#imageEditModalSubmit").click(async function() {
        let data = {};
        data['imageid'] = lastSelected[0];
        data['description'] = inventoryDescriptionInput.value;
        data['category'] = inventoryCategoryInput.value;

        await updateImage(data);
        await refreshImages();
    });

    await refreshImages();
});

// =================== Fetch/Post data ===================
async function getImages() {
    const resp = await fetch(`/manager/images/get`, { method: 'GET' });
    return resp.json();
}
async function updateImage(data) {
    const resp = await fetch(`/manager/images/update`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}
async function deleteImage(data) {
    const resp = await fetch(`/manager/images/delete`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
}

// =================== Call these ===================
async function refreshImages() {
    imageTable.clear();
    let data = await getImages();
    imageTable.rows.add(data).draw();
    imageTable.columns.adjust().draw();
}
