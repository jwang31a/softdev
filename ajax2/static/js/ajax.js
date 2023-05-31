var loadXMLDoc = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(xhttp.responseText);
            document.getElementById("pain").innerHTML = response.username;
        }
    }
    xhttp.open("POST", "/ajax")
    var u = document.getElementById("user").value;
    var hid = document.getElementById("hidden").value;
    var postVars = "username="+u+"&hidden"+hid;
    xhttp.send(postVars);
}

console.log("this script exists ayo")