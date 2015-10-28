nv.addGraph(function() {
  var chart = nv.models.pieChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .showLabels(true);

    d3.select("#chart-pie-1 svg")
        .datum( [
              {
                "label": "Vendas",
                "value" : 85
              } ,
              {
                "label": "Impostos",
                "value" : 15
              }
        ]
      )
      .transition().duration(1200)
        .call(chart);

  return chart;
});