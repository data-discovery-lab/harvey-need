function gridData(csvData) {
  var data = new Array();
  var xpos = 1; //starting xpos and ypos at 1 so the stroke will show when we make the grid below
  var ypos = 1;
  var width = 50;
  var height = 50;
  var click = 0;

  console.log(csvData);

  // iterate for rows 
  for (var column = 0; column < 4; column++) {
    data.push( new Array() );
    
    var MAX = (column) * 5;

    // iterate for cells/columns inside rows
    for (var row = 0; row < 5; row++) {
      data[column].push({
        x: xpos,
        y: ypos,
        width: width,
        height: parseInt(csvData[MAX].weight)*5,
        click: click
      })
      MAX++;
      // Increment the y position to move down a row
      ypos += width + 25;
    }
    // Reset the Y position after a column is complete
    ypos = 1;
    // Increment the x position to move over a column
    xpos += height + 100; 
  }
  return data;
}

d3.text("text.csv", function(datasetText) { 

  var csvData = d3.csvParse(datasetText);

  var gd = gridData(csvData);
  // I like to log the data to the console for quick debugging
  console.log(gd);

  var grid = d3.select("#grid")
    .append("svg")
    .attr("width","510px")
    .attr("height","610px");
    
  var column = grid.selectAll(".column")
    .data(gd)
    .enter().append("g")
    .attr("class", "column")
    .style("padding-left", "10px");


  var row = column.selectAll(".square")
    .data(function(d) { return d; })
    .enter().append("rect")
    .attr("class","square")
    .attr("x", function(d) { return d.x; })
    .attr("y", function(d) { return d.y; })
    .attr("width", function(d) { return d.width; })
    .attr("height", function(d) { return d.height; })
    .style("margin-bottom", "10px")
    .style("fill", "#fff")
    .style("stroke", "#222")
    .style("stroke-width", "1")
});
