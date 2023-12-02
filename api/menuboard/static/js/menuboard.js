/*
function scaleMenu(numC, catSize, iSize){
    document.getElementById("board").style.columnCount = numC;
    var categories = document.querySelectorAll('h2');
    for (var i = 0; i < categories.length; i++) {
        categories[i].style.fontSize = catSize;
    }
    var items = document.querySelectorAll('li');
    for (var i = 0; i < items.length; i++) {
        items[i].style.fontSize = iSize;
    }
}
*/

function checkOverflow(element){
    var curOverf = element.style.overflow; 
        if ( !curOverf || curOverf === "visible" ) 
            element.style.overflow = "hidden";  
        var isOverflowing = el.clientWidth < el.scrollWidth || el.clientHeight < el.scrollHeight; 
        el.style.overflow = curOverf; 
                  
        return isOverflowing; 
}
