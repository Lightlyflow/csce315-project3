function scaleText(pixelIncrement){
    currentSize = parseFloat(window.getComputedStyle(document.documentElement).fontSize);
    document.documentElement.style.fontSize = (currentSize + pixelIncrement) + 'px';
}

function toggleImages() {
    var shareTeaLogo = document.getElementById('sharetea-logo');
    shareTeaLogo.setAttribute("src", "");
    shareTeaLogo.style.setProperty("color", "black");
    shareTeaLogo.style.setProperty("background", "white");
    shareTeaLogo.style.setProperty("box-shadow", "none");
    shareTeaLogo.style.setProperty("border-radius", "7px", "important");
    shareTeaLogo.parentElement.style.setProperty("width", "fit-content");

    var landingBackground = document.getElementById('landing-background');
    landingBackground.style.setProperty("background", "white");

    var accessimage = document.getElementById("dropdownMenuButton");
    while (accessimage.firstChild) {
        accessimage.removeChild(accessimage.firstChild);
    }
    accessimage.innerHTML = "Accessibility";
    accessimage.style.setProperty("color", "blue");
    accessimage.style.setProperty("background", "white");
    accessimage.style.setProperty("box-shadow", "none");
    accessimage.style.setProperty("border-radius", "7px", "important");

    var googleLogo = document.getElementById('google-logo');
    googleLogo.setAttribute("src", "");
}