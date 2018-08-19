<!doctype html>
<html>
<head>
    <title>experiment graph</title>

    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis-network.min.css" rel="stylesheet" type="text/css"/>

    <style type="text/css">
        #mynetwork {
            width: 800px;
            height: 600px;
            border: 1px solid lightgray;
        }
    </style>
</head>
<body>

<div id="mynetwork"></div>
<pre id="eventSpan"></pre>

<script type="text/javascript">

    // create an array with nodes
    var nodes = new vis.DataSet({{!nodes}});

    // create an array with edges
    var edges = new vis.DataSet({{!edges}})

    // create a network
    var container = document.getElementById('mynetwork');
    var data = {
        nodes: nodes,
        edges: edges
    };

    var options = {
			interaction:{hover:true},
            layout:{randomSeed:0}
		};

    var network = new vis.Network(container, data, options);

    network.on("hoverNode", function (params) {
        var node = nodes._data[params['node']];
        document.getElementById('eventSpan').innerHTML = '<h2>hoverNode event: </h2>' + JSON.stringify(node, null, 4);
    });
    network.on("blurNode", function (params) {
        document.getElementById('eventSpan').innerHTML = '';
    });
    network.on("selectEdge", function (params) {
        var nodes = network.getConnectedNodes(params['edges'][0]);
        window.open('diff/' + nodes[0].toString() + '/' + nodes[1].toString());
    });


</script>


</body>
</html>
