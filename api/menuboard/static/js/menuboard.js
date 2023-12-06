function checkOverflow(element){
    var curOverf = element.style.overflow; 
        if ( !curOverf || curOverf === "visible" ) 
            element.style.overflow = "hidden";  
        var isOverflowing = el.clientWidth < el.scrollWidth || el.clientHeight < el.scrollHeight; 
        el.style.overflow = curOverf; 
                  
        return isOverflowing; 
}
