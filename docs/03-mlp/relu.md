# ReLU and the importance of non-linear transformation

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Interactive Neural Net Transformation</title>
<!-- 1. Load Plotly.js from a CDN -->
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<!-- 2. CSS for Styling the Application -->
<style>
    #interactive-nn-container { 
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
        margin: 10px; 
        background-color: #f9f9f9; 
        padding: 15px;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    .nn-container { 
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
        gap: 20px; 
    }
    .nn-plot-container { 
        border: 1px solid #ddd; 
        border-radius: 8px; 
        background-color: #fff; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); 
        padding: 10px;
    }
    .nn-controls { 
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
    .nn-slider-group { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
    }
    .nn-slider-group label { 
        font-weight: bold; 
        margin-bottom: 10px; 
        color: #333; 
    }
    .nn-slider-group input[type=range] { 
        width: 220px; 
    }
    .nn-solve-button { 
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
    .nn-solve-button:hover { 
        background-color: #218838; 
    }
    .nn-plot-title { 
        text-align: center; 
        font-size: 16px; 
        font-weight: bold; 
        padding-top: 15px; 
        color: #444; 
    }
    #nn-statusMessage { 
        grid-column: 1 / -1; 
        text-align: center; 
        font-size: 18px; 
        color: #007bff; 
        font-weight: bold; 
        min-height: 25px; 
    }
    
    /* New styles for equations */
    .nn-equations-section {
        grid-column: 1 / -1;
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    .nn-equations-header {
        padding-left: 1em;
        cursor: pointer;
        display: flex;
        align-items: center;
        background-color: #f8f9fa;
        border-radius: 8px 8px 0 0;
        transition: background-color 0.2s;
        user-select: none;
    }
    
    .nn-equations-header:hover {
        background-color: #e9ecef;
    }
    
    .nn-equations-toggle {
        width: 0;
        height: 0;
        border-left: 8px solid #495057;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        margin-right: 12px;
        transition: transform 0.3s ease;
    }
    
    .nn-equations-toggle.expanded {
        transform: rotate(90deg);
    }
    
    .nn-equations-content {
        padding: 20px;
        display: none;
    }
    
    .nn-equations-content.show {
        display: block;
    }
    
    .nn-equation {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 6px;
        padding: 15px;
        margin: 10px 0;
        font-family: 'Courier New', monospace;
        font-size: 16px;
    }
    
    .nn-equation-title {
        font-weight: bold;
        color: #495057;
        margin-bottom: 8px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }
    
    .nn-matrix-toggle {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 8px 16px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 14px;
        margin-top: 10px;
        transition: background-color 0.2s;
    }
    
    .nn-matrix-toggle:hover {
        background-color: #0056b3;
    }
    
    .nn-matrix-display {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 4px;
        padding: 15px;
        margin-top: 10px;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        display: none;
    }
    
    .nn-matrix-display.show {
        display: block;
    }
    
    .nn-matrix {
        text-align: center;
        white-space: pre-line;
    }
    
    .nn-matrix-values {
        color: #dc3545;
        font-weight: bold;
    }
</style>
</head>
<body>

<div id="interactive-nn-container">
    <h2>Interactive Transformation Demo</h2>
    <p>Adjust the sliders to see how a linear (rotation + scaling) and non-linear (ReLU) transformation can make data separable. Or, press "Solve" to see a working solution.</p>

    <!-- Controls -->
    <div class="nn-controls">
        <div class="nn-slider-group">
            <label for="nn-rotationSlider">Rotation Angle: <span id="nn-rotationValue">0</span>°</label>
            <input type="range" id="nn-rotationSlider" min="-180" max="180" value="0" step="1">
        </div>
        <div class="nn-slider-group">
            <label for="nn-scaleSlider">Scaling Factor: <span id="nn-scaleValue">1.00</span></label>
            <input type="range" id="nn-scaleSlider" min="0.5" max="3" value="1.0" step="0.05">
        </div>
        <div class="nn-slider-group">
            <label for="nn-reluSlider">ReLU Negative Slope: <span id="nn-reluValue">0.00</span></label>
            <input type="range" id="nn-reluSlider" min="0" max="1" value="1.0" step="0.01">
        </div>
        <button id="nn-solveButton" class="nn-solve-button">Solve</button>
    </div>

    <!-- Equations Section -->
    <div class="nn-equations-section">
        <div class="nn-equations-header" id="nn-equationsHeader">
            <div class="nn-equations-toggle" id="nn-equationsToggle"></div>
            <h3 style="margin: 0; color: #495057;">Mathematical Transformations</h3>
        </div>
        
        <div class="nn-equations-content" id="nn-equationsContent">
            <div class="nn-equation">
                <div class="nn-equation-title">1. Linear Transformation:</div>
                <div><strong>Y = W<sup>T</sup>X + b</strong></div>
                <div style="margin-top: 8px; font-size: 14px; color: #6c757d;">
                    Where W is the transformation matrix (rotation + scaling) and b is the bias (set to 0 here)
                </div>
                <button class="nn-matrix-toggle" id="nn-matrixToggle">Show Matrix W</button>
                <div class="nn-matrix-display" id="nn-matrixDisplay">
                    <div class="nn-matrix" id="nn-matrixContent"></div>
                </div>
            </div>
            
            <div class="nn-equation">
                <div class="nn-equation-title">2. Non-linear Transformation (Leaky ReLU):</div>
                <div><strong>Z = f(Y) = max(αY, Y)</strong></div>
                <div style="margin-top: 8px; font-size: 14px; color: #6c757d;">
                    Where α is the negative slope parameter: <span id="nn-alphaValue">1.00</span>
                </div>
                <div style="margin-top: 8px; font-size: 12px; color: #6c757d;">
                    Applied element-wise: f(y) = y if y > 0, else α × y
                </div>
            </div>
        </div>
    </div>

    <div id="nn-statusMessage"></div>

    <div class="nn-container">
        <div class="nn-plot-container">
            <div class="nn-plot-title">1. Original Data (Input Space X)</div>
            <div id="nn-plotX"></div>
        </div>
        <div class="nn-plot-container">
            <div class="nn-plot-title">2. After Linear Transform (Y = W<sup>T</sup>X)</div>
            <div id="nn-plotY"></div>
        </div>
        <div class="nn-plot-container">
            <div class="nn-plot-title">3. After Non-linearity (Z = f(Y))</div>
            <div id="nn-plotZ"></div>
        </div>
    </div>
</div>

<!-- 4. JavaScript for Interactivity -->
<script>
    (function() {
        // --- DATA DEFINITION ---
        const class0_X = [
            [-2.75, 0.27], [-3.63, 1.20], [-2.51, 1.95], [-1.85, 3.02], [-0.81, 2.54], [0.03, 3.28], 
            [1.82, 3.23], [3.37, 2.48], [4.76, 1.96], [4.74, 0.82], [3.22, 1.02], [0.38, 1.22],
            [-0.62, -0.04], [0.52, -0.44], [1.72, -0.31], [2.29, -1.63], [0.87, -1.84], [-0.87, -1.52]
        ];
        const class1_X = [
            [-5.33, 2.15], [-4.88, 3.79], [-3.99, 3.16], [-2.98, 4.30], [-1.91, 6.07], [-1.06, 4.89], 
            [0.78, 5.01], [-0.22, 6.47], [1.43, 6.11], [2.98, 4.41], [4.50, 3.61], [5.13, 4.95], [6.37, 3.01]
        ];

        // --- PLOTTING SETUP ---
        const plotLayout = {
            margin: { l: 40, r: 20, t: 20, b: 40 },
            xaxis: { range: [-15, 15], zeroline: true, zerolinewidth: 2, zerolinecolor: '#ddd' },
            yaxis: { range: [-15, 15], zeroline: true, zerolinewidth: 2, zerolinecolor: '#ddd', scaleanchor: "x", scaleratio: 1 },
            showlegend: false,
            autosize: true
        };
        const traceClass0 = { mode: 'markers', type: 'scatter', marker: { color: 'magenta', size: 8, line: { color: 'purple', width: 1.5 } } };
        const traceClass1 = { mode: 'markers', type: 'scatter', marker: { color: 'gold', size: 8, line: { color: 'orange', width: 1.5 } } };
        const unpack = (points) => ({ x: points.map(p => p[0]), y: points.map(p => p[1]) });

        // --- MATRIX DISPLAY FUNCTIONS ---
        function updateMatrixDisplay(angleDeg, scale) {
            const angleRad = angleDeg * Math.PI / 180;
            const cosT = Math.cos(angleRad);
            const sinT = Math.sin(angleRad);
            
            const w11 = (cosT * scale).toFixed(3);
            const w12 = (-sinT * scale).toFixed(3);
            const w21 = (sinT * scale).toFixed(3);
            const w22 = (cosT * scale).toFixed(3);
            
            const matrixContent = `W = ⎡ <span class="nn-matrix-values">${w11}</span>  <span class="nn-matrix-values">${w12}</span> ⎤
    ⎣ <span class="nn-matrix-values">${w21}</span>  <span class="nn-matrix-values">${w22}</span> ⎦

This combines:
• Rotation by ${angleDeg}°
• Scaling by ${scale}`;
            
            document.getElementById('nn-matrixContent').innerHTML = matrixContent;
        }

        function toggleMatrix() {
            const display = document.getElementById('nn-matrixDisplay');
            const button = document.getElementById('nn-matrixToggle');
            
            if (display.classList.contains('show')) {
                display.classList.remove('show');
                button.textContent = 'Show Matrix W';
            } else {
                display.classList.add('show');
                button.textContent = 'Hide Matrix W';
            }
        }

        function toggleEquations() {
            const content = document.getElementById('nn-equationsContent');
            const toggle = document.getElementById('nn-equationsToggle');
            
            if (content.classList.contains('show')) {
                content.classList.remove('show');
                toggle.classList.remove('expanded');
            } else {
                content.classList.add('show');
                toggle.classList.add('expanded');
            }
        }

        // --- TRANSFORMATION LOGIC ---
        function linearTransform(points, angleDeg, scale) {
            const angleRad = angleDeg * Math.PI / 180;
            const cosT = Math.cos(angleRad);
            const sinT = Math.sin(angleRad);
            return points.map(p => {
                const rotX = p[0] * cosT - p[1] * sinT;
                const rotY = p[0] * sinT + p[1] * cosT;
                return [rotX * scale, rotY * scale];
            });
        }

        function nonlinearTransform(points, slope) {
            return points.map(p => [p[0] > 0 ? p[0] : p[0] * slope, p[1] > 0 ? p[1] : p[1] * slope]);
        }

        // --- MAIN UPDATE FUNCTION ---
        function updatePlots(isSolve = false) {
            const angle = parseFloat(document.getElementById('nn-rotationSlider').value);
            const scale = parseFloat(document.getElementById('nn-scaleSlider').value);
            const slope = parseFloat(document.getElementById('nn-reluSlider').value);
            
            document.getElementById('nn-rotationValue').textContent = angle.toFixed(0);
            document.getElementById('nn-scaleValue').textContent = scale.toFixed(2);
            document.getElementById('nn-reluValue').textContent = slope.toFixed(2);
            document.getElementById('nn-alphaValue').textContent = slope.toFixed(2);

            // Update matrix display
            updateMatrixDisplay(angle, scale);

            const class0_Y = linearTransform(class0_X, angle, scale);
            const class1_Y = linearTransform(class1_X, angle, scale);
            const class0_Z = nonlinearTransform(class0_Y, slope);
            const class1_Z = nonlinearTransform(class1_Y, slope);

            Plotly.react('nn-plotY', [{ ...traceClass0, ...unpack(class0_Y) }, { ...traceClass1, ...unpack(class1_Y) }], plotLayout);
            
            const plotZ_data = [{ ...traceClass0, ...unpack(class0_Z) }, { ...traceClass1, ...unpack(class1_Z) }];
            
            if (isSolve) {
                // --- MODIFIED SECTION: Create a scaled diagonal line ---
                const line_p1_base = [0, 5.2];
                const line_p2_base = [5, 0];

                // Scale the line's endpoints by the current scaling factor
                const line_p1_scaled = [line_p1_base[0] * scale, line_p1_base[1] * scale];
                const line_p2_scaled = [line_p2_base[0] * scale, line_p2_base[1] * scale];

                const separatingLine = {
                    x: [line_p1_scaled[0], line_p2_scaled[0]],
                    y: [line_p1_scaled[1], line_p2_scaled[1]],
                    mode: 'lines',
                    type: 'scatter',
                    line: { color: 'blue', width: 3, dash: 'dash' }
                };
                // --- END OF MODIFIED SECTION ---

                plotZ_data.push(separatingLine);
                document.getElementById('nn-statusMessage').textContent = 'Solved! The data is now linearly separable.';
            } else {
                document.getElementById('nn-statusMessage').textContent = '';
            }
            
            Plotly.react('nn-plotZ', plotZ_data, plotLayout);
        }

        // --- SOLVE FUNCTION ---
        function solve() {
            const optimalAngle = -59;
            const optimalScale = 2.0;
            const optimalSlope = 0.0;

            document.getElementById('nn-rotationSlider').value = optimalAngle;
            document.getElementById('nn-scaleSlider').value = optimalScale;
            document.getElementById('nn-reluSlider').value = optimalSlope;
            
            updatePlots(true);
        }

        // --- INITIALIZATION ---
        function init() {
            Plotly.newPlot('nn-plotX', [{ ...traceClass0, ...unpack(class0_X) }, { ...traceClass1, ...unpack(class1_X) }], plotLayout);
            
            document.getElementById('nn-rotationSlider').addEventListener('input', () => updatePlots(false));
            document.getElementById('nn-scaleSlider').addEventListener('input', () => updatePlots(false));
            document.getElementById('nn-reluSlider').addEventListener('input', () => updatePlots(false));
            document.getElementById('nn-solveButton').addEventListener('click', solve);
            document.getElementById('nn-matrixToggle').addEventListener('click', toggleMatrix);
            document.getElementById('nn-equationsHeader').addEventListener('click', toggleEquations);
            
            window.addEventListener('resize', () => {
                Plotly.relayout('nn-plotX', { 'width': document.getElementById('nn-plotX').parentElement.clientWidth - 20 });
                Plotly.relayout('nn-plotY', { 'width': document.getElementById('nn-plotY').parentElement.clientWidth - 20 });
                Plotly.relayout('nn-plotZ', { 'width': document.getElementById('nn-plotZ').parentElement.clientWidth - 20 });
            });

            updatePlots(false);
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