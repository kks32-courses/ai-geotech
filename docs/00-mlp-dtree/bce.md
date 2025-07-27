# Binary Cross Entropy Loss

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Interactive Binary Cross Entropy Loss Demo</title>
<!-- Load Plotly.js from CDN -->
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>

<!-- CSS for Styling -->
<style>
    #bce-container { 
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
        margin: 10px; 
        background-color: #f9f9f9; 
        padding: 15px;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    .bce-grid-container { 
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
        gap: 20px; 
    }
    .bce-plot-container { 
        border: 1px solid #ddd; 
        border-radius: 8px; 
        background-color: #fff; 
        box-shadow: 0 2px 5px rgba(0,0,0,0.1); 
        padding: 10px;
    }
    .bce-controls { 
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
    .bce-slider-group { 
        display: flex; 
        flex-direction: column; 
        align-items: center; 
    }
    .bce-slider-group label { 
        font-weight: bold; 
        margin-bottom: 10px; 
        color: #333; 
    }
    .bce-slider-group input[type=range] { 
        width: 220px; 
    }
    .bce-solve-button { 
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
    .bce-solve-button:hover { 
        background-color: #218838; 
    }
    .bce-solve-button.worst { 
        background-color: #dc3545; 
    }
    .bce-solve-button.worst:hover { 
        background-color: #c82333; 
    }
    .bce-plot-title { 
        text-align: center; 
        font-size: 16px; 
        font-weight: bold; 
        padding-top: 15px; 
        color: #444; 
    }
    #bce-statusMessage { 
        grid-column: 1 / -1; 
        text-align: center; 
        font-size: 18px; 
        color: #007bff; 
        font-weight: bold; 
        min-height: 25px; 
    }
    
    /* Equations section styles */
    .bce-equations-section {
        grid-column: 1 / -1;
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    
    .bce-equations-header {
        padding: 15px;
        cursor: pointer;
        display: flex;
        align-items: center;
        background-color: #f8f9fa;
        border-radius: 8px 8px 0 0;
        transition: background-color 0.2s;
        user-select: none;
    }
    
    .bce-equations-header:hover {
        background-color: #e9ecef;
    }
    
    .bce-equations-toggle {
        width: 0;
        height: 0;
        border-left: 8px solid #495057;
        border-top: 6px solid transparent;
        border-bottom: 6px solid transparent;
        margin-right: 12px;
        transition: transform 0.3s ease;
    }
    
    .bce-equations-toggle.expanded {
        transform: rotate(90deg);
    }
    
    .bce-equations-content {
        padding: 20px;
        display: none;
    }
    
    .bce-equations-content.show {
        display: block;
    }
    
    .bce-equation {
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 6px;
        padding: 15px;
        margin: 10px 0;
        font-family: 'Courier New', monospace;
        font-size: 16px;
    }
    
    .bce-equation-title {
        font-weight: bold;
        color: #495057;
        margin-bottom: 8px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }
    
    .bce-calc-toggle {
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
    
    .bce-calc-toggle:hover {
        background-color: #0056b3;
    }
    
    .bce-calc-display {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 4px;
        padding: 15px;
        margin-top: 10px;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        display: none;
    }
    
    .bce-calc-display.show {
        display: block;
    }
    
    .bce-calc-values {
        color: #dc3545;
        font-weight: bold;
    }

    /* Transformation visualization styles */
    .bce-transform-step {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px 0;
        flex-wrap: wrap;
        gap: 15px;
    }

    .bce-step-box {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        min-width: 150px;
    }

    .bce-step-title {
        font-weight: bold;
        color: #495057;
        margin-bottom: 8px;
        font-size: 14px;
    }

    .bce-arrow {
        font-size: 24px;
        color: #6b7280;
        font-weight: bold;
    }

    .bce-data-point {
        display: inline-block;
        padding: 8px 12px;
        border-radius: 6px;
        font-weight: bold;
        color: white;
        text-align: center;
        min-width: 40px;
    }

    .bce-data-point.liquefaction {
        background-color: #dc2626;
    }

    .bce-data-point.stable {
        background-color: #059669;
    }

    .bce-prediction-display {
        background-color: #e3f2fd;
        border: 2px solid #1976d2;
        padding: 8px 12px;
        border-radius: 6px;
        font-weight: bold;
        color: #1976d2;
    }

    .bce-loss-display {
        padding: 8px 12px;
        border-radius: 6px;
        font-weight: bold;
        color: white;
        text-align: center;
    }
</style>
</head>
<body>

<div id="bce-container">
    <h2>Interactive Binary Cross Entropy Loss Demo</h2>
    <p>See how BCE loss "punishes" wrong predictions through both visual intuition and mathematical precision. The red "glow" shows punishment intensity!</p>

    <!-- Controls -->
    <div class="bce-controls">
        <div class="bce-slider-group">
            <label for="bce-confidenceSlider">Model Confidence: <span id="bce-confidenceValue">70</span>%</label>
            <input type="range" id="bce-confidenceSlider" min="10" max="90" value="70" step="5">
        </div>
        <button id="bce-solveButton" class="bce-solve-button">Show Optimal</button>
        <button id="bce-worstButton" class="bce-solve-button worst">Show Worst Case</button>
        <button id="bce-resetButton" class="bce-solve-button" style="background-color: #6c757d;">Reset</button>
    </div>

    <!-- Equations Section -->
    <div class="bce-equations-section">
        <div class="bce-equations-header" id="bce-equationsHeader">
            <div class="bce-equations-toggle" id="bce-equationsToggle"></div>
            <h3 style="margin: 0; color: #495057;">Mathematical Foundation: Binary Cross Entropy Loss</h3>
        </div>
        
        <div class="bce-equations-content" id="bce-equationsContent">
            <div class="bce-equation">
                <div class="bce-equation-title">1. Binary Cross Entropy Formula:</div>
                <div><strong>BCE(y, p) = -[y × log(p) + (1-y) × log(1-p)]</strong></div>
                <div style="margin-top: 8px; font-size: 14px; color: #6c757d;">
                    Where y = true label (0 or 1), p = predicted probability (0 to 1)
                </div>
                <button class="bce-calc-toggle" id="bce-calcToggle">Show Sample Calculation</button>
                <div class="bce-calc-display" id="bce-calcDisplay">
                    <div id="bce-calcContent"></div>
                </div>
            </div>
            
            <div class="bce-equation">
                <div class="bce-equation-title">2. Why This Works:</div>
                <div>• <strong>Perfect prediction:</strong> BCE = 0 when p=1 and y=1, or p=0 and y=0</div>
                <div>• <strong>Wrong confident prediction:</strong> BCE → ∞ as p→0 when y=1 (or p→1 when y=0)</div>
                <div>• <strong>Uncertainty:</strong> BCE = log(2) ≈ 0.693 when p=0.5 regardless of y</div>
                <div style="margin-top: 8px; font-size: 14px; color: #6c757d;">
                    The logarithmic penalty severely punishes confident wrong predictions, creating a strong learning signal
                </div>
            </div>
        </div>
    </div>

    <!-- Step-by-step transformation -->
    <div class="bce-equations-section">
        <div class="bce-equations-header" id="bce-transformHeader">
            <div class="bce-equations-toggle" id="bce-transformToggle"></div>
            <h3 style="margin: 0; color: #495057;">Step-by-Step: How Data Transforms into Loss</h3>
        </div>
        
        <div class="bce-equations-content" id="bce-transformContent">
            <div class="bce-transform-step">
                <div class="bce-step-box">
                    <div class="bce-step-title">Raw Data</div>
                    <div>Sites with known liquefaction outcomes</div>
                </div>
                <span class="bce-arrow">→</span>
                <div class="bce-step-box">
                    <div class="bce-step-title">Model Predictions</div>
                    <div>Probability of liquefaction (0-1)</div>
                </div>
                <span class="bce-arrow">→</span>
                <div class="bce-step-box">
                    <div class="bce-step-title">BCE Loss</div>
                    <div>Punishment for wrong predictions</div>
                </div>
                <span class="bce-arrow">→</span>
                <div class="bce-step-box">
                    <div class="bce-step-title">Learning Signal</div>
                    <div>Gradient updates to improve model</div>
                </div>
            </div>
        </div>
    </div>

    <div id="bce-statusMessage"></div>

    <!-- Main visualization grid -->
    <div class="bce-grid-container">
        <div class="bce-plot-container">
            <div class="bce-plot-title">1. Training Data (Ground Truth)</div>
            <div id="bce-plotTruth"></div>
        </div>
        <div class="bce-plot-container">
            <div class="bce-plot-title">2. Model Predictions + Decision Boundary</div>
            <div id="bce-plotPredictions"></div>
        </div>
        <div class="bce-plot-container">
            <div class="bce-plot-title">3. Loss "Punishment" (Visual)</div>
            <div id="bce-plotLoss"></div>
        </div>
    </div>
    
    <!-- Full-width loss curves plot -->
    <div class="bce-plot-container" style="grid-column: 1 / -1;">
        <div class="bce-plot-title">4. Loss Curves (Mathematical View)</div>
        <div id="bce-plotCurves"></div>
    </div>
</div>

<!-- JavaScript for Interactivity -->
<script>
(function() {
    // Sample data points (liquefaction prediction) - positioned in 2D space
    const sampleData = [
        { id: 1, x: 2, y: 3, trueLabel: 1, name: "Site A (Loose sand)" },
        { id: 2, x: 6, y: 2, trueLabel: 1, name: "Site B (Silty sand)" },
        { id: 3, x: 1, y: 6, trueLabel: 0, name: "Site C (Dense gravel)" },
        { id: 4, x: 7, y: 5, trueLabel: 0, name: "Site D (Clay)" },
        { id: 5, x: 4, y: 4, trueLabel: 1, name: "Site E (Fine sand)" },
        { id: 6, x: 3, y: 1, trueLabel: 0, name: "Site F (Rock)" }
    ];

    // Plotting setup
    const plotLayout = {
        margin: { l: 40, r: 20, t: 20, b: 40 },
        showlegend: false,
        autosize: true
    };

    const spatialLayout = {
        ...plotLayout,
        xaxis: { title: 'Feature 1 (Soil Density)', range: [0, 8] },
        yaxis: { title: 'Feature 2 (Groundwater Level)', range: [0, 7], scaleanchor: "x", scaleratio: 1 }
    };

    // Calculate BCE loss
    function calculateBCE(trueLabel, prediction) {
        const p = Math.max(0.001, Math.min(0.999, prediction));
        return -(trueLabel * Math.log(p) + (1 - trueLabel) * Math.log(1 - p));
    }

    // Generate predictions based on confidence and mode
    function generatePredictions(confidence, mode = 'normal') {
        return sampleData.map(point => {
            let prediction;
            
            switch(mode) {
                case 'optimal':
                    // High confidence when correct
                    prediction = point.trueLabel === 1 ? 0.9 : 0.1;
                    break;
                case 'worst':
                    // High confidence when wrong
                    prediction = point.trueLabel === 1 ? 0.1 : 0.9;
                    break;
                default:
                    // Simulate based on position and confidence
                    const baseCorrect = confidence / 100;
                    const baseWrong = (100 - confidence) / 100;
                    
                    // Simple decision boundary logic: points with x > 4 tend to be predicted differently
                    if (point.x > 4) {
                        prediction = point.trueLabel === 1 ? baseCorrect : baseWrong;
                    } else {
                        prediction = point.trueLabel === 1 ? baseWrong : baseCorrect;
                    }
            }
            
            const loss = calculateBCE(point.trueLabel, prediction);
            const isCorrect = (prediction > 0.5 && point.trueLabel === 1) || 
                             (prediction < 0.5 && point.trueLabel === 0);
            
            return { ...point, prediction, loss, isCorrect };
        });
    }

    // Update calculation display
    function updateCalculation() {
        const confidence = parseFloat(document.getElementById('bce-confidenceSlider').value);
        const data = generatePredictions(confidence);
        const point = data[0]; // Use first sample for demonstration
        const p = point.prediction.toFixed(3);
        const y = point.trueLabel;
        const loss = point.loss.toFixed(3);
        
        const calculation = `Example: ${point.name}
        
y (true label) = ${y}
p (predicted prob) = ${p}

BCE = -[${y} × log(${p}) + ${1-y} × log(${(1-point.prediction).toFixed(3)})]
    = -[${y} × ${Math.log(point.prediction).toFixed(3)} + ${1-y} × ${Math.log(1-point.prediction).toFixed(3)}]
    = ${loss}

${point.isCorrect ? '✓ Correct prediction' : '✗ Wrong prediction'}
${point.loss < 0.5 ? 'Low loss' : point.loss < 1.5 ? 'Medium loss' : 'High loss'}`;
        
        document.getElementById('bce-calcContent').textContent = calculation;
    }

    // Main update function
    function updatePlots(mode = 'normal') {
        const confidence = parseFloat(document.getElementById('bce-confidenceSlider').value);
        document.getElementById('bce-confidenceValue').textContent = confidence;
        
        const processedData = generatePredictions(confidence, mode);
        const totalLoss = processedData.reduce((sum, point) => sum + point.loss, 0);
        
        // Plot 1: Ground truth (spatial)
        const truthTrace = {
            x: sampleData.map(p => p.x),
            y: sampleData.map(p => p.y),
            mode: 'markers',
            type: 'scatter',
            marker: { 
                size: 15, 
                color: sampleData.map(p => p.trueLabel ? '#dc2626' : '#059669'),
                line: { color: 'white', width: 2 }
            },
            text: sampleData.map(p => `${p.name}<br>True Label: ${p.trueLabel}`),
            hovertemplate: '%{text}<extra></extra>'
        };
        
        Plotly.react('bce-plotTruth', [truthTrace], spatialLayout);
        
        // Plot 2: Predictions with decision boundary (spatial)
        const predTrace = {
            x: processedData.map(p => p.x),
            y: processedData.map(p => p.y),
            mode: 'markers',
            type: 'scatter',
            marker: { 
                size: 15, 
                color: processedData.map(p => p.isCorrect ? '#10b981' : '#ef4444'),
                line: { color: 'white', width: 2 }
            },
            text: processedData.map(p => `${p.name}<br>Predicted: ${p.prediction.toFixed(3)}<br>${p.isCorrect ? 'Correct' : 'Wrong'}`),
            hovertemplate: '%{text}<extra></extra>'
        };
        
        // Decision boundary (simple vertical line for demonstration)
        const boundaryTrace = {
            x: [4, 4],
            y: [0, 7],
            mode: 'lines',
            type: 'scatter',
            line: { color: '#6b7280', width: 3, dash: 'dash' },
            hoverinfo: 'none'
        };
        
        // Prediction probability bars (shown as rectangles)
        const probBars = processedData.map(point => ({
            x: [point.x - 0.3, point.x + 0.3, point.x + 0.3, point.x - 0.3, point.x - 0.3],
            y: [point.y + 0.5, point.y + 0.5, point.y + 0.5 + point.prediction * 1.5, point.y + 0.5 + point.prediction * 1.5, point.y + 0.5],
            mode: 'lines',
            type: 'scatter',
            fill: 'toself',
            fillcolor: point.isCorrect ? 'rgba(16, 185, 129, 0.6)' : 'rgba(239, 68, 68, 0.6)',
            line: { color: point.isCorrect ? '#10b981' : '#ef4444', width: 2 },
            hoverinfo: 'none'
        }));
        
        Plotly.react('bce-plotPredictions', [predTrace, boundaryTrace, ...probBars], spatialLayout);
        
        // Plot 3: Loss "punishment" with glow effect (spatial)
        const lossTrace = {
            x: processedData.map(p => p.x),
            y: processedData.map(p => p.y),
            mode: 'markers',
            type: 'scatter',
            marker: { 
                size: 15,
                color: processedData.map(p => p.trueLabel ? '#dc2626' : '#059669'),
                line: { color: 'white', width: 2 }
            },
            text: processedData.map(p => `${p.name}<br>Loss: ${p.loss.toFixed(3)}<br>${p.isCorrect ? 'Correct' : 'Wrong'}`),
            hovertemplate: '%{text}<extra></extra>'
        };
        
        // Add "punishment glow" circles
        const glowTraces = processedData.map(point => ({
            x: [point.x],
            y: [point.y],
            mode: 'markers',
            type: 'scatter',
            marker: { 
                size: Math.max(20, Math.min(60, 20 + point.loss * 15)),
                color: `rgba(239, 68, 68, ${Math.min(point.loss / 3, 0.8)})`,
                line: { width: 0 }
            },
            hoverinfo: 'none'
        }));
        
        Plotly.react('bce-plotLoss', [lossTrace, ...glowTraces], spatialLayout);
        
        // Plot 4: Loss curves (mathematical view)
        const probRange = Array.from({length: 100}, (_, i) => (i + 1) / 100);
        const lossWhenY1 = probRange.map(p => calculateBCE(1, p));
        const lossWhenY0 = probRange.map(p => calculateBCE(0, p));
        
        const curve1 = {
            x: probRange,
            y: lossWhenY1,
            mode: 'lines',
            type: 'scatter',
            line: { color: '#dc2626', width: 3 },
            name: 'y = 1 (Liquefaction)'
        };
        
        const curve0 = {
            x: probRange,
            y: lossWhenY0,
            mode: 'lines',
            type: 'scatter',
            line: { color: '#059669', width: 3 },
            name: 'y = 0 (No Liquefaction)'
        };
        
        // Add current sample points
        const currentPoints = {
            x: processedData.map(p => p.prediction),
            y: processedData.map(p => p.loss),
            mode: 'markers',
            type: 'scatter',
            marker: { 
                size: 12, 
                color: processedData.map(p => p.trueLabel ? '#dc2626' : '#059669'),
                line: { color: '#fbbf24', width: 2 }
            },
            name: 'Current Samples'
        };
        
        Plotly.react('bce-plotCurves', [curve1, curve0, currentPoints], {
            ...plotLayout,
            xaxis: { title: 'Predicted Probability', range: [0, 1] },
            yaxis: { title: 'BCE Loss', range: [0, 5] },
            showlegend: true
        });
        
        // Update status message
        let statusMsg = `Total Loss: ${totalLoss.toFixed(2)}`;
        switch(mode) {
            case 'optimal':
                statusMsg += ' - Optimal! Model is confident when correct ✓';
                break;
            case 'worst':
                statusMsg += ' - Worst case! Model is confident when wrong ✗';
                break;
            default:
                statusMsg += ' - Adjust confidence to see how loss changes';
        }
        
        document.getElementById('bce-statusMessage').textContent = statusMsg;
        updateCalculation();
    }

    // Toggle functions
    function toggleCalculation() {
        const display = document.getElementById('bce-calcDisplay');
        const button = document.getElementById('bce-calcToggle');
        
        if (display.classList.contains('show')) {
            display.classList.remove('show');
            button.textContent = 'Show Sample Calculation';
        } else {
            display.classList.add('show');
            button.textContent = 'Hide Calculation';
        }
    }

    function toggleEquations() {
        const content = document.getElementById('bce-equationsContent');
        const toggle = document.getElementById('bce-equationsToggle');
        
        if (content.classList.contains('show')) {
            content.classList.remove('show');
            toggle.classList.remove('expanded');
        } else {
            content.classList.add('show');
            toggle.classList.add('expanded');
        }
    }

    function toggleTransform() {
        const content = document.getElementById('bce-transformContent');
        const toggle = document.getElementById('bce-transformToggle');
        
        if (content.classList.contains('show')) {
            content.classList.remove('show');
            toggle.classList.remove('expanded');
        } else {
            content.classList.add('show');
            toggle.classList.add('expanded');
        }
    }

    // Button handlers
    function showOptimal() { updatePlots('optimal'); }
    function showWorst() { updatePlots('worst'); }
    function reset() { updatePlots('normal'); }

    // Initialization
    function init() {
        document.getElementById('bce-confidenceSlider').addEventListener('input', () => updatePlots('normal'));
        document.getElementById('bce-solveButton').addEventListener('click', showOptimal);
        document.getElementById('bce-worstButton').addEventListener('click', showWorst);
        document.getElementById('bce-resetButton').addEventListener('click', reset);
        document.getElementById('bce-calcToggle').addEventListener('click', toggleCalculation);
        document.getElementById('bce-equationsHeader').addEventListener('click', toggleEquations);
        document.getElementById('bce-transformHeader').addEventListener('click', toggleTransform);
        
        updatePlots('normal');
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