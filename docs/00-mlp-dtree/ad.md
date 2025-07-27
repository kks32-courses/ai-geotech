# Automatic Differentiation: Forward and Reverse-mode

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Interactive Automatic Differentiation</title>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>

<style>
    #ad-container { 
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; 
        margin: 10px; 
        background-color: #f9f9f9; 
        padding: 15px;
        border: 1px solid #ccc;
        border-radius: 8px;
    }
    
    .ad-header {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }
    
    .ad-header h2 {
        margin: 0;
        font-size: 24px;
        color: #444;
    }
    
    .ad-controls { 
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 20px;
        flex-wrap: wrap;
        padding: 15px;
        background-color: #fff;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    
    .ad-button { 
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
    
    .ad-button:hover { 
        background-color: #218838; 
    }
    
    .ad-button.active {
        background-color: #007bff;
    }
    
    .ad-button.active:hover {
        background-color: #0056b3;
    }
    
    .ad-button:disabled { 
        background-color: #6c757d; 
        cursor: not-allowed;
    }
    
    .ad-main-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        min-height: 500px;
    }
    
    .ad-graph-container {
        background-color: #fff;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
    }
    
    .ad-calculations {
        background-color: #fff;
        border-radius: 8px;
        padding: 15px;
        color: #333;
        overflow-y: auto;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border: 1px solid #ddd;
    }
    
    .calculation-step {
        margin: 10px 0;
        padding: 12px;
        background-color: #e9ecef;
        border-radius: 6px;
        color: #333;
        font-size: 14px;
        border-left: 4px solid #007bff;
        opacity: 0;
        transform: translateX(-20px);
        transition: all 0.4s ease;
    }
    
    .calculation-step.active {
        opacity: 1;
        transform: translateX(0);
    }
    
    .calculation-step.highlight {
        background-color: #d4edda;
        border-left-color: #28a745;
        font-weight: bold;
    }
    
    #ad-graph-svg {
        width: 100%;
        height: 450px;
    }
    
    .node-circle {
        stroke: #333;
        stroke-width: 2;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .node-circle.input {
        fill: #ff7f0e;
    }
    
    .node-circle.operation {
        fill: #ff7f0e;
    }
    
    .node-circle.output {
        fill: #1f77b4;
    }
    
    .node-circle.highlighted {
        stroke: #ff1744;
        stroke-width: 4;
        filter: drop-shadow(0 0 8px rgba(255, 23, 68, 0.6));
    }
    
    .node-text {
        font-size: 14px;
        font-weight: bold;
        text-anchor: middle;
        dominant-baseline: middle;
        fill: #333;
        pointer-events: none;
    }
    
    .node-value {
        font-size: 12px;
        font-weight: bold;
        fill: #333;
        pointer-events: none;
    }
    
    .edge-line {
        stroke: #333;
        stroke-width: 2;
        fill: none;
        marker-end: url(#arrowhead);
        transition: all 0.3s ease;
    }
    
    .edge-line.highlighted {
        stroke: #ff1744;
        stroke-width: 4;
        animation: pulse 1.5s infinite;
    }
    
    .edge-label {
        font-size: 11px;
        font-weight: bold;
        fill: #d73527;
        text-anchor: middle;
        dominant-baseline: middle;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.3s ease;
        background: white;
        padding: 2px 4px;
        border-radius: 3px;
    }
    
    .edge-label.visible {
        opacity: 1;
    }
    
    .edge-line.path1 {
        stroke: #ff6b35;
        stroke-width: 4;
        animation: pulse 1.5s infinite;
    }
    
    .edge-line.path2 {
        stroke: #4ecdc4;
        stroke-width: 4;
        animation: pulse 1.5s infinite;
    }
    
    .edge-label.path1 {
        fill: #ff6b35;
        opacity: 1;
    }
    
    .final-gradient-label {
        font-size: 11px;
        font-weight: bold;
        fill: #2c3e50;
        text-anchor: middle;
        dominant-baseline: middle;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .final-gradient-label.visible {
        opacity: 1;
    }
    
    @keyframes pulse {
        0% { stroke-opacity: 1; }
        50% { stroke-opacity: 0.6; }
        100% { stroke-opacity: 1; }
    }
    
    .status-message {
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        margin: 15px 0;
        padding: 10px;
        background-color: #fff;
        border-radius: 6px;
        border: 1px solid #ddd;
        color: #333;
    }
    
    .input-controls {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 15px 0;
        flex-wrap: wrap;
    }
    
    .input-group {
        display: flex;
        align-items: center;
        gap: 8px;
        background-color: #f8f9fa;
        padding: 8px 12px;
        border-radius: 6px;
        border: 1px solid #dee2e6;
        color: #333;
    }
    
    .input-group input {
        width: 60px;
        padding: 4px 8px;
        border: 1px solid #ced4da;
        border-radius: 4px;
        font-size: 14px;
        text-align: center;
    }
    
    .legend {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 15px;
        flex-wrap: wrap;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 6px;
        background-color: #f8f9fa;
        padding: 6px 10px;
        border-radius: 6px;
        border: 1px solid #dee2e6;
        color: #333;
        font-size: 12px;
    }
    
    .legend-circle {
        width: 16px;
        height: 16px;
        border-radius: 50%;
        border: 2px solid #333;
    }
    
    .mode-indicator {
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #007bff;
        margin: 10px 0;
    }
</style>
</head>
<body>

<div id="ad-container">
    <div class="ad-header">
        <h2>Interactive Automatic Differentiation</h2>
        <p>Explore forward and reverse mode AD on the function: y = x₁² + x₂</p>
    </div>

    <div class="input-controls">
        <div class="input-group">
            <label>x₁ =</label>
            <input type="number" id="x1-input" value="2" step="0.1">
        </div>
        <div class="input-group">
            <label>x₂ =</label>
            <input type="number" id="x2-input" value="3" step="0.1">
        </div>
    </div>

    <div class="ad-controls">
        <button id="forward-btn" class="ad-button active">Forward Mode</button>
        <!-- Forward mode differentiation selector -->
        <div id="forward-wrt-selector" style="display: flex; align-items: center; gap: 10px; background-color: #f8f9fa; padding: 8px 12px; border-radius: 6px; border: 1px solid #dee2e6;">
            <span style="font-weight: bold; color: #333;">Differentiate w.r.t.:</span>
            <label style="display: flex; align-items: center; gap: 5px; color: #333;">
                <input type="radio" name="forward-wrt" value="x1" checked> x₁
            </label>
            <label style="display: flex; align-items: center; gap: 5px; color: #333;">
                <input type="radio" name="forward-wrt" value="x2"> x₂
            </label>
        </div>
        <button id="reverse-btn" class="ad-button">Reverse Mode</button>        
        <button id="step-btn" class="ad-button">Next Step</button>
        <button id="reset-btn" class="ad-button">Reset</button>
        <button id="auto-btn" class="ad-button">Auto Play</button>
    </div>

    <div class="mode-indicator" id="mode-indicator">Forward Mode AD</div>
    
    <div class="status-message" id="status-message">
        Click "Next Step" to begin Forward Mode AD
    </div>

    <div class="ad-main-content">
        <div class="ad-graph-container">
            <svg id="ad-graph-svg"></svg>
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-circle" style="background: #ff7f0e;"></div>
                    <span>Input/Operation</span>
                </div>
                <div class="legend-item">
                    <div class="legend-circle" style="background: #1f77b4;"></div>
                    <span>Output</span>
                </div>
            </div>
        </div>
        
        <div class="ad-calculations">
            <h3 style="margin-top: 0; text-align: center; color: #333;">Step-by-Step Calculations</h3>
            <div id="calculation-steps"></div>
        </div>
    </div>
</div>

<script>
(function() {
    // Graph structure for y = x1^2 + x2
    const nodes = [
        { id: 'x1', x: 120, y: 350, label: 'x₁', type: 'input' },
        { id: 'x2', x: 320, y: 350, label: 'x₂', type: 'input' },
        { id: 'square', x: 120, y: 250, label: 'x₁²', type: 'operation' },
        { id: 'add', x: 220, y: 150, label: '+', type: 'operation' },
        { id: 'y', x: 220, y: 80, label: 'y', type: 'output' }
    ];

    // Forward mode edges
    const forwardEdges = [
        { from: 'x1', to: 'square', label: '' },
        { from: 'square', to: 'add', label: '' },
        { from: 'x2', to: 'add', label: '' },
        { from: 'add', to: 'y', label: '' }
    ];

    // Reverse mode edges with gradient labels
    const reverseEdges = [
        { from: 'y', to: 'add', label: '∂y/∂w₄ = 1' },
        { from: 'add', to: 'square', label: '∂w₄/∂w₃ = 1' },
        { from: 'add', to: 'x2', label: '∂w₄/∂w₂ = 1' },
        { from: 'square', to: 'x1', label: '∂w₃/∂w₁ = 2 w₁' }
    ];

    let currentMode = 'forward';
    let currentStep = 0;
    let autoInterval;
    let values = {};
    let forwardWrt = 'x1'; // which variable we're differentiating w.r.t.

    // Forward mode steps - with actual AD derivative computation
    function getForwardSteps() {
        if (forwardWrt === 'x1') {
            return [
                {
                    description: "Seed derivatives: ẇ₁ = 1, ẇ₂ = 0 (differentiating w.r.t. x₁)",
                    highlight: ['x1', 'x2'],
                    edges: [],
                    calculation: "Forward mode AD: ∂y/∂x₁\nSeed the inputs:\nw₁ = x₁ = %x1%, ẇ₁ = 1\nw₂ = x₂ = %x2%, ẇ₂ = 0",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '', add: '', y: '' },
                    derivatives: { x1: '1', x2: '0', square: '', add: '', y: '' }
                },
                {
                    description: "Compute w₃ = w₁² and ẇ₃ = 2w₁ · ẇ₁",
                    highlight: ['square'],
                    edges: ['x1-square'],
                    calculation: "Squaring operation:\nw₃ = w₁² = (%x1%)² = %v1%\nẇ₃ = (dw₃/dw₁) · (dw₁/dx₁) = 2w₁ · ẇ₁ = 2(%x1%) · 1 = %dv1_dx1%",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '', y: '' },
                    derivatives: { x1: '1', x2: '0', square: '%dv1_dx1%', add: '', y: '' }
                },
                {
                    description: "Compute w₄ = w₃ + w₂ and ẇ₄ = ẇ₃ + ẇ₂",
                    highlight: ['add'],
                    edges: ['square-add', 'x2-add'],
                    calculation: "Addition operation:\nw₄ = w₃ + w₂ = %v1% + %x2% = %y%\nẇ₄ = ẇ₃ + ẇ₂ = %dv1_dx1% + 0 = %dy_dx1%",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '' },
                    derivatives: { x1: '1', x2: '0', square: '%dv1_dx1%', add: '%dy_dx1%', y: '' }
                },
                {
                    description: "Final: y = w₄ and ẏ = ẇ₄",
                    highlight: ['y'],
                    edges: ['add-y'],
                    calculation: "Output:\ny = w₄ = %y%\nẏ = ẇ₄ = %dy_dx1%\n\nResult: ∂y/∂x₁ = %dy_dx1%",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '%y%' },
                    derivatives: { x1: '1', x2: '0', square: '%dv1_dx1%', add: '%dy_dx1%', y: '%dy_dx1%' }
                }
            ];
        } else {
            return [
                {
                    description: "Seed derivatives: ẇ₁ = 0, ẇ₂ = 1 (differentiating w.r.t. x₂)",
                    highlight: ['x1', 'x2'],
                    edges: [],
                    calculation: "Forward mode AD: ∂y/∂x₂\nSeed the inputs:\nw₁ = x₁ = %x1%, ẇ₁ = 0\nw₂ = x₂ = %x2%, ẇ₂ = 1",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '', add: '', y: '' },
                    derivatives: { x1: '0', x2: '1', square: '', add: '', y: '' }
                },
                {
                    description: "Compute w₃ = w₁² and ẇ₃ = 2w₁ · ẇ₁",
                    highlight: ['square'],
                    edges: ['x1-square'],
                    calculation: "Squaring operation:\nw₃ = w₁² = (%x1%)² = %v1%\nẇ₃ = 2w₁ · ẇ₁ = 2(%x1%) · 0 = %dv1_dx2%",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '', y: '' },
                    derivatives: { x1: '0', x2: '1', square: '%dv1_dx2%', add: '', y: '' }
                },
                {
                    description: "Compute w₄ = w₃ + w₂ and ẇ₄ = ẇ₃ + ẇ₂",
                    highlight: ['add'],
                    edges: ['square-add', 'x2-add'],
                    calculation: "Addition operation:\nw₄ = w₃ + w₂ = %v1% + %x2% = %y%\nẇ₄ = ẇ₃ + ẇ₂ = %dv1_dx2% + 1 = %dy_dx2%",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '' },
                    derivatives: { x1: '0', x2: '1', square: '%dv1_dx2%', add: '%dy_dx2%', y: '' }
                },
                {
                    description: "Final: y = w₄ and ẏ = ẇ₄",
                    highlight: ['y'],
                    edges: ['add-y'],
                    calculation: "Output:\ny = w₄ = %y%\nẏ = ẇ₄ = %dy_dx2%\n\nResult: ∂y/∂x₂ = %dy_dx2%",
                    nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '%y%' },
                    derivatives: { x1: '0', x2: '1', square: '%dv1_dx2%', add: '%dy_dx2%', y: '%dy_dx2%' }
                }
            ];
        }
    }

    // Reverse mode steps - with final chain rule visualization
    const reverseSteps = [
        {
            description: "Forward pass complete, now backward pass",
            highlight: ['y'],
            edges: [],
            calculation: "All values computed:\nw₁=%x1%, w₂=%x2%, w₃=%v1%, w₄=%y%, y=%y%\n\nStart: ∂y/∂y = 1",
            nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '%y%' }
        },
        {
            description: "∂y/∂w₄ = 1 (y = w₄)",
            highlight: ['add'],
            edges: ['y-add'],
            calculation: "∂y/∂w₄ = ∂y/∂y × ∂y/∂w₄ = 1 × 1 = 1",
            nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '%y%' }
        },
        {
            description: "∂y/∂w₃ = 1, ∂y/∂w₂ = 1 (w₄ = w₃ + w₂)",
            highlight: ['square', 'x2'],
            edges: ['add-square', 'add-x2'],
            calculation: "∂y/∂w₃ = ∂y/∂w₄ × ∂w₄/∂w₃ = 1 × 1 = 1\n∂y/∂w₂ = ∂y/∂w₄ × ∂w₄/∂w₂ = 1 × 1 = 1",
            nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '%y%' }
        },
        {
            description: "∂y/∂w₁ = 2x₁ (w₃ = w₁²)",
            highlight: ['x1'],
            edges: ['square-x1'],
            calculation: "∂y/∂w₁ = ∂y/∂w₃ × ∂w₃/∂w₁ = 1 × 2w₁ = 2(%x1%) = %dy_dx1%",
            nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '%y%' }
        },
        {
            description: "Chain rule visualization: Two gradient paths",
            highlight: ['x1', 'x2'],
            edges: [],
            edgePaths: {
                path1: ['square-x1', 'add-square', 'y-add'],
                path2: ['add-x2', 'y-add']
            },
            calculation: "Path 1 (orange): ∂y/∂w₁ = ∂y/∂w₄ × ∂w₄/∂w₃ × ∂w₃/∂w₁\n                    = 1 × 1 × 2w₁ = %dy_dx1%\n\nPath 2 (teal): ∂y/∂w₂ = ∂y/∂w₄ × ∂w₄/∂w₂\n                = 1 × 1 = 1\n\nFinal gradient: ∇y = (%dy_dx1%, 1)",
            nodeValues: { x1: '%x1%', x2: '%x2%', square: '%v1%', add: '%y%', y: '%y%' },
            showFinalGradients: true
        }
    ];

    function updateValues() {
        const x1 = parseFloat(document.getElementById('x1-input').value);
        const x2 = parseFloat(document.getElementById('x2-input').value);
        
        values = {
            x1: x1,
            x2: x2,
            v1: x1 * x1,
            y: x1 * x1 + x2,
            dy_dx1: 2 * x1,
            dy_dx2: 1,
            dv1_dx1: 2 * x1,
            dv1_dx2: 0
        };
    }

    function createGraph() {
        const svg = d3.select('#ad-graph-svg');
        svg.selectAll('*').remove();

        // Define arrow marker
        svg.append('defs').append('marker')
            .attr('id', 'arrowhead')
            .attr('viewBox', '-0 -5 10 10')
            .attr('refX', 25)
            .attr('refY', 0)
            .attr('orient', 'auto')
            .attr('markerWidth', 6)
            .attr('markerHeight', 6)
            .append('path')
            .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
            .attr('fill', '#333');

        // Draw edges based on current mode
        const edges = currentMode === 'forward' ? forwardEdges : reverseEdges;
        
        edges.forEach(edge => {
            const fromNode = nodes.find(n => n.id === edge.from);
            const toNode = nodes.find(n => n.id === edge.to);
            
            // Calculate edge endpoints
            const dx = toNode.x - fromNode.x;
            const dy = toNode.y - fromNode.y;
            const length = Math.sqrt(dx * dx + dy * dy);
            const radius = 30;
            
            const x1 = fromNode.x + (dx / length) * radius;
            const y1 = fromNode.y + (dy / length) * radius;
            const x2 = toNode.x - (dx / length) * radius;
            const y2 = toNode.y - (dy / length) * radius;
            
            const edgeGroup = svg.append('g').attr('class', `edge-group edge-${edge.from}-${edge.to}`);
            
            edgeGroup.append('line')
                .attr('class', `edge-line`)
                .attr('x1', x1)
                .attr('y1', y1)
                .attr('x2', x2)
                .attr('y2', y2);
            
            // Add edge label for reverse mode with better positioning
            if (edge.label && currentMode === 'reverse') {
                const midX = (x1 + x2) / 2;
                const midY = (y1 + y2) / 2;
                
                // Calculate perpendicular offset for better visibility
                const perpX = -(dy / length) * 25;
                const perpY = (dx / length) * 25;
                
                // Add white background rectangle for better readability
                const textElement = edgeGroup.append('text')
                    .attr('class', `edge-label edge-label-${edge.from}-${edge.to}`)
                    .attr('x', midX + perpX)
                    .attr('y', midY + perpY)
                    .text(edge.label);
                
                // Add white background
                const bbox = textElement.node().getBBox();
                edgeGroup.insert('rect', 'text')
                    .attr('x', bbox.x - 2)
                    .attr('y', bbox.y - 1)
                    .attr('width', bbox.width + 4)
                    .attr('height', bbox.height + 2)
                    .attr('fill', 'white')
                    .attr('stroke', '#ddd')
                    .attr('stroke-width', 1)
                    .attr('rx', 2)
                    .attr('class', `edge-label-bg edge-label-bg-${edge.from}-${edge.to}`)
                    .style('opacity', 0);
            }
        });

        // Draw nodes
        nodes.forEach(node => {
            const g = svg.append('g').attr('class', `node-group node-${node.id}`);
            
            g.append('circle')
                .attr('class', `node-circle ${node.type}`)
                .attr('cx', node.x)
                .attr('cy', node.y)
                .attr('r', 30);
            
            // Node label inside circle
            g.append('text')
                .attr('class', 'node-text')
                .attr('x', node.x)
                .attr('y', node.y)
                .text(node.label);
            
            // Value display next to node (function value)
            g.append('text')
                .attr('class', `node-value-display node-value-${node.id}`)
                .attr('x', node.x + 45)
                .attr('y', node.y - 5)
                .attr('font-size', '13px')
                .attr('font-weight', 'bold')
                .attr('fill', '#333')
                .text('');
                
            // Derivative display next to node (for forward mode)
            g.append('text')
                .attr('class', `node-deriv-display node-deriv-${node.id}`)
                .attr('x', node.x + 45)
                .attr('y', node.y + 10)
                .attr('font-size', '12px')
                .attr('font-weight', 'bold')
                .attr('fill', '#d73527')
                .text('');
                
            // Final gradient display below input nodes (for reverse mode final step)
            if (node.type === 'input') {
                g.append('text')
                    .attr('class', `final-gradient-label final-gradient-${node.id}`)
                    .attr('x', node.x)
                    .attr('y', node.y + 50)
                    .attr('font-size', '10px')
                    .attr('font-weight', 'bold')
                    .attr('fill', '#2c3e50')
                    .attr('text-anchor', 'middle')
                    .text('');
            }
        });
    }

    function highlightElements(elementIds, edgeIds, edgePaths) {
        // Reset all highlights
        d3.selectAll('.node-circle').classed('highlighted', false);
        d3.selectAll('.edge-line').classed('highlighted', false);
        d3.selectAll('.edge-line').classed('path1', false);
        d3.selectAll('.edge-line').classed('path2', false);
        d3.selectAll('.edge-label').classed('visible', false);
        d3.selectAll('.edge-label-bg').style('opacity', 0);
        d3.selectAll('.edge-label').classed('path1', false);
        d3.selectAll('.edge-label').classed('path2', false);

        // Highlight nodes
        elementIds.forEach(id => {
            d3.select(`.node-${id} .node-circle`).classed('highlighted', true);
        });
        
        // Handle special case of colored paths for chain rule visualization
        if (edgePaths) {
            // Path 1: x1 -> square -> add -> y (orange)
            edgePaths.path1.forEach(edgeId => {
                d3.select(`.edge-${edgeId} .edge-line`).classed('path1', true);
                d3.select(`.edge-label-${edgeId}`).classed('visible', true).classed('path1', true);
                d3.select(`.edge-label-bg-${edgeId}`).style('opacity', 1);
            });
            
            // Path 2: x2 -> add -> y (teal)
            edgePaths.path2.forEach(edgeId => {
                d3.select(`.edge-${edgeId} .edge-line`).classed('path2', true);
                d3.select(`.edge-label-${edgeId}`).classed('visible', true).classed('path2', true);
                d3.select(`.edge-label-bg-${edgeId}`).style('opacity', 1);
            });
        } else {
            // Regular edge highlighting
            edgeIds.forEach(edgeId => {
                d3.select(`.edge-${edgeId} .edge-line`).classed('highlighted', true);
                d3.select(`.edge-label-${edgeId}`).classed('visible', true);
                d3.select(`.edge-label-bg-${edgeId}`).style('opacity', 1);
            });
        }
    }

    function formatCalculation(template) {
        let result = template;
        for (const [key, value] of Object.entries(values)) {
            const regex = new RegExp(`%${key}%`, 'g');
            result = result.replace(regex, typeof value === 'number' ? value.toFixed(2) : value);
        }
        return result;
    }

    function updateNodeValues(nodeValues, derivatives, showFinalGradients) {
        const subscripts = { x1: '₁', x2: '₂', square: '₃', add: '₄', y: '' };
        
        nodes.forEach(node => {
            // Update function values
            if (nodeValues[node.id] !== undefined && nodeValues[node.id] !== '') {
                const valueText = formatCalculation(nodeValues[node.id]);
                const subscript = subscripts[node.id];
                const label = node.id === 'y' ? `y = ${valueText}` : `w${subscript} = ${valueText}`;
                d3.select(`.node-value-${node.id}`).text(label);
            } else {
                d3.select(`.node-value-${node.id}`).text('');
            }
            
            // Update derivative values (for forward mode)
            if (currentMode === 'forward' && derivatives && derivatives[node.id] !== undefined && derivatives[node.id] !== '') {
                const derivText = formatCalculation(derivatives[node.id]);
                const subscript = subscripts[node.id];
                const derivLabel = node.id === 'y' ? `ẏ = ${derivText}` : `ẇ${subscript} = ${derivText}`;
                d3.select(`.node-deriv-${node.id}`).text(derivLabel);
            } else {
                d3.select(`.node-deriv-${node.id}`).text('');
            }
        });
        
        // Show final gradient calculations for reverse mode
        if (showFinalGradients && currentMode === 'reverse') {
            // For x1 node
            const x1GradientText = `∂y/∂w₁ = ∂y/∂w₄ × ∂w₄/∂w₃ × ∂w₃/∂w₁\n= 1 × 1 × ${(2 * values.x1).toFixed(2)} = ${values.dy_dx1.toFixed(2)}`;
            d3.select('.final-gradient-x1')
                .selectAll('tspan').remove();
            
            const x1Text = d3.select('.final-gradient-x1');
            x1GradientText.split('\n').forEach((line, i) => {
                x1Text.append('tspan')
                    .attr('x', 120)
                    .attr('dy', i === 0 ? 0 : '1.2em')
                    .text(line);
            });
            
            // For x2 node  
            const x2GradientText = `∂y/∂w₂ = ∂y/∂w₄ × ∂w₄/∂w₂\n= 1 × 1 = 1`;
            d3.select('.final-gradient-x2')
                .selectAll('tspan').remove();
                
            const x2Text = d3.select('.final-gradient-x2');
            x2GradientText.split('\n').forEach((line, i) => {
                x2Text.append('tspan')
                    .attr('x', 320)
                    .attr('dy', i === 0 ? 0 : '1.2em')
                    .text(line);
            });
            
            d3.selectAll('.final-gradient-label').classed('visible', true);
        } else {
            d3.selectAll('.final-gradient-label').classed('visible', false);
            d3.selectAll('.final-gradient-label').selectAll('tspan').remove();
        }
    }

    function updateCalculationDisplay() {
        const container = document.getElementById('calculation-steps');
        const steps = currentMode === 'forward' ? getForwardSteps() : reverseSteps;
        
        container.innerHTML = '';
        
        for (let i = 0; i <= currentStep && i < steps.length; i++) {
            const stepDiv = document.createElement('div');
            stepDiv.className = 'calculation-step';
            if (i === currentStep) {
                stepDiv.classList.add('highlight');
            }
            
            const formattedCalc = formatCalculation(steps[i].calculation);
            stepDiv.innerHTML = `
                <div style="margin-bottom: 8px; font-weight: bold;">${steps[i].description}</div>
                <div style="font-family: monospace; white-space: pre-line; font-size: 13px;">${formattedCalc}</div>
            `;
            
            container.appendChild(stepDiv);
            
            // Animate in
            setTimeout(() => stepDiv.classList.add('active'), i * 50);
        }
    }

    function nextStep() {
        const steps = currentMode === 'forward' ? getForwardSteps() : reverseSteps;
        
        if (currentStep < steps.length) {
            const step = steps[currentStep];
            highlightElements(step.highlight, step.edges || [], step.edgePaths);
            updateNodeValues(step.nodeValues, step.derivatives, step.showFinalGradients);
            updateCalculationDisplay();
            currentStep++;
            
            if (currentStep >= steps.length) {
                document.getElementById('status-message').textContent = 
                    `${currentMode === 'forward' ? 'Forward' : 'Reverse'} mode complete!`;
                document.getElementById('step-btn').disabled = true;
            } else {
                document.getElementById('status-message').textContent = 
                    `Step ${currentStep} of ${steps.length}`;
            }
        }
    }

    function reset() {
        currentStep = 0;
        clearInterval(autoInterval);
        highlightElements([], []);
        
        // Clear all node values and derivatives
        nodes.forEach(node => {
            d3.select(`.node-value-${node.id}`).text('');
            d3.select(`.node-deriv-${node.id}`).text('');
        });
        
        // Clear final gradient labels
        d3.selectAll('.final-gradient-label').classed('visible', false);
        d3.selectAll('.final-gradient-label').selectAll('tspan').remove();
        
        document.getElementById('calculation-steps').innerHTML = '';
        document.getElementById('step-btn').disabled = false;
        document.getElementById('status-message').textContent = 
            `Click "Next Step" to begin ${currentMode === 'forward' ? 'Forward' : 'Reverse'} Mode AD`;
    }

    function switchMode(mode) {
        currentMode = mode;
        document.getElementById('mode-indicator').textContent = 
            `${mode === 'forward' ? 'Forward' : 'Reverse'} Mode AD`;
        
        // Show/hide forward mode selector
        const selector = document.getElementById('forward-wrt-selector');
        selector.style.display = mode === 'forward' ? 'flex' : 'none';
        
        reset();
        createGraph();
        
        document.getElementById('forward-btn').classList.toggle('active', mode === 'forward');
        document.getElementById('reverse-btn').classList.toggle('active', mode === 'reverse');
    }

    function autoPlay() {
        reset();
        // Start immediately, then continue with intervals
        setTimeout(() => {
            nextStep();
            autoInterval = setInterval(() => {
                nextStep();
                if (currentStep >= (currentMode === 'forward' ? getForwardSteps() : reverseSteps).length) {
                    clearInterval(autoInterval);
                }
            }, 1500);
        }, 100);
    }

    // Event listeners
    document.getElementById('forward-btn').addEventListener('click', () => switchMode('forward'));
    document.getElementById('reverse-btn').addEventListener('click', () => switchMode('reverse'));
    document.getElementById('step-btn').addEventListener('click', nextStep);
    document.getElementById('reset-btn').addEventListener('click', reset);
    document.getElementById('auto-btn').addEventListener('click', autoPlay);
    
    // Forward mode differentiation selector
    document.querySelectorAll('input[name="forward-wrt"]').forEach(radio => {
        radio.addEventListener('change', (e) => {
            forwardWrt = e.target.value;
            reset();
        });
    });
    
    document.getElementById('x1-input').addEventListener('input', () => {
        updateValues();
        if (currentStep > 0) {
            const steps = currentMode === 'forward' ? getForwardSteps() : reverseSteps;
            if (currentStep <= steps.length) {
                const step = steps[currentStep - 1];
                updateNodeValues(step.nodeValues, step.derivatives, step.showFinalGradients);
                updateCalculationDisplay();
            }
        }
    });
    
    document.getElementById('x2-input').addEventListener('input', () => {
        updateValues();
        if (currentStep > 0) {
            const steps = currentMode === 'forward' ? getForwardSteps() : reverseSteps;
            if (currentStep <= steps.length) {
                const step = steps[currentStep - 1];
                updateNodeValues(step.nodeValues, step.derivatives, step.showFinalGradients);
                updateCalculationDisplay();
            }
        }
    });

    // Initialize
    updateValues();
    createGraph();
    reset();
})();
</script>

</body>
</html>