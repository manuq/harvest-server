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

var colors = [
    "#EA3556", "#B182E6",
    "#EDDE45", "#ED146F",
    "#9BF0E9", "#8DE582",
];

var laptopColor = function () {
    return d3.scale.ordinal().range(colors);
}();

function crearEquiposMuestra() {

    var chart = d3.select(".chart.equipos-muestra")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + (width + margin.left + margin.right) / 2 + "," + (height + margin.top + margin.bottom) / 2 + ")");

    var partition = d3.layout.partition()
        .sort(null)
        .size([2 * Math.PI, radius * radius])
        .value(function(d) { return 1; });

    var arc = d3.svg.arc()
        .startAngle(function(d) { return d.x; })
        .endAngle(function(d) { return d.x + d.dx; })
        .innerRadius(function(d) { return Math.sqrt(d.y); })
        .outerRadius(function(d) { return Math.sqrt(d.y + d.dy); });

    var labelRadius = radius + 30;

    $.getJSON("/json/equipos_muestra", function(data) {
        var value = function(d) { return d.size; };
        var path = chart.datum(data).selectAll("path");
        path.data(partition.value(value).nodes)
            .enter().append("path")
            .attr("class", "donaPath")
            .attr("display", function(d) { return d.depth ? null : "none"; }) // hide inner ring
            .attr("d", arc)
            .style("fill", function(d) { return laptopColor((d.children ? d : d.parent).name); })
            .style("fill-rule", "evenodd")
            .on("mouseover", function(d) {
            })
            .on("mouseout", function(d){
            });

        path.data(partition.value(value).nodes)
            .enter().append("text")
            .attr("class", "donaText")
            .attr("transform", function(d) {
                var c = arc.centroid(d);
                x = c[0],
                y = c[1],
                h = Math.sqrt(x*x + y*y);
                return "translate(" + (x/h * labelRadius) +  ',' +
                    (y/h * labelRadius) +  ")";
            })
            .attr("dy", ".5em")
            .attr("visibility", "visible")
            .text(function(d) {
                if (!d.parent) {
                    return "";
                }
                if (d.parent.name == 'all') {
                    return d.name;
                }
                return "";
            });
    });
}

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

function crearUsoSugarGnomeDuracion() {
    var chart = d3.select(".chart.sugar-gnome-duracion")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + (width + margin.left + margin.right) / 2 + "," + (height + margin.top + margin.bottom) / 2 + ")");

    var arc = d3.svg.arc()
        .innerRadius(0)
        .outerRadius(radius);

    var pie = d3.layout.pie()
        .value(function(d) {
            return d.value;
        });

    $.getJSON("/json/uso_sugar_gnome_duracion", function(data) {

        var total = data[0].value + data[1].value;
        data[0].percentage = Math.round(data[0].value / total * 100);
        data[1].percentage = 100 - data[0].percentage;

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
            .attr("dy", "2.5em")
            .text(function(d) {
                return d.data.session;
            });

        arcs.append("text")
            .attr("class", "sliceText big")
            .attr("transform", function(d) {
                return "translate(" + arc.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .text(function(d) {
                return d.data.percentage + '%';
            });
    });

}

function crearUsoSugarGnomeConteo() {
    var chart = d3.select(".chart.sugar-gnome-conteo")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + (width + margin.left + margin.right) / 2 + "," + (height + margin.top + margin.bottom) / 2 + ")");

    var arc = d3.svg.arc()
        .innerRadius(0)
        .outerRadius(radius);

    var pie = d3.layout.pie()
        .value(function(d) {
            return d.value;
        });

    $.getJSON("/json/uso_sugar_gnome_conteo", function(data) {

        var total = data[0].value + data[1].value;
        data[0].percentage = Math.round(data[0].value / total * 100);
        data[1].percentage = 100 - data[0].percentage;

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
            .attr("dy", "2.5em")
            .text(function(d) {
                return d.data.session;
            });

        arcs.append("text")
            .attr("class", "sliceText big")
            .attr("transform", function(d) {
                return "translate(" + arc.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .text(function(d) {
                return d.data.percentage + '%';
            });

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
            return d.act_name;
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
                return "translate(" + barX(d.act_name) + ", 0)";
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
                return d.act_name
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

crearEquiposMuestra();
crearTiempoDeUso();
crearUsoSugarGnomeDuracion();
crearUsoSugarGnomeConteo();
crearRankingActs();
crearRankingApps();
