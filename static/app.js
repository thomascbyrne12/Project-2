// Link to server
const url = "localhost:5500";

// Reads in JSON data
d3.json(url, function(cricket_data) {
    create_bar(cricket_data);
});

function create_bar(data) {

};