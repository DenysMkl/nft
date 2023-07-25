const ctx = document.getElementById('price-of-goods');
const gradient = ctx.getContext('2d').createLinearGradient(0, 0, 400, 0);
gradient.addColorStop(0, '#C2D1DD');
gradient.addColorStop(1, '#456DA2'); 

scaleConfig = {
    border: {
        color: '#111E26'
    },
    grid: {
        color: '#111E26'
    }
}

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      datasets: [{
        
        data: [12, 19, 13, 15, 12, 13, 10, 12, 5, 16, 12, 11],
        borderColor: gradient,
        borderWidth: 1,
        tension: 0.4,
        pointStyle: 'circle',
        pointBackgroundColor: 'black',
        pointHoverBackgroundColor: gradient,
        pointHoverRadius: 5,
        
      }]
    },
    options: {
        scales:{
            x: scaleConfig,
            y: scaleConfig,
        },
        plugins: {
            legend: {
                display: false
            }
        },

    }
    
    
    
  });
