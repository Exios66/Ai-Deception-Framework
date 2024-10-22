document.addEventListener('DOMContentLoaded', function() {
    const modelUploadForm = document.getElementById('model-upload-form');
    const contentInput = document.getElementById('content-input');
    const detectDeceptionBtn = document.getElementById('detect-deception');
    const analysisResults = document.getElementById('analysis-results');
    const detectionResults = document.getElementById('detection-results');
    const metricsContainer = document.getElementById('metrics-container');

    modelUploadForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(this);
        fetch('/api/analyze-model', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            analysisResults.innerHTML = `<h3>Analysis Results:</h3><pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error('Error:', error);
            analysisResults.innerHTML = '<p>An error occurred during analysis.</p>';
        });
    });

    detectDeceptionBtn.addEventListener('click', function() {
        const content = contentInput.value;
        fetch('/api/detect-deception', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ content: content })
        })
        .then(response => response.json())
        .then(data => {
            detectionResults.innerHTML = `<h3>Deception Detection Results:</h3><pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error('Error:', error);
            detectionResults.innerHTML = '<p>An error occurred during deception detection.</p>';
        });
    });

    function fetchDeceptionMetrics() {
        fetch('/api/deception-metrics')
        .then(response => response.json())
        .then(data => {
            metricsContainer.innerHTML = '';
            data.forEach(metric => {
                const metricElement = document.createElement('div');
                metricElement.className = 'metric';
                metricElement.innerHTML = `
                    <h3>${metric.name}</h3>
                    <p>${metric.value}</p>
                `;
                metricsContainer.appendChild(metricElement);
            });
        })
        .catch(error => {
            console.error('Error:', error);
            metricsContainer.innerHTML = '<p>Failed to load deception metrics.</p>';
        });
    }

    // Fetch metrics on page load and every 5 minutes
    fetchDeceptionMetrics();
    setInterval(fetchDeceptionMetrics, 300000);
});

// Fetch and display features
fetch('/api/features')
    .then(response => response.json())
    .then(features => {
        // Display features on the page
    });
