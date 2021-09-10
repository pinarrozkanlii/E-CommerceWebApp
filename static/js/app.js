function myfunc(){
    const sect = document.querySelector('section');
    const table = document.querySelector('table');

    var addRule = (function (style) {
        var sheet = document.head.appendChild(style).sheet;
        return function (selector, css) {
            var propText = typeof css === "string" ? css : Object.keys(css).map(function (p) {
                return p + ":" + (p === "content" ? "'" + css[p] + "'" : css[p]);
            }).join(";");
            sheet.insertRule(selector + "{" + propText + "}", sheet.cssRules.length);
        };
    })(document.createElement("style"));
    
    addRule(".background:after", {
        position: "absolute",
        width: "100%",
        height: "100%",
        background: "rgba(0,0,0,0.7)",
        top: "0",
        left:"0",
        content: "''"
    });
    addRule("section",{
        visibility:"visible"
        
    });
    
    table.style.zIndex = "1";
    
    const t1 = new TimelineMax();

    t1.fromTo(sect,1,{height:"0px"},{height:'310px', ease:Power2.easeInOut})
}
