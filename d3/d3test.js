a = document.getElementById("a");
data = document.getElementById("data");

//selectAll() selects all elements that match this, in this case, tag
//select() selects the first element that matches this description
var dothings = function() {
  d3.selectAll("p").html("updated")
}

//if we have data, we can edit what's on the page using this
//.html() edits the inner html of a tag
var dahta = function() {
  let nice = [];
  for (let i = 0; i < 9; i++) {
    nice.push(Math.random());
  }
  d3.selectAll("p").data(nice).html((d) => d);
}

a.addEventListener("click", dothings);
data.addEventListener("click", dahta);