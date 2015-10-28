nv.addGraph(function() {
  var chart = nv.models.pieChart()
      .x(function(d) { return d.label })
      .y(function(d) { return d.value })
      .showLabels(true);

    d3.select("#chart-pie-2 svg")
        .datum( [
              {
                "label": "Compras",
                "value" : 55
              } ,
              {
                "label": "Taxas",
                "value" : 15
              },
              {
                "label": "Impostos",
                "value" : 30
              }
        ]
      )
      .transition().duration(1200)
        .call(chart);

  return chart;
});