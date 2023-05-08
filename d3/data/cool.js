const width = 500, height = 500;
const x_scale = d3.scaleBand().range([0, width]);
const y_scale = d3.scaleBand().range([height, 0]);

const a = d3.select("d3_demo")
    .attr("width", width)
    .attr("height", height);

const data = {
    fruit: ["apple", "orange", "banana", "grape", "lemon"],
    nums: [5, 16, 3, 10, 7]
};

x_scale.domain(data.fruit.map((d) => d.fruit));
y_scale.domain([0, d3.max(data.nums, (d) => d.nums)]);

a
 .selectAll("rect")
 .data(data)
 .join("rect")
  .attr("class", "bar")
  .attr("x", (d) => x_scale(d.fruit))
  .attr("y", (d) => y_scale(d.nums))
  .attr("width", x_scale.bandwidth())
  .attr("height", (d) => height - y_scale(d.n));