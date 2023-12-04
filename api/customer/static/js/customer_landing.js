function scaleText(pixelIncrement){
    currentSize = parseFloat(window.getComputedStyle(document.documentElement).fontSize);
    document.documentElement.style.fontSize = (currentSize + pixelIncrement) + 'px';
}