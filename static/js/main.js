const ctx = document.getElementById('myChart').getContext('2d');

var graph={
    type: 'line',
    data: {
        labels: ['jan', 'feb', 'mar', 'apr', 'may', 'jun'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(73, 198, 230, 0.5)',
            ],
            borderWidth: 1
        }]
    },
    options: {}
}

const myChart = new Chart(ctx, graph);



var socket=new WebSocket('ws://127.0.0.1:8000/ws/graph/')

socket.onmessage=function(event){
    var data=JSON.parse(event.data);
    console.log(data);

    var newGraph=graph.data.datasets[0].data;
    newGraph.shift();
    newGraph.push(data.value);
    graph.data.datasets[0].data=newGraph;

    myChart.update();

    // document.querySelector("#app").innerText=data.value;
}