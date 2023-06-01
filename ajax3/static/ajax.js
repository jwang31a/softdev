function loadXMLDoc() {
    var req = new XMLHttpRequest()
    req.onreadystatechange = function()
    {
        if (req.readyState == 4)
        {
            if (req.status != 200)
            {
                //error handling code here
            }
            else
            {
                var response = JSON.parse(req.responseText)
                document.getElementById('myDiv').innerHTML = response.output
            }
        }
    }

    req.open('POST', '/ajax')
    req.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    var u = document.getElementById("username").value;
    var p = document.getElementById("password").value;
    var postVars = "username=" + u + "&password=" + p;
    console.log(postVars);
    req.send(postVars);
}