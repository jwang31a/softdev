//getting the stuff from DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    ctx.clearRect(0,0,500,500);
};

var radius = 0;
var growing = true;

var callback = function() {
    if (growing) {
        radius++;
        ctx.beginPath();
        ctx.arc(250,250,radius,0, 2*Math.PI);
        ctx.stroke();
    } else if (radius == 250) {
        growing = false;
    } else if (radius == 0) {
        growing = true;
    } else {
        radius--;
    }
}

var drawDot = () => {
    console.log("asdf");
    if (typeof requestID === "none") {
        requestID = window.requestAnimationFrame(callback);
    }
};

var stopIt = function() {
    console.log("stopit");
    console.log(requestID);
};

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
