var margin = {top: 40, right: 30, bottom: 30, left: 60};
var width = 960 - margin.left - margin.right;
var height = 500 - margin.top - margin.bottom;

var formato_hora = d3.time.format("%H:%M hs");

var barY = d3.scale.linear()
    .range([height, 0]);

var barX = d3.scale.ordinal()
    .rangeRoundBands([0, width], 0.1);

var xAxis = d3.svg.axis()
    .scale(barX)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(barY)
    .orient("left")
    .tickFormat(function(d) { return formato_hora(new Date(0, 0, 0, 0, 0, d)) });

var chart = d3.select(".chart.uso-semanal")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

$.getJSON("/json/tiempo_de_uso", function (data) {
    barX.domain(data.map(function (d) { return d.year + ', ' + d.week; }));
    barY.domain([0, d3.max(data, function(d) { return d.spent_time; })]);

    chart.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    chart.append("g")
        .attr("class", "y axis")
        .call(yAxis);

    var bar = chart.selectAll(".bar")
        .data(data)
        .enter().append("g")
        .attr("transform", function (d, i) { return "translate(" + barX(d.year + ', ' + d.week) + ", 0)"; });

    bar.append("rect")
        .attr("class", "bar")
        .attr("y", function (d) { return barY(d.spent_time) })
        .attr("width", barX.rangeBand())
        .attr("height", function (d) { return height - barY(d.spent_time) });

    bar.append("text")
        .attr("class", "barText")
        .attr("x", barX.rangeBand() / 2)
        .attr("y", function (d) { return barY(d.spent_time) - 3 })
        .attr("dy", "-0.5em")
        .text(function (d) { return formato_hora(new Date(0, 0, 0, 0, 0, d.spent_time)) });
});

var barY2 = d3.scale.linear()
    .range([height, 0]);

var barX2 = d3.scale.ordinal()
    .rangeRoundBands([0, width], 0.1);

var chart2 = d3.select(".chart.ranking-acts")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

$.getJSON("/json/ranking_actividades", function (data) {
    console.log(data);

    barX2.domain(data.map(function (d) { return d.bundle_id; }));
    barY2.domain([0, d3.max(data, function(d) { return d.spent_time; })]);

    var bar = chart2.selectAll(".bar")
        .data(data)
        .enter().append("g")
        .attr("transform", function (d, i) { return "translate(" + barX2(d.bundle_id) + ", 0)"; });

    bar.append("rect")
        .attr("class", "bar")
        .attr("y", function (d) { return barY2(d.spent_time) })
        .attr("width", barX2.rangeBand())
        .attr("height", function (d) { return height - barY2(d.spent_time) });

    bar.append("text")
        .attr("class", "barText")
        .attr("x", barX2.rangeBand() / 2)
        .attr("y", function (d) { return barY2(d.spent_time) - 3 })
        .attr("dy", "-0.5em")
        .text(function (d) { return d.bundle_id });

});
