# Gradient Descent

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Gradient Descent Animation</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<style>
    #gradient-descent-container { 
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
        margin: 10px; 
        background-color: #f9f9f9; 
        padding: 15px;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    .gd-container { 
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
        gap: 20px; 
    }
    .gd-plot-container { 
        border: 1px solid #ddd; 
        border-radius: 8px; 
        background-color: #fff; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); 
        padding: 10px;
    }
    .gd-controls { 
        grid-column: 1 / -1; 
        padding: 20px; 
        background-color: #fff; 
        border-radius: 8px; 
        border: 1px solid #ddd; 
        display: flex; 
        flex-wrap: wrap; 
        justify-content: space-around; 
        align-items: center; 
        gap: 20px; 
        margin-bottom: 20px;
    }
    .gd-button { 
        padding: 10px 20px; 
        font-size: 16px; 
        font-weight: bold; 
        color: white; 
        background-color: #28a745; 
        border: none; 
        border-radius: 5px; 
        cursor: pointer; 
        transition: background-color 0.2s; 
    }
    .gd-button:hover { 
        background-color: #218838; 
    }
    .gd-button:disabled { 
        background-color: #6c757d; 
        cursor: not-allowed; 
    }
    .gd-plot-title { 
        text-align: center; 
        font-size: 16px; 
        font-weight: bold; 
        padding-top: 15px; 
        color: #444; 
    }
    #gd-statusMessage { 
        grid-column: 1 / -1; 
        text-align: center; 
        font-size: 18px; 
        color: #007bff; 
        font-weight: bold; 
        min-height: 25px; 
    }
</style>
</head>
<body>

<div id="gradient-descent-container">
    <h2>Gradient Descent Animation</h2>
    <p>Three scenarios showing different learning rates and their effects on convergence. Function: f(x) = x⁴ - 6x² + 3x</p>

    <div class="gd-controls">
        <button id="gd-startButton" class="gd-button">Start Animation</button>
        <button id="gd-resetButton" class="gd-button">Reset</button>
    </div>

    <div id="gd-statusMessage"></div>

    <div class="gd-container">
        <div class="gd-plot-container">
            <div class="gd-plot-title">1. Oscillating (LR = 0.14)</div>
            <div id="gd-plot1"></div>
        </div>
        <div class="gd-plot-container">
            <div class="gd-plot-title">2. Stuck in Local Minimum (LR = 0.0005)</div>
            <div id="gd-plot2"></div>
        </div>
        <div class="gd-plot-container">
            <div class="gd-plot-title">3. Converging (LR = 0.07)</div>
            <div id="gd-plot3"></div>
        </div>
    </div>
</div>

<script>
    (function() {
        // --- CONFIGURATION ---
        const scenarios = {
            scenario1: {
                initial_x: 2.5,
                learning_rate: 0.14,
                iterations: 15,
                plotId: 'gd-plot1',
                name: 'Oscillating'
            },
            scenario2: {
                initial_x: 2.5,
                learning_rate: 0.0005,
                iterations: 50,
                plotId: 'gd-plot2',
                name: 'Stuck in Local Minimum'
            },
            scenario3: {
                initial_x: 2.5,
                learning_rate: 0.07,
                iterations: 20,
                plotId: 'gd-plot3',
                name: 'Converging'
            }
        };

        // --- MATHEMATICAL FUNCTIONS ---
        function func(x) {
            return Math.pow(x, 4) - 6 * Math.pow(x, 2) + 3 * x;
        }

        function derivative(x) {
            return 4 * Math.pow(x, 3) - 12 * x + 3;
        }

        function gradientDescent(initial_x, learning_rate, iterations) {
            let x = initial_x;
            let history = [x];
            
            for (let i = 0; i < iterations; i++) {
                const gradient = derivative(x);
                x -= learning_rate * gradient;
                history.push(x);
            }
            
            return history;
        }

        // --- PLOTTING SETUP ---
        const xRange = [-3.5, 3.5];
        const plotLayout = {
            margin: { l: 40, r: 20, t: 20, b: 40 },
            xaxis: { 
                range: xRange, 
                zeroline: true, 
                zerolinewidth: 2, 
                zerolinecolor: '#ddd',
                title: 'x'
            },
            yaxis: { 
                range: [-15, 15], 
                zeroline: true, 
                zerolinewidth: 2, 
                zerolinecolor: '#ddd',
                title: 'f(x)'
            },
            showlegend: false,
            autosize: true
        };

        // --- ANIMATION STATE ---
        let isAnimating = false;
        let animationFrame = 0;
        let histories = {};
        let animationId;

        // --- PLOTTING FUNCTIONS ---
        function createFunctionCurve() {
            const x_values = [];
            const y_values = [];
            
            for (let i = 0; i <= 200; i++) {
                const x = xRange[0] + (i / 200) * (xRange[1] - xRange[0]);
                x_values.push(x);
                y_values.push(func(x));
            }
            
            return {
                x: x_values,
                y: y_values,
                mode: 'lines',
                type: 'scatter',
                line: { color: '#2196F3', width: 3 },
                name: 'Function'
            };
        }

        function createPathTrace(history, currentFrame) {
            const points = history.slice(0, currentFrame + 1);
            const x_values = points;
            const y_values = points.map(x => func(x));
            
            return {
                x: x_values,
                y: y_values,
                mode: 'lines+markers',
                type: 'scatter',
                line: { color: '#FF5722', width: 2 },
                marker: { 
                    color: '#FF5722', 
                    size: 6,
                    line: { color: '#333', width: 1 }
                },
                name: 'Path'
            };
        }

        function createCurrentPointTrace(history, currentFrame) {
            if (currentFrame >= history.length) return null;
            
            const x = history[currentFrame];
            const y = func(x);
            
            return {
                x: [x],
                y: [y],
                mode: 'markers',
                type: 'scatter',
                marker: { 
                    color: '#FF9800', 
                    size: 12,
                    line: { color: '#333', width: 2 }
                },
                name: 'Current'
            };
        }

        function updatePlot(scenarioKey, frame) {
            const scenario = scenarios[scenarioKey];
            const history = histories[scenarioKey];
            
            const traces = [createFunctionCurve()];
            
            if (frame > 0) {
                traces.push(createPathTrace(history, frame));
            }
            
            const currentPoint = createCurrentPointTrace(history, frame);
            if (currentPoint) {
                traces.push(currentPoint);
            }
            
            Plotly.react(scenario.plotId, traces, plotLayout);
        }

        function initializePlots() {
            Object.keys(scenarios).forEach(key => {
                const scenario = scenarios[key];
                histories[key] = gradientDescent(scenario.initial_x, scenario.learning_rate, scenario.iterations);
                
                const traces = [createFunctionCurve()];
                Plotly.newPlot(scenario.plotId, traces, plotLayout);
            });
        }

        function animate() {
            if (animationFrame >= Math.max(...Object.values(histories).map(h => h.length))) {
                isAnimating = false;
                document.getElementById('gd-startButton').disabled = false;
                document.getElementById('gd-statusMessage').textContent = 'SGD complete!';
                return;
            }

            Object.keys(scenarios).forEach(key => {
                updatePlot(key, animationFrame);
            });

            const maxIterations = Math.max(...Object.values(histories).map(h => h.length - 1));
            document.getElementById('gd-statusMessage').textContent = 
                `SGD running... Step ${animationFrame}/${maxIterations}`;

            animationFrame++;
            animationId = setTimeout(animate, 300);
        }

        function startAnimation() {
            if (isAnimating) return;
            
            isAnimating = true;
            animationFrame = 0;
            document.getElementById('gd-startButton').disabled = true;
            document.getElementById('gd-statusMessage').textContent = 'Starting animation...';
            
            animate();
        }

        function resetAnimation() {
            if (animationId) {
                clearTimeout(animationId);
            }
            
            isAnimating = false;
            animationFrame = 0;
            document.getElementById('gd-startButton').disabled = false;
            
            Object.keys(scenarios).forEach(key => {
                updatePlot(key, 0);
            });
        }

        // --- INITIALIZATION ---
        function init() {
            initializePlots();
            
            document.getElementById('gd-startButton').addEventListener('click', startAnimation);
            document.getElementById('gd-resetButton').addEventListener('click', resetAnimation);
            
            window.addEventListener('resize', () => {
                Object.keys(scenarios).forEach(key => {
                    const scenario = scenarios[key];
                    Plotly.relayout(scenario.plotId, { 
                        'width': document.getElementById(scenario.plotId).parentElement.clientWidth - 20 
                    });
                });
            });
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', init);
        } else {
            init();
        }
    })();
</script>

</body>
</html>