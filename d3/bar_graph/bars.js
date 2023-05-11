barsButton = document.getElementById("crazy");

var clear = function() {
    d3.selectAll("g").remove();
}

var makeData = function(n) {
    let data = [];
    for (let i = 0; i < n; i++) {
        data.push(Math.round(Math.random() * 100) / 100);
    }
    return data;
}

var barry = function() {
    //still not sure how to edit a specific svg, since all the tutorials I've seen interact with newly created svgs
    clear();
    let data = makeData(10);
    // console.log(data);
    
    var svg = d3.select("svg"), 
        margin = 100, 
        width = svg.attr("width") - margin, 
        height = svg.attr("height") - margin;

    var barWidth = width / data.length;

    var xScale = d3.scaleBand()
        .range([0, width])
        .padding(0.5)
    var yScale = d3.scaleLinear()
        .range([height, 0]);

    var g = svg.append("g")
        .attr("transform", "translate(" + 50 + "," + 50 + ")");

    xScale.domain(data.map(function(i) {
        return i;
    }));
    yScale.domain([0, d3.max(data, function(d) {
        return d;
    })])

    console.log(xScale);

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));

    g.append("g")
        .call(d3.axisLeft(yScale).tickFormat(function(d) {
            return d;
        }));

    g.selectAll("bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", function(i) {return xScale(i);})
        .attr("y", function(d) {return yScale(d);})
        .attr("width", xScale.bandwidth())
        .attr("height", function(d) {return height - yScale(d) ;});
}

barsButton.addEventListener("click", barry);