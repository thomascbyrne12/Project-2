// Link to server
const url = "http://localhost:5000";

// Reads in JSON data
d3.json(url).then(function(cricket_data) {
    console.log(cricket_data);
    create_run_bar(cricket_data);
    create_averages(cricket_data);
    create_career(cricket_data);
});

function create_run_bar(data) {
    
    // Initialize empty data array
    var push1 = [];
    var push2 = [];

    // For loop to fill runs array
    for (i = 0; i < 10; i++) {
        push1.push(data[i].runs);
    }

    // For loop to fill names array
    for (i = 0; i < 10; i++) {
        push2.push(data[i].playername)
    }

    // Define data array
    var data = [{
        x: push1,
        y: push2,
        type: 'line',
        orientation: 'h'
    }];

    var layout = {
        title: 'Most Runs Scored (Career)'
    };

    Plotly.newPlot('line', data, layout);
};

function create_averages(data) {

    // Filling data for averages plot
    var push1 = [
        data[52].avg,
        data[47].avg,
        data[402].avg,
        data[275].avg,
        data[283].avg,
        data[103].avg,
        data[388].avg,
        data[56].avg,
        data[110].avg,
        data[42].avg
    ];

    // Filling data for player names plot
    var push2 = [
        data[52].playername,
        data[47].playername,
        data[402].playername,
        data[275].playername,
        data[283].playername,
        data[103].playername,
        data[388].playername,
        data[56].playername,
        data[110].playername,
        data[42].playername
    ];

    // Define data array
    var data = [{
        x: push1,
        y: push2,
        type: 'bar',
        orientation: 'h'
    }];

    var layout  = {
        title: 'Highest Career Batting Averages'
    };

    Plotly.newPlot('bar', data, layout);
};

function create_career(data) {

    // Filling data for career length plot
    var push1 = [
        data[314].careerlength,
        data[681].careerlength,
        data[144].careerlength,
        data[0].careerlength,
        data[276].careerlength,
        data[436].careerlength,
        data[2486].careerlength,
        data[76].careerlength,
        data[258].careerlength,
        data[334].careerlength
    ];

    // Filling data for player names plot
    var push2 = [
        data[314].playername,
        data[681].playername,
        data[144].playername,
        data[0].playername,
        data[276].playername,
        data[436].playername,
        data[2486].playername,
        data[76].playername,
        data[258].playername,
        data[334].playername
    ];

    // Define data array
    var data = [{
        x: push1,
        y: push2,
        type: 'bar',
    }];

    var layout = {
        title: 'Longest Internation Careers'
    };

    Plotly.newPlot('upright-bar', data, layout);
};
