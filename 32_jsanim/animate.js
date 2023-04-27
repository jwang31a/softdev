//getting the stuff from DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("circle");
var dvdButton = document.getElementById("dvd");
var stopButton = document.getElementById("stop");

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = function(e) {
    //e.preventDefault();
    ctx.clearRect(0,0,500,500);
};

//drawdot code begin
var radius = 0;
var growing = true;

//helper function for drawDot
//initially a callback for requestAnimationFrame, but changed, which is why this exists
var grow = function() {
    clear();
    if (growing) {
        radius++;
        ctx.beginPath();
        ctx.fillStyle = "blue";
        ctx.arc(250,250,radius,0, 2*Math.PI);
        ctx.fill();
        ctx.stroke();
    } else {
        radius--;
        ctx.beginPath();
        ctx.fillStyle = "blue";
        ctx.arc(250,250,radius,0, 2*Math.PI);
        ctx.fill();
        ctx.stroke();
    }
    if (radius >= 250) {
        growing = false;
    } else if (radius == 0) {
        growing = true;
    }
    window.cancelAnimationFrame(requestID);
}

var drawDot = () => {
    console.log("asdf");
    console.log(typeof requestID);
    grow();
    requestID = window.requestAnimationFrame(drawDot);
    console.log(radius + "radius is" + "and isGrowing" + growing);
};

var stopIt = function() {
    console.log("stopit");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

var dvdLogoSetup = function() {
    window.cancelAnimationFrame(requestID);
    var rectWidth = 60;
    var rectHeight = 40;

    var rectX = Math.random()*440;
    var rectY = Math.random()*460;

    var xVel = 1;
    var yVel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        ctx.clearRect(0,0, c.width,c.height)
        // ctx.fillRect(rectX, rectY, rectWidth, rectHeight);
        //line above seems to be testing where the image would be
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX <= 0 || rectX + rectWidth >= c.width) {
            xVel = -1 * xVel;
        }
        if (rectY <= 0 || rectY + rectHeight >= c.height) {
            yVel = -1 * yVel;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    }
    dvdLogo();
}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);