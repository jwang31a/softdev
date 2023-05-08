data = {"blue" : 3, 
    "orange" : 6, 
    "bobby" : 10,
    "keyboard" : 4,
    "banana" : 7
};

var visualize = function() {
    const div = d3.create("div")
        .style("text-align", "right").html("<p>bobby</p>")
}

v = document.getElementById("visualize");
v.addEventListener("click", visualize);