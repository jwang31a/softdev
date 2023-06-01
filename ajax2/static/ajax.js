var loadXMLDoc = function() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            var response = JSON.parse(xhttp.responseText);
            console.log(response);
            document.getElementById("pain").innerHTML = response.username;
        }
        console.log("ayo this worked");
    }
    xhttp.open("POST", "/ajax");
    var u = document.getElementById("username").value;
    var p = document.getElementById("password").value;
    var postVars = u + " " + p;
    xhttp.send(postVars);
}

/*
$(document).ready(function() {
    $("form").on("submit", function(event) {
        $.ajax({
            data : {
                username : $("#username").val(),
                password : $("#password").val()
            },
            type : "POST",
            url : "/ajax"
        })
        .done(function(data) {
            $("#output").text(data.output).show();
        });
        event.preventDefault();
    });
});
*/