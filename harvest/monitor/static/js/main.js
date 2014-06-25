var margin = {
    top: 40,
    right: 30,
    bottom: 30,
    left: 60
};
var width = 960 - margin.left - margin.right;
var height = 500 - margin.top - margin.bottom;
var radius = 180;

var formato_hora = d3.time.format("%H:%M hs");

function crearTiempoDeUso() {
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
        .tickFormat(function(d) {
            return formato_hora(new Date(0, 0, 0, 0, 0, d))
        });

    var chart = d3.select(".chart.uso-semanal")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    $.getJSON("/json/tiempo_de_uso", function(data) {
        barX.domain(data.map(function(d) {
            return d.year + ', ' + d.week;
        }));
        barY.domain([0, d3.max(data, function(d) {
            return d.spent_sugar + d.spent_gnome;
        })]);

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
            .attr("transform", function(d, i) {
                return "translate(" + barX(d.year + ', ' + d.week) + ", 0)";
            });

        bar.append("rect")
            .attr("class", "bar gnome")
            .attr("y", function(d) {
                return barY(d.spent_gnome)
            })
            .attr("width", barX.rangeBand())
            .attr("height", function(d) {
                return height - barY(d.spent_gnome)
            });

        bar.append("rect")
            .attr("class", "bar sugar")
            .attr("y", function(d) {
                return barY(d.spent_sugar + d.spent_gnome)
            })
            .attr("width", barX.rangeBand())
            .attr("height", function(d) {
                return height - barY(d.spent_sugar)
            });

        bar.append("text")
            .attr("class", "barText")
            .attr("x", barX.rangeBand() / 2)
            .attr("y", function(d) {
                return barY(d.spent_sugar + d.spent_gnome) - 3
            })
            .attr("dy", "-0.5em")
            .text(function(d) {
                return formato_hora(new Date(0, 0, 0, 0, 0, d.spent_sugar + d.spent_gnome))
            });
    });
}

function crearUsoSugarGnome() {
    var data = [{'session': 'Sugar', 'value': 12356},
                {'session': 'GNOME', 'value': 9356}];

    var chart = d3.select(".chart.sugar-gnome")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .data(data)
        .attr("transform", "translate(" + (width + margin.left + margin.right) / 2 + "," + (height + margin.top + margin.bottom) / 2 + ")");

    var arc = d3.svg.arc()
        .innerRadius(0)
        .outerRadius(radius);

    var pie = d3.layout.pie()
        .value(function(d) {
            return d.value;
        });

     var arcs = chart.selectAll(".slice")
        .data(pie(data))
        .enter()
        .append("g")
        .attr("class", function(d) {
            if (d.data.session == 'Sugar') {
                return "slice sugar";
            } else {
                return "slice gnome";
            }
        });

    arcs.append("path")
        .attr("d", arc)
        .attr("class", "sugar");

    arcs.append("text")
        .attr("class", "sliceText")
        .attr("transform", function(d) {
            return "translate(" + arc.centroid(d) + ")";
        })
        .attr("dy", ".35em")
        .text(function(d) {
            return d.data.session;
        });

}

function crearRankingActs() {
    var barY = d3.scale.linear()
        .range([height, 0]);

    var barX = d3.scale.ordinal()
        .rangeRoundBands([0, width], 0.1);

    var chart = d3.select(".chart.ranking-acts")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    $.getJSON("/json/ranking_actividades", function(data) {
        var domain = data.map(function(d) {
            return d.bundle_id;
        })

        var missing = 10 - domain.length;
        for (var i = 0; i < missing; i++) {
            domain.push(i);
        }

        barX.domain(domain);
        barY.domain([0, d3.max(data, function(d) {
            return d.spent_time;
        })]);

        var bar = chart.selectAll(".bar")
            .data(data)
            .enter().append("g")
            .attr("transform", function(d, i) {
                return "translate(" + barX(d.bundle_id) + ", 0)";
            });

        bar.append("rect")
            .attr("class", "bar sugar")
            .attr("y", function(d) {
                return barY(d.spent_time)
            })
            .attr("width", barX.rangeBand())
            .attr("height", function(d) {
                return height - barY(d.spent_time)
            });

        bar.append("text")
            .attr("class", "barText")
            .attr("x", barX.rangeBand() / 2)
            .attr("y", function(d) {
                return barY(d.spent_time) - 3
            })
            .attr("dy", "-0.5em")
            .text(function(d) {
                return d.bundle_id
            });

    });
}

function crearRankingApps() {
    var barY = d3.scale.linear()
        .range([height, 0]);

    var barX = d3.scale.ordinal()
        .rangeRoundBands([0, width], 0.1);

    var chart = d3.select(".chart.ranking-apps")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    $.getJSON("/json/ranking_aplicaciones", function(data) {
        var domain = data.map(function(d) {
            return d.app_name;
        });

        var missing = 10 - domain.length;
        for (var i = 0; i < missing; i++) {
            domain.push(i);
        }

        barX.domain(domain);
        barY.domain([0, d3.max(data, function(d) {
            return d.spent_time;
        })]);

        var bar = chart.selectAll(".bar")
            .data(data)
            .enter().append("g")
            .attr("transform", function(d, i) {
                return "translate(" + barX(d.app_name) + ", 0)";
            });

        bar.append("rect")
            .attr("class", "bar gnome")
            .attr("y", function(d) {
                return barY(d.spent_time)
            })
            .attr("width", barX.rangeBand())
            .attr("height", function(d) {
                return height - barY(d.spent_time)
            });

        bar.append("text")
            .attr("class", "barText")
            .attr("x", barX.rangeBand() / 2)
            .attr("y", function(d) {
                return barY(d.spent_time) - 3
            })
            .attr("dy", "-0.5em")
            .text(function(d) {
                return d.app_name
            });

    });
}

crearTiempoDeUso();
crearUsoSugarGnome();
crearRankingActs();
crearRankingApps();