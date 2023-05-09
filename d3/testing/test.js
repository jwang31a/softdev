//d3 interacts with svg elements
//svg kind of like canvas, but different since elements exist in html instead of just in the canvas

var lineButton = document.getElementById("lineButton");
var rectButton = document.getElementById("rectButton");
var visButton = document.getElementById("visualize");

width = 500;
height = 500;

var lines = function() {
    d3.selectAll("svg").remove();
    var svg = d3.select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
    svg.append("line")
        .attr("x1", 0)
        .attr("y1", 200)
        .attr("x2", 450)
        .attr("y2", 350)
        .attr("stroke", "black");
}

var rects = function() {
    d3.selectAll("svg").remove();
    var svg = d3.select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", height);
    svg.append("rect")
        .attr("width", 50)
        .attr("height", 50);
        //.attr("opacity", 0.1); (this makes color lighter or darker, 0 is completely transparent, 1 is completely opaque)
}

//big chunky function that does interesting stuff
var visualize = function() {
    //removes all svgs to have a clean slate
    d3.selectAll("svg").remove();
    //creates data (data2 commented out, but would map all values of array and multiply by 20)
    var data = [Math.random(), Math.random(), Math.random(), Math.random(), Math.random()];
    //const data2 = data.map(x => x * 20);
    //variables to have while graphing
    var width = 250;
    var scale = 50;
    var barHeight = 25;

    //selects the body, creates an svg with certain width and height dependent on array length
    var graph = d3.select("body")
        .append("svg")
        .attr("width", width)
        .attr("height", barHeight * data.length);
    //creates groups, enters data into them
    //each new group will be transformed down based on which element of the array it is, using i
    var bar = graph.selectAll("g")
        .data(data)
        .enter()
        .append("g")
        .attr("transform", function(d, i) {
            return "translate(0," + i * barHeight + ")";
        });
    //adds rect to bar, which is a group
    bar.append("rect")
        .attr("width", function(d) {
            //scale changes a bit here to make data visible, but in actual data, this wouldn't be needed
            return d * scale + 10;
        })
        .attr("height", barHeight - 1);
    //puts text into each box
    bar.append("text")
        .attr("x", function(d) {
            return d * scale;
            })
        .attr("y", barHeight / 2)
        .text(function(d) {
            //sketchy way of rounding to two decimal places
            return Math.round(d * 100) / 100;
        });
}

/*
circles have cx, cy (coordinates of the origin), r
ellipses have cx, cy, rx, ry
text is also an element, has x, y, inner html can have text as well
<g> is used to group elements together, helps with applying transformations to children of elements
*/

lineButton.addEventListener("click", lines);
rectButton.addEventListener("click", rects)
visButton.addEventListener("click", visualize);