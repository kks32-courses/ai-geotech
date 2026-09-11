# Gradient Descent

## The update rule

Gradient descent minimizes $f$ by repeating

$$x_{k+1} = x_k - \eta \, f'(x_k),$$

where $\eta > 0$ is the learning rate. The step moves against the derivative, so it goes downhill whenever $f'(x_k) \neq 0$. The iteration stops moving where $f'(x) = 0$. That is a stationary point, and it can be a minimum, a maximum, or a saddle.

Stochastic gradient descent replaces $f'(x_k)$ with the gradient of the loss on a random subset of the data. The demo on this page uses the exact derivative of a fixed one-dimensional function, so it runs plain gradient descent with no sampling and no randomness.

## Choosing the learning rate

Near a minimum $x_{\min}$ the derivative is close to linear, $f'(x) \approx f''(x_{\min})(x - x_{\min})$. Substituting into the update gives

$$x_{k+1} - x_{\min} \approx \big(1 - \eta f''(x_{\min})\big)\,(x_k - x_{\min}).$$

The distance to the minimum shrinks when $|1 - \eta f''(x_{\min})| < 1$, which holds when

$$0 < \eta < \frac{2}{f''(x_{\min})} .$$

Below $1/f''(x_{\min})$ the iterate approaches from one side. Between $1/f''(x_{\min})$ and $2/f''(x_{\min})$ it alternates sides and still converges. Above $2/f''(x_{\min})$ the distance grows every step and the iterate leaves that minimum. The bound depends on the curvature at the minimum, so a rate that is stable at one minimum of the same function can be unstable at another.

## The function in the demo

The demo minimizes

$$f(x) = x^4 - 6x^2 + 3x, \qquad f'(x) = 4x^3 - 12x + 3, \qquad f''(x) = 12x^2 - 12 .$$

Setting $f'(x) = 0$ gives three stationary points. The global minimum is at $x = -1.8456$ with $f = -14.37$. The local minimum is at $x = 1.5901$ with $f = -4.01$. A maximum sits between them at $x = 0.2556$. The two stability limits are

$$\frac{2}{f''(-1.8456)} = \frac{2}{28.88} = 0.069, \qquad \frac{2}{f''(1.5901)} = \frac{2}{18.34} = 0.109 .$$

All three panels start at $x_0 = 2.5$, which is inside the basin of the local minimum. Panel 1 runs 15 steps, panel 2 runs 50, and panel 3 runs 20.

## Animation

<script src="https://cdn.plot.ly/plotly-3.0.1.min.js"></script>

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
    .gd-plot-note { 
        font-size: 13px; 
        color: #555; 
        padding: 6px 10px 0 10px; 
        line-height: 1.4; 
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

<div id="gradient-descent-container">
    <p>Three learning rates on f(x) = x⁴ - 6x² + 3x, all starting from x₀ = 2.5. The updates are deterministic full-batch gradient descent, not stochastic.</p>

    <div class="gd-controls">
        <button id="gd-startButton" class="gd-button">Start Animation</button>
        <button id="gd-resetButton" class="gd-button">Reset</button>
    </div>

    <div id="gd-statusMessage"></div>

    <div class="gd-container">
        <div class="gd-plot-container">
            <div class="gd-plot-title">1. Oscillating (LR = 0.14)</div>
            <div class="gd-plot-note">0.14 is above the 0.109 limit at the local minimum. After 15 steps the iterate bounces between x = 1.05 and x = 1.83 around x = 1.590 and never settles.</div>
            <div id="gd-plot1"></div>
        </div>
        <div class="gd-plot-container">
            <div class="gd-plot-title">2. Too slow to converge (LR = 0.0005)</div>
            <div class="gd-plot-note">After 50 steps the iterate is at x = 1.999 with f' = 11.0. It is still descending toward the local minimum at x = 1.590, f = -4.01, and the animation ends first.</div>
            <div id="gd-plot2"></div>
        </div>
        <div class="gd-plot-container">
            <div class="gd-plot-title">3. Oscillating around the global minimum (LR = 0.07)</div>
            <div class="gd-plot-note">The first step jumps to x = 0.015 and the run crosses into the global basin. 0.07 is just above the 0.069 limit there, so the iterate cycles between x = -1.76 and x = -1.92 around x = -1.846, f = -14.37, instead of settling.</div>
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
                name: 'Too slow to converge'
            },
            scenario3: {
                initial_x: 2.5,
                learning_rate: 0.07,
                iterations: 20,
                plotId: 'gd-plot3',
                name: 'Oscillating around the global minimum'
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
                document.getElementById('gd-statusMessage').textContent = 'Gradient descent complete!';
                return;
            }

            Object.keys(scenarios).forEach(key => {
                updatePlot(key, animationFrame);
            });

            const maxIterations = Math.max(...Object.values(histories).map(h => h.length - 1));
            document.getElementById('gd-statusMessage').textContent = 
                `Gradient descent running... Step ${animationFrame}/${maxIterations}`;

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
