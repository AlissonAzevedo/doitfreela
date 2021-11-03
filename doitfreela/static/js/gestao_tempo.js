const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['24/10', '25/10', '26/10', '27/10', '28/10', '29/10', '30/10',],
        datasets: [
            {
                label: 'Horas Executadas',
                data: [12, 19, 3, 5, 2, 3, 6],
                borderWidth: 6,
                backgroundColor: [
                    'transparent',
                    
                ],
                borderColor: [
                    'rgb(255, 0, 0)',
                ],
                tension: 0.3,
            },

            {
                label: 'Horas Esperadas',
                data: [10, 14, 3, 6, 2, 5, 2],
                borderWidth: 6,
                backgroundColor: [
                    'transparent',
                    
                ],
                borderColor: [
                    'rgb(8, 0, 255)',
                ],
                tension: 0.3,
            }

    ]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Gestão de Tempo',
            }
        }
    }
});