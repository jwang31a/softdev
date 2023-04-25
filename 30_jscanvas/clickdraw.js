//retrieve node in DOM via ID
var c = document.getElementById("slate");
var r = document.getElementById("buttonToggle");
var w = document.getElementById("buttonClear");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ";
        var b = document.getElementById("buttonToggle").innerHTML = "circ";
    }
    else {
        mode = "rect";
        var b = document.getElementById("buttonToggle").innerHTML = "rect";
    }
    console.log(b);
}

var drawRect = function(e) {
    var mouseX = e.clientX - e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.clientY - e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    console.log(e.clientX, e.offsetX, e.clientY, e.offsetY);
    // console.log(e.clientX, e.clientY);
    ctx.fillStyle = "orange";
    ctx.strokeStyle = "black";
    ctx.beginPath();
    ctx.fillRect(e.offsetX, e.offsetY, 30, 30);
    ctx.stroke();
}

var drawCircle = function(e) {
    var mouseX = e.clientX; //gets X-coor of mouse when event is fired
    var mouseY = e.clientY; //gets Y-coor of mouse when event is fired
    //console.log("mouseclick registered at ", mouseX, mouseY);
    //console.log(e.clientX, e.clientY);
    //ctx.(mouseX, mouseY, 10, 10);
    ctx.beginPath();
    ctx.fillStyle = "orange";
    ctx.arc(e.offsetX, e.offsetY, 20, 0, 2*Math.PI);
    //arc creates empty circle
    ctx.fill();
    ctx.stroke();
}

var draw = function(e) {
    if (mode === "rect") {
        drawRect(e);
    } else {
        drawCircle(e);
    }
}

var wipeCanvas = (e) => {
    //4 arguments, x, y, width (horizontal), length (vertical)
    ctx.clearRect(0, 0, 600, 600);
}

c.addEventListener("click", draw); //passes the mouse event as parameter for the function
r.addEventListener('click', toggleMode);
w.addEventListener("click", wipeCanvas);