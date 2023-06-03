//this doesn't do anything, copy pasted code in script tag in index.html
var loadDoc = function() {
    var xhttp = new XMLHttpRequest();
    //i have no idea what is in this request
    //console.log(xhttp);
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("aj").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "static/ajax_info.txt", true);
    xhttp.send();
}

var unloadDoc = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("aj").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "static/ajax_info2.txt", true);
    xhttp.send();
}
