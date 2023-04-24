//retrieve node in DOM via ID
var c = document.getElementById("slate");
var r = document.getElementById("buttonToggle");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ";
    }
    else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.clientX - e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.clientY - e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    console.log(e.clientX, e.offsetX, e.clientY, e.offsetY);
    // console.log(e.clientX, e.clientY);
    ctx.fillRect(e.offsetX, e.offsetY, 10, 10);
}

var drawCircle = function(e) {
    var mouseX = e.clientX; //gets X-coor of mouse when event is fired
    var mouseY = e.clientY; //gets Y-coor of mouse when event is fired
    //console.log("mouseclick registered at ", mouseX, mouseY);
    //console.log(e.clientX, e.clientY);
    //ctx.(mouseX, mouseY, 10, 10);
}

var draw = function(e) {
    if (mode === "rect") {
        drawRect(e);
    } else {
        drawCircle(e);
    }
}

var wipeCanvas = () => {

}

c.addEventListener("click", draw); //passes the mouse event as parameter for the function
r.addEventListener('click', toggleMode);