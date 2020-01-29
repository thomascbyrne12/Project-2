// Link to server
const url = "localhost:5500";

// Reads in JSON data
d3.json(url, function(cricket_data) {
    create_bar(cricket_data);
});

function create_bar(data) {
    // Define SVG area dimensions
    var svgWidth = 960;
    var svgHeight = 660;

    // Define the chart's margins as an object
    var chartMargin = {
        top: 30,
        right: 30,
        bottom: 30,
        left: 30
    };

    // Define dimensions of the chart area
    var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
    var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

};