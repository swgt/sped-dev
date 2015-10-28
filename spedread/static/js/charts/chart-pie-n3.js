nv.addGraph(function() {
  var chart = nv.models.pieChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .showLabels(true);

    d3.select("#chart-pie svg")
        .datum( [
              {
                "label": "Entradas",
                "value" : 65
              } ,
              {
                "label": "Saídas",
                "value" : 35
              }
        ]
      )
      .transition().duration(1200)
        .call(chart);

  return chart;
});