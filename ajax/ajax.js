function loadDoc() {
    var xhttp = new XMLHttpRequest();
    //i have no idea what is in this request
    xhttp.status = 200;
    console.log(xhttp);
    
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "ajax_info.txt", true);
    xhttp.send();
}