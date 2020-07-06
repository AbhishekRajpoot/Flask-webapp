document.getElementById('button').addEventListener('click',
function(){
    document.querySelector('.bg-modal').style.display = 'flex';
});

document.querySelector('.close').addEventListener('click',
function(){
    document.querySelector('.bg-modal').style.display='none';
});


document.getElementById('button-addemp').addEventListener('click',
function(){
    document.querySelector('.modal-bg').style.display = 'flex';
});

document.querySelector('.s-out').addEventListener('click',
function(){
    document.querySelector('.modal-bg').style.display='none';
});



$(".alert").alert();


google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Year', 'Sales'],
          ['2004',  660 ],
          ['2005',  1100 ],
          ['2006',  660 ],
          ['2007',  1030 ],
          ['2008',  1000 ],
          ['2009',  1170 ],
          ['20010',  2222 ],
          ['2001',  1500 ],
          ['2012',  4500 ],
          ['2013',  2500 ],
          ['2014',  1500 ],
          ['2015',  1030]
        ]);

        var options = {
          title: 'Monthwise sale prediction',
          curveType: 'function',
          legend: { position: 'top-right' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

        chart.draw(data, options);
      }



google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(chart);

      function chart() {

        var data = google.visualization.arrayToDataTable([
          ['Sales', 'Sales by category'],
          ['Grocery',     11],
          ['Fashion',      2],
          ['crockery',  2],
          ['Home decor', 2],
          ['Essentials',    7]
        ]);

        var options = {
          title: 'Product sales by categories'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }