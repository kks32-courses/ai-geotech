# Universal approximation theorem

## The statement

A single hidden layer network with $N$ units computes

$$F(x) = \sum_{i=1}^{N} w_i \, \sigma(v_i^{\mathsf{T}} x + b_i) + w_0 .$$

The input is $x \in \mathbb{R}^n$. Each $v_i \in \mathbb{R}^n$ is an input weight vector and each $b_i \in \mathbb{R}$ is a bias. The function $\sigma$ is the activation, applied to one number at a time. The $w_i$ are the output weights and $w_0$ is the output bias. Every demo on this page takes $n = 1$, so $v_i^{\mathsf{T}} x$ is the ordinary product $v_i x$.

Fix a compact set $K \subset \mathbb{R}^n$, a continuous target $f: K \to \mathbb{R}$, and a tolerance $\epsilon > 0$. The theorem says that some width $N$ and some choice of $v_i$, $b_i$, $w_i$ satisfy

$$\sup_{x \in K} |F(x) - f(x)| < \epsilon .$$

The left side is the sup norm, the largest error anywhere on $K$. Compactness is a real condition and not a technicality. A ReLU network is affine outside a bounded interval, so no finite width approximates $\sin$ uniformly on all of $\mathbb{R}$.

Cybenko (1989) proved this for sigmoidal $\sigma$, meaning $\sigma(t) \to 0$ as $t \to -\infty$ and $\sigma(t) \to 1$ as $t \to +\infty$. That version does not cover ReLU, which every demo below uses. Leshno, Lin, Pinkus and Schocken (1993) give the general statement. For a locally bounded and piecewise continuous $\sigma$, the single hidden layer family is dense in $C(K)$ for every compact $K$ if and only if $\sigma$ is not a polynomial. The activation comparison at the bottom of this page shows what happens when $\sigma$ is a polynomial.

## What the theorem does not give

The theorem is an existence result. It says a set of weights exists. It does not say the network is learnable, small, or trustworthy away from the data.

- It bounds nothing about $N$. The width needed can grow without limit as $\epsilon$ shrinks, and the theorem gives no rate.
- It says nothing about training. Gradient descent starts somewhere and follows a non-convex loss. It may never reach weights that achieve $\epsilon$.
- It says nothing about generalization. Approximating a known $f$ on all of $K$ is a different problem from fitting $f$ from a finite sample of noisy points.
- It says nothing about $x$ outside $K$. A network that matches $f$ everywhere on $K$ can do anything beyond it.

[03d-mlp-extrapolation.ipynb](03d-mlp-extrapolation.ipynb) shows the last point. A ReLU network is piecewise linear with finitely many kinks, so past its largest kink the output is affine in the input. Trained on settlement data over the first two years, it predicts 519 mm at 20 years against a true asymptote of 100 mm. The theorem does not forbid this, because 20 years is outside the interval the network was fitted on.

## Building a function from ReLU units

Pick nodes $0 = x_0 < x_1 < \dots < x_N = 1$ and write $s_k = \big(f(x_{k+1}) - f(x_k)\big) / (x_{k+1} - x_k)$ for the slope of $f$ across bin $k$. The piecewise linear interpolant of $f$ at those nodes is a sum of $N$ ReLU units,

$$g(x) = f(x_0) + s_0 \, \mathrm{ReLU}(x - x_0) + \sum_{k=1}^{N-1} (s_k - s_{k-1}) \, \mathrm{ReLU}(x - x_k) ,$$

because each new unit adds a slope change of $s_k - s_{k-1}$ at the node $x_k$ and contributes nothing to its left. The demo below draws $g$ for a sine target. A sum of ReLU units is continuous and piecewise linear, so it is never a staircase. The slider sets $N$.

<div id="relu-construction">
  <canvas id="relu-steps" width="800" height="400"></canvas>
  <div class="controls">
    <label>Number of ReLU units: <span id="bumps-value">3</span>
      <input type="range" id="bumps" min="1" max="50" value="3">
    </label>
  </div>
</div>

## ReLU Network Approximation Visualization

This interactive demo shows how a neural network decomposes functions into ReLU components. The example network uses 5 ReLU neurons to approximate a cubic function.

The unit $\mathrm{ReLU}(wx + b)$ is zero on one side of $x = -b/w$ and linear on the other. That point is a kink, not an inflection point. $\mathrm{ReLU}(wx+b)$ is convex on the whole line, so its curvature never changes sign. For $w > 0$ the unit is zero to the left of the kink and rises to the right. For $w < 0$ it rises to the left and is zero to the right.

Two of the units below show both cases. $\mathrm{ReLU}(x-2)$ has $w = 1$ and $b = -2$, so its kink is at $x = 2$ and it rises to the right. $\mathrm{ReLU}(-x-1)$ has $w = -1$ and $b = -1$, so its kink is at $x = -1$ and it rises to the left.

These five weights are hand-picked, not fitted. Over $x \in [-3, 5]$ the sum misses the cubic by 15.0 in the sup norm, which is 12.5% of the target's range of 120. Turning units off shows how much each one carries.

<div id="relu-components-demo">
  <h3>Interactive ReLU Decomposition</h3>
  <div class="controls">
    <label>
      <input type="checkbox" id="show-target" checked> Target Function
    </label>
    <label>
      <input type="checkbox" id="show-component-1" checked> -20·ReLU(-x-1)
    </label>
    <label>
      <input type="checkbox" id="show-component-2" checked> 5·ReLU(x+1)
    </label>
    <label>
      <input type="checkbox" id="show-component-3" checked> -5·ReLU(x)
    </label>
    <label>
      <input type="checkbox" id="show-component-4" checked> 5·ReLU(x-2)
    </label>
    <label>
      <input type="checkbox" id="show-component-5" checked> 15·ReLU(x-3)
    </label>
    <label>
      <input type="checkbox" id="show-sum" checked> <strong>Neural Network Output</strong>
    </label>
  </div>
  <canvas id="relu-decomposition" width="800" height="500"></canvas>
  <div class="info">
    <p>Approximation Error (L∞): <span id="decomp-error">-</span></p>
  </div>
  <h3>Neural Network Architecture</h3>
  <canvas id="nn-architecture" width="1200" height="450"></canvas>
</div>




## External Visualization

[![Try Desmos Graph](https://img.shields.io/badge/Try-Desmos_Graph-orange?style=flat-square&logo=firefox&logoColor=orange)](https://www.desmos.com/calculator/6sbcqpf2cb)

<iframe src="https://www.desmos.com/calculator/6sbcqpf2cb?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>



## Activation Function Comparison

This demo compares three activations on the same target. ReLU and sigmoid are not polynomials, so widening the layer drives the error down. The parabolic activation $\sigma(z) = z^2$ is a polynomial, and widening the layer buys nothing.

The reason is an identity. Expanding one unit gives $w_i (v_i x + b_i)^2 = w_i v_i^2 x^2 + 2 w_i v_i b_i x + w_i b_i^2$, so

$$\sum_{i=1}^{N} w_i (v_i x + b_i)^2 + w_0 = a x^2 + bx + c$$

for every $N$, with $a = \sum_i w_i v_i^2$, $b = 2\sum_i w_i v_i b_i$ and $c = w_0 + \sum_i w_i b_i^2$. Any $(a, b, c)$ is reachable, so a quadratic activation spans exactly the quadratics at any width. The demo draws the least-squares quadratic for this branch, and the unit slider has no effect on it.

On $[0,1]$ that fit matches $\sin(\pi x)$ with a sup-norm error of 0.049, about what 5 ReLU units achieve. On $\sin(2\pi x)$ the same fit reaches 0.941 against an amplitude of 1. The quadratic that minimizes the sup norm does better at 0.683 and is still far from zero. A ReLU sum reaches 0.049 on $\sin(2\pi x)$ with 10 units and 0.005 with 30.

<div id="activation-comparison-demo">
  <canvas id="activation-comparison" width="800" height="400"></canvas>
  <div class="controls">
    <label>Target Function:
      <select id="target-function">
        <option value="sine">sin(πx)</option>
        <option value="sine2">sin(2πx)</option>
        <option value="step">Smooth Step (tanh)</option>
        <option value="sawtooth">Triangle Wave</option>
      </select>
    </label>
    <label>Activation Type:
      <select id="activation-type">
        <option value="relu">ReLU (non-polynomial)</option>
        <option value="sigmoid">Sigmoid (non-polynomial)</option>
        <option value="parabolic">Parabolic (polynomial)</option>
      </select>
    </label>
    <label>Number of Units: <span id="units-value">5</span>
      <input type="range" id="num-units" min="2" max="30" value="5">
    </label>
  </div>
</div>

### What to watch

- **ReLU and sigmoid**: neither is a polynomial, so the family they generate is dense in $C(K)$ for every compact $K$. Raise the unit count and the reported error falls.
- **Parabolic**: a polynomial, so the family is the quadratics and nothing else. The unit slider changes nothing. Universality belongs to the network family, not to the activation on its own.

<script>
// ReLU Decomposition Visualization
document.addEventListener('DOMContentLoaded', function() {
  // First demo: ReLU decomposition
  const decompCanvas = document.getElementById('relu-decomposition');
  if (decompCanvas) {
    const ctx = decompCanvas.getContext('2d');
    
    // Set device pixel ratio for high DPI displays
    const dpr = window.devicePixelRatio || 1;
    const rect = decompCanvas.getBoundingClientRect();
    decompCanvas.width = rect.width * dpr;
    decompCanvas.height = rect.height * dpr;
    ctx.scale(dpr, dpr);
    decompCanvas.style.width = rect.width + 'px';
    decompCanvas.style.height = rect.height + 'px';
    
    // Define the target cubic function
    const targetFunc = x => x * x * x - 3 * x * x + 2 * x + 5;
    
    // ReLU function
    const relu = x => Math.max(0, x);
    
    // ReLU components with weights and biases
    // Note: ReLU(-x-1) means we need to apply ReLU to (-x-1)
    const components = [
      { weight: -20, input: x => -x - 1, label: '-20·ReLU(-x-1)', color: '#E74C3C', 
        neuronWeight: -20, neuronBias: -1, negateInput: true },
      { weight: 5, input: x => x + 1, label: '5·ReLU(x+1)', color: '#3498DB',
        neuronWeight: 5, neuronBias: 1, negateInput: false },
      { weight: -5, input: x => x, label: '-5·ReLU(x)', color: '#9B59B6',
        neuronWeight: -5, neuronBias: 0, negateInput: false },
      { weight: 5, input: x => x - 2, label: '5·ReLU(x-2)', color: '#F39C12',
        neuronWeight: 5, neuronBias: -2, negateInput: false },
      { weight: 15, input: x => x - 3, label: '15·ReLU(x-3)', color: '#1ABC9C',
        neuronWeight: 15, neuronBias: -3, negateInput: false }
    ];
    
    function drawDecomposition() {
      const canvasWidth = decompCanvas.width / dpr;
      const canvasHeight = decompCanvas.height / dpr;
      ctx.clearRect(0, 0, canvasWidth, canvasHeight);
      
      // Set up coordinate system
      const padding = 50;
      const width = canvasWidth - 2 * padding;
      const height = canvasHeight - 2 * padding;
      const xMin = -3;
      const xMax = 5;
      const yMin = -60;
      const yMax = 70;
      
      // Draw axes
      ctx.strokeStyle = '#ddd';
      ctx.lineWidth = 1;
      ctx.beginPath();
      // X-axis
      ctx.moveTo(padding, padding + height * (yMax / (yMax - yMin)));
      ctx.lineTo(padding + width, padding + height * (yMax / (yMax - yMin)));
      // Y-axis
      ctx.moveTo(padding + width * (-xMin / (xMax - xMin)), padding);
      ctx.lineTo(padding + width * (-xMin / (xMax - xMin)), padding + height);
      ctx.stroke();
      
      // Helper function to convert coordinates
      const toX = x => padding + width * ((x - xMin) / (xMax - xMin));
      const toY = y => padding + height * ((yMax - y) / (yMax - yMin));
      
      // Draw grid lines
      ctx.strokeStyle = '#f0f0f0';
      ctx.lineWidth = 0.5;
      for (let x = Math.ceil(xMin); x <= xMax; x++) {
        ctx.beginPath();
        ctx.moveTo(toX(x), padding);
        ctx.lineTo(toX(x), padding + height);
        ctx.stroke();
      }
      for (let y = -40; y <= 60; y += 20) {
        ctx.beginPath();
        ctx.moveTo(padding, toY(y));
        ctx.lineTo(padding + width, toY(y));
        ctx.stroke();
      }
      
      // Plot functions
      const numPoints = 500;
      const dx = (xMax - xMin) / numPoints;
      
      // Draw target function if checked
      if (document.getElementById('show-target').checked) {
        ctx.strokeStyle = '#2196F3';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= numPoints; i++) {
          const x = xMin + i * dx;
          const y = targetFunc(x);
          if (i === 0) ctx.moveTo(toX(x), toY(y));
          else ctx.lineTo(toX(x), toY(y));
        }
        ctx.stroke();
      }
      
      // Draw individual ReLU components
      components.forEach((comp, idx) => {
        const checkboxId = `show-component-${idx + 1}`;
        if (document.getElementById(checkboxId).checked) {
          ctx.strokeStyle = comp.color;
          ctx.lineWidth = 1.5;
          ctx.setLineDash([5, 3]);
          ctx.beginPath();
          for (let i = 0; i <= numPoints; i++) {
            const x = xMin + i * dx;
            const y = comp.weight * relu(comp.input(x));
            if (i === 0) ctx.moveTo(toX(x), toY(y));
            else ctx.lineTo(toX(x), toY(y));
          }
          ctx.stroke();
          ctx.setLineDash([]);
        }
      });
      
      // Which components are selected
      const activeComponents = [];
      components.forEach((comp, idx) => {
        const checkboxId = `show-component-${idx + 1}`;
        if (document.getElementById(checkboxId).checked) {
          activeComponents.push(comp);
        }
      });
      
      // The error of the active sum, reported whether or not the sum is drawn
      let maxError = 0;
      const drawSum = document.getElementById('show-sum').checked;
      if (drawSum) {
        ctx.strokeStyle = '#FF5722';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
      }
      for (let i = 0; i <= numPoints; i++) {
        const x = xMin + i * dx;
        let ySum = 0;
        activeComponents.forEach(comp => {
          ySum += comp.weight * relu(comp.input(x));
        });
        maxError = Math.max(maxError, Math.abs(targetFunc(x) - ySum));
        if (drawSum) {
          if (i === 0) ctx.moveTo(toX(x), toY(ySum));
          else ctx.lineTo(toX(x), toY(ySum));
        }
      }
      if (drawSum) ctx.stroke();
      document.getElementById('decomp-error').textContent = maxError.toFixed(4);
      
      // Draw legend
      ctx.font = '12px monospace';
      let legendY = 30;
      
      if (document.getElementById('show-target').checked) {
        ctx.fillStyle = '#2196F3';
        ctx.fillText('Target: x³ - 3x² + 2x + 5', padding + 10, legendY);
        legendY += 20;
      }
      
      if (document.getElementById('show-sum').checked) {
        ctx.fillStyle = '#FF5722';
        const activeCount = activeComponents.length;
        const sumLabel = activeCount === 5 ? 'Neural Network Output (All)' : 
                         activeCount > 0 ? `Partial Sum (${activeCount} neurons)` : 
                         'Neural Network Output';
        ctx.fillText(sumLabel, padding + 10, legendY);
        legendY += 20;
      }
      
      // Draw axis labels
      ctx.fillStyle = '#333';
      ctx.font = '14px monospace';
      ctx.fillText('x', padding + width - 20, toY(0) - 10);
      ctx.fillText('y', toX(0) + 10, padding + 20);
      
      // Draw x-axis tick labels
      ctx.font = '11px monospace';
      for (let x = -3; x <= 5; x++) {
        if (x !== 0) {
          ctx.fillText(x.toString(), toX(x) - 5, toY(0) + 15);
        }
      }
      
      // Draw y-axis tick labels
      for (let y = -40; y <= 60; y += 20) {
        if (y !== 0) {
          ctx.fillText(y.toString(), toX(0) - 25, toY(y) + 3);
        }
      }
    }
    
    // Function to draw neural network architecture
    function drawNeuralNetwork() {
      const nnCanvas = document.getElementById('nn-architecture');
      if (!nnCanvas) return;
      
      const nnCtx = nnCanvas.getContext('2d');
      
      // Set device pixel ratio for high DPI displays
      const dpr = window.devicePixelRatio || 1;
      const rect = nnCanvas.getBoundingClientRect();
      nnCanvas.width = rect.width * dpr;
      nnCanvas.height = rect.height * dpr;
      nnCtx.scale(dpr, dpr);
      nnCanvas.style.width = rect.width + 'px';
      nnCanvas.style.height = rect.height + 'px';
      
      nnCtx.clearRect(0, 0, rect.width, rect.height);
      
      const width = rect.width;
      const height = rect.height;
      const centerY = height / 2;
      
      // Positions
      const inputX = 150;
      const hiddenX = width / 2;
      const outputX = width - 150;
      const neuronRadius = 30;
      
      // Check which neurons are active
      const activeNeurons = [];
      components.forEach((comp, idx) => {
        const checkboxId = `show-component-${idx + 1}`;
        if (document.getElementById(checkboxId).checked) {
          activeNeurons.push({...comp, index: idx});
        }
      });
      
      // Draw input node
      nnCtx.strokeStyle = '#2C3E50';
      nnCtx.fillStyle = '#ECF0F1';
      nnCtx.lineWidth = 3;
      nnCtx.beginPath();
      nnCtx.arc(inputX, centerY, neuronRadius, 0, 2 * Math.PI);
      nnCtx.fill();
      nnCtx.stroke();
      nnCtx.fillStyle = '#2C3E50';
      nnCtx.font = 'bold 20px monospace';
      nnCtx.textAlign = 'center';
      nnCtx.textBaseline = 'middle';
      nnCtx.fillText('x', inputX, centerY);
      
      // Draw hidden neurons
      const neuronSpacing = 60;
      const startY = centerY - (activeNeurons.length - 1) * neuronSpacing / 2;
      
      activeNeurons.forEach((neuron, i) => {
        const y = startY + i * neuronSpacing;
        
        // Draw connection from input to hidden
        nnCtx.strokeStyle = neuron.color;
        nnCtx.lineWidth = 3;
        nnCtx.globalAlpha = 0.7;
        nnCtx.beginPath();
        nnCtx.moveTo(inputX + neuronRadius, centerY);
        nnCtx.lineTo(hiddenX - neuronRadius, y);
        nnCtx.stroke();
        nnCtx.globalAlpha = 1.0;
        
        // Draw weight label on input connection
        nnCtx.fillStyle = '#2C3E50';
        nnCtx.font = 'bold 14px monospace';
        nnCtx.textAlign = 'center';
        const midX = (inputX + hiddenX) / 2;
        const midY = (centerY + y) / 2;
        
        // Background for weight label
        nnCtx.fillStyle = 'white';
        nnCtx.fillRect(midX - 25, midY - 15, 50, 20);
        nnCtx.fillStyle = '#2C3E50';
        
        if (neuron.negateInput) {
          nnCtx.fillText(`w₁=-1`, midX, midY);
        } else {
          nnCtx.fillText(`w₁=1`, midX, midY);
        }
        
        // Draw hidden neuron
        nnCtx.fillStyle = neuron.color;
        nnCtx.strokeStyle = '#2C3E50';
        nnCtx.lineWidth = 3;
        nnCtx.beginPath();
        nnCtx.arc(hiddenX, y, neuronRadius, 0, 2 * Math.PI);
        nnCtx.fill();
        nnCtx.stroke();
        
        // Draw ReLU label and bias
        nnCtx.fillStyle = 'white';
        nnCtx.font = 'bold 14px monospace';
        nnCtx.textAlign = 'center';
        nnCtx.textBaseline = 'middle';
        nnCtx.fillText('ReLU', hiddenX, y - 7);
        nnCtx.font = '12px monospace';
        nnCtx.fillText(`b=${neuron.neuronBias}`, hiddenX, y + 10);
        
        // Draw connection from hidden to output
        nnCtx.strokeStyle = neuron.color;
        nnCtx.lineWidth = 3;
        nnCtx.globalAlpha = 0.7;
        nnCtx.beginPath();
        nnCtx.moveTo(hiddenX + neuronRadius, y);
        nnCtx.lineTo(outputX - neuronRadius, centerY);
        nnCtx.stroke();
        nnCtx.globalAlpha = 1.0;
        
        // Draw output weight label (using same positioning logic as w₁)
        const outMidX = (hiddenX + outputX) / 2;
        const outMidY = (y + centerY) / 2;  // Same logic as w₁: midpoint between nodes
        
        // Background for weight label
        nnCtx.fillStyle = 'white';
        nnCtx.fillRect(outMidX - 35, outMidY - 15, 70, 20);
        
        nnCtx.fillStyle = '#2C3E50';
        nnCtx.font = 'bold 14px monospace';
        nnCtx.textAlign = 'center';
        nnCtx.fillText(`w₂=${neuron.neuronWeight}`, outMidX, outMidY);
      });
      
      // Draw output node
      nnCtx.strokeStyle = '#2C3E50';
      nnCtx.fillStyle = '#E67E22';
      nnCtx.lineWidth = 3;
      nnCtx.beginPath();
      nnCtx.arc(outputX, centerY, neuronRadius, 0, 2 * Math.PI);
      nnCtx.fill();
      nnCtx.stroke();
      nnCtx.fillStyle = 'white';
      nnCtx.font = 'bold 24px monospace';
      nnCtx.textAlign = 'center';
      nnCtx.textBaseline = 'middle';
      nnCtx.fillText('Σ', outputX, centerY);
      
      // Draw labels for input and output
      nnCtx.fillStyle = '#2C3E50';
      nnCtx.font = 'bold 16px monospace';
      nnCtx.textAlign = 'center';
      nnCtx.fillText('Input', inputX, centerY + neuronRadius + 50);
      nnCtx.fillText('Hidden Layer', hiddenX, height - 110);
      nnCtx.fillText('Output', outputX, centerY + neuronRadius + 50);
      
      // Draw title
      nnCtx.fillStyle = '#2C3E50';
      nnCtx.font = 'bold 18px monospace';
      nnCtx.textAlign = 'left';
      nnCtx.fillText(`Active Neurons: ${activeNeurons.length}/5`, 30, 35);
      
      // Draw equation at the bottom
      if (activeNeurons.length > 0) {
        nnCtx.font = '14px monospace';
        nnCtx.fillStyle = '#2C3E50';
        const eqY = height - 40;
        nnCtx.fillText('f(x) = ', 30, eqY);
        let eqX = 90;
        activeNeurons.forEach((neuron, i) => {
          if (i > 0) {
            nnCtx.fillStyle = '#2C3E50';
            nnCtx.fillText(' + ', eqX, eqY);
            eqX += 25;
          }
          nnCtx.fillStyle = neuron.color;
          nnCtx.font = 'bold 14px monospace';
          let term = neuron.label;
          nnCtx.fillText(term, eqX, eqY);
          eqX += term.length * 8;
        });
      }
    }
    
    // Add event listeners to checkboxes
    ['show-target', 'show-component-1', 'show-component-2', 
     'show-component-3', 'show-component-4', 'show-component-5', 
     'show-sum'].forEach(id => {
      const elem = document.getElementById(id);
      if (elem) elem.addEventListener('change', () => {
        drawDecomposition();
        drawNeuralNetwork();
      });
    });
    
    // Initial draw
    drawDecomposition();
    drawNeuralNetwork();
  }
});

// The piecewise-linear interpolant of targetFunc at numUnits+1 equally spaced
// nodes on [0,1], written as a sum of numUnits ReLU units:
//   g(x) = f(0) + s0*ReLU(x) + sum_k (s_k - s_{k-1})*ReLU(x - k/N)
function reluInterpolant(targetFunc, numUnits) {
  const h = 1 / numUnits;
  const node = [];
  for (let k = 0; k <= numUnits; k++) node.push(targetFunc(k * h));
  const slope = [];
  for (let k = 0; k < numUnits; k++) slope.push((node[k + 1] - node[k]) / h);
  const units = [{ w: slope[0], shift: 0 }];
  for (let k = 1; k < numUnits; k++) units.push({ w: slope[k] - slope[k - 1], shift: k * h });
  const w0 = node[0];
  return x => {
    let s = w0;
    for (const u of units) s += u.w * Math.max(0, x - u.shift);
    return s;
  };
}

// Least-squares quadratic fit of targetFunc on samples+1 points of [0,1].
// This is the best a network with activation sigma(z) = z^2 can do at any width.
function bestQuadratic(targetFunc, samples) {
  let n = 0, s1 = 0, s2 = 0, s3 = 0, s4 = 0, ty = 0, txy = 0, tx2y = 0;
  for (let i = 0; i <= samples; i++) {
    const x = i / samples, y = targetFunc(x), x2 = x * x;
    n += 1; s1 += x; s2 += x2; s3 += x2 * x; s4 += x2 * x2;
    ty += y; txy += x * y; tx2y += x2 * y;
  }
  const M = [[s4, s3, s2], [s3, s2, s1], [s2, s1, n]];
  const r = [tx2y, txy, ty];
  const det = m => m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                 - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                 + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]);
  const sub = (m, col, v) => m.map((row, i) => row.map((e, j) => (j === col ? v[i] : e)));
  const D = det(M);
  const a = det(sub(M, 0, r)) / D;
  const b = det(sub(M, 1, r)) / D;
  const c = det(sub(M, 2, r)) / D;
  return x => a * x * x + b * x + c;
}

// ReLU sum demo
document.addEventListener('DOMContentLoaded', function() {
  const reluCanvas = document.getElementById('relu-steps');
  if (!reluCanvas) return;
  
  const reluCtx = reluCanvas.getContext('2d');
  
  // Set device pixel ratio for high DPI displays
  const dpr = window.devicePixelRatio || 1;
  const rect = reluCanvas.getBoundingClientRect();
  reluCanvas.width = rect.width * dpr;
  reluCanvas.height = rect.height * dpr;
  reluCtx.scale(dpr, dpr);
  reluCanvas.style.width = rect.width + 'px';
  reluCanvas.style.height = rect.height + 'px';
  
  function drawReluConstruction() {
    const canvasWidth = rect.width;
    const canvasHeight = rect.height;
    reluCtx.clearRect(0, 0, canvasWidth, canvasHeight);
    
    const numBumps = parseInt(document.getElementById('bumps').value);
    const width = canvasWidth - 100;
    const height = canvasHeight - 100;
    
    // Draw axes
    reluCtx.strokeStyle = '#ddd';
    reluCtx.lineWidth = 1;
    reluCtx.beginPath();
    reluCtx.moveTo(50, canvasHeight - 50);
    reluCtx.lineTo(canvasWidth - 50, canvasHeight - 50);
    reluCtx.moveTo(50, 50);
    reluCtx.lineTo(50, canvasHeight - 50);
    reluCtx.stroke();
    
    // Target function (sine wave)
    const targetFunc = x => Math.sin(Math.PI * x);
    
    // Draw target function
    reluCtx.strokeStyle = '#2196F3';
    reluCtx.lineWidth = 2;
    reluCtx.beginPath();
    for (let i = 0; i <= 200; i++) {
      const x = i / 200;
      const y = targetFunc(x);
      const px = 50 + x * width;
      const py = canvasHeight / 2 - y * height / 4;
      if (i === 0) reluCtx.moveTo(px, py);
      else reluCtx.lineTo(px, py);
    }
    reluCtx.stroke();
    
    // Draw the ReLU sum. It is continuous and piecewise linear.
    const approx = reluInterpolant(targetFunc, numBumps);
    reluCtx.strokeStyle = '#FF5722';
    reluCtx.lineWidth = 2;
    reluCtx.beginPath();
    let maxError = 0;
    for (let i = 0; i <= 200; i++) {
      const x = i / 200;
      const y = approx(x);
      const px = 50 + x * width;
      const py = canvasHeight / 2 - y * height / 4;
      if (i === 0) reluCtx.moveTo(px, py);
      else reluCtx.lineTo(px, py);
      maxError = Math.max(maxError, Math.abs(targetFunc(x) - y));
    }
    reluCtx.stroke();
    
    // Mark the kinks, one per ReLU unit
    reluCtx.fillStyle = '#FF5722';
    for (let k = 0; k < numBumps; k++) {
      const x = k / numBumps;
      const px = 50 + x * width;
      const py = canvasHeight / 2 - approx(x) * height / 4;
      reluCtx.beginPath();
      reluCtx.arc(px, py, 3, 0, 2 * Math.PI);
      reluCtx.fill();
    }
    
    // Legend
    reluCtx.font = '14px monospace';
    reluCtx.fillStyle = '#2196F3';
    reluCtx.fillText('Target: sin(πx)', canvasWidth - 180, 30);
    reluCtx.fillStyle = '#FF5722';
    reluCtx.fillText(`ReLU sum (${numBumps} units)`, canvasWidth - 180, 50);
    reluCtx.fillStyle = '#666';
    reluCtx.fillText(`Max Error: ${maxError.toFixed(3)}`, canvasWidth - 180, 70);
  }
  
  document.getElementById('bumps').addEventListener('input', function() {
    document.getElementById('bumps-value').textContent = this.value;
    drawReluConstruction();
  });
  
  drawReluConstruction();
});

// Activation function comparison demo
document.addEventListener('DOMContentLoaded', function() {
  const compCanvas = document.getElementById('activation-comparison');
  if (!compCanvas) return;
  
  const compCtx = compCanvas.getContext('2d');
  
  // Set device pixel ratio for high DPI displays
  const dpr = window.devicePixelRatio || 1;
  const rect = compCanvas.getBoundingClientRect();
  compCanvas.width = rect.width * dpr;
  compCanvas.height = rect.height * dpr;
  compCtx.scale(dpr, dpr);
  compCanvas.style.width = rect.width + 'px';
  compCanvas.style.height = rect.height + 'px';
  
  function drawComparison() {
    const canvasWidth = rect.width;
    const canvasHeight = rect.height;
    compCtx.clearRect(0, 0, canvasWidth, canvasHeight);
    
    const targetType = document.getElementById('target-function').value;
    const activationType = document.getElementById('activation-type').value;
    const numUnits = parseInt(document.getElementById('num-units').value);
    const width = canvasWidth - 100;
    const height = canvasHeight - 100;
    const centerY = canvasHeight / 2;
    
    // Draw axes
    compCtx.strokeStyle = '#ddd';
    compCtx.lineWidth = 1;
    compCtx.beginPath();
    compCtx.moveTo(50, canvasHeight - 50);
    compCtx.lineTo(canvasWidth - 50, canvasHeight - 50);
    compCtx.moveTo(50, 50);
    compCtx.lineTo(50, canvasHeight - 50);
    compCtx.stroke();
    
    // Draw axis labels
    compCtx.fillStyle = '#666';
    compCtx.font = '12px monospace';
    compCtx.textAlign = 'center';
    compCtx.fillText('x', canvasWidth / 2, canvasHeight - 20);
    compCtx.save();
    compCtx.translate(20, canvasHeight / 2);
    compCtx.rotate(-Math.PI / 2);
    compCtx.fillText('f(x)', 0, 0);
    compCtx.restore();
    
    // Target function based on selection
    let targetFunc;
    if (targetType === 'sine') {
      targetFunc = x => Math.sin(Math.PI * x);
    } else if (targetType === 'sine2') {
      targetFunc = x => Math.sin(2 * Math.PI * x);
    } else if (targetType === 'step') {
      // Smooth approximation of step function using tanh (continuous!)
      targetFunc = x => {
        const steepness = 50;
        return 0.5 * Math.tanh(steepness * (x - 0.3)) - 0.5 * Math.tanh(steepness * (x - 0.7));
      };
    } else if (targetType === 'sawtooth') {
      // Triangle wave (continuous sawtooth)
      targetFunc = x => {
        const period = 1;
        const t = x / period;
        const phase = t - Math.floor(t);
        return phase < 0.5 ? 4 * phase - 1 : 3 - 4 * phase;
      };
    }
    
    // Draw target function
    compCtx.strokeStyle = '#2196F3';
    compCtx.lineWidth = 3;
    compCtx.beginPath();
    for (let i = 0; i <= 200; i++) {
      const x = i / 200;
      const y = targetFunc(x);
      const px = 50 + x * width;
      const py = centerY - y * height / 3;
      if (i === 0) compCtx.moveTo(px, py);
      else compCtx.lineTo(px, py);
    }
    compCtx.stroke();
    
    // Activation functions
    const sigmoid = x => 1 / (1 + Math.exp(-x));
    const relu = x => Math.max(0, x);
    const parabolic = x => x * x;
    
    // Draw approximation based on selected activation
    compCtx.strokeStyle = '#FF5722';
    compCtx.lineWidth = 2;
    compCtx.globalAlpha = 0.8;
    compCtx.beginPath();
    
    let maxError = 0;
    let approxFunc;
    
    if (activationType === 'relu') {
      // Sum of numUnits ReLU units: the piecewise-linear interpolant
      approxFunc = reluInterpolant(targetFunc, numUnits);
    } else if (activationType === 'sigmoid') {
      // Sigmoid smooth approximation - smooth transitions between steps
      approxFunc = x => {
        let sum = 0;
        const steepness = 10 * numUnits; // Sharper transitions with more units
        for (let i = 0; i < numUnits; i++) {
          const left = i / numUnits;
          const right = (i + 1) / numUnits;
          const center = (left + right) / 2;
          const height = targetFunc(center);
          // Sigmoid "step" - smooth transition from 0 to height
          const leftSigmoid = sigmoid(steepness * (x - left));
          const rightSigmoid = sigmoid(steepness * (x - right));
          const step = leftSigmoid - rightSigmoid;
          sum += height * step;
        }
        return sum;
      };
    } else if (activationType === 'parabolic') {
      // sum_i w_i (v_i x + b_i)^2 + w_0 = a x^2 + b x + c for any width,
      // so the whole family is the quadratics. Draw the least-squares
      // quadratic on the same 201-point grid the error is measured on.
      approxFunc = bestQuadratic(targetFunc, 200);
    }
    
    // Draw approximation and compute error
    for (let i = 0; i <= 200; i++) {
      const x = i / 200;
      const y = approxFunc(x);
      const px = 50 + x * width;
      const py = centerY - y * height / 3;
      if (i === 0) compCtx.moveTo(px, py);
      else compCtx.lineTo(px, py);
      
      maxError = Math.max(maxError, Math.abs(targetFunc(x) - y));
    }
    compCtx.stroke();
    compCtx.globalAlpha = 1.0;
    
    // Legend. The sigmoid branch evaluates 2N sigmoids but collects into N+1
    // distinct units sigma(s(x - k/N)), k = 0..N, so it is an N+1 unit network.
    compCtx.font = '14px monospace';
    compCtx.fillStyle = '#2196F3';
    compCtx.fillText('Target function', canvasWidth - 220, 30);
    compCtx.fillStyle = '#FF5722';
    let approxLabel;
    if (activationType === 'relu') approxLabel = `ReLU (${numUnits} units)`;
    else if (activationType === 'sigmoid') approxLabel = `Sigmoid (${numUnits + 1} units)`;
    else approxLabel = 'Parabolic (best quadratic)';
    compCtx.fillText(approxLabel, canvasWidth - 220, 50);
    compCtx.fillStyle = '#666';
    compCtx.fillText(`Max Error: ${maxError.toFixed(3)}`, canvasWidth - 220, 70);
    
    if (activationType === 'parabolic') {
      compCtx.fillStyle = '#E74C3C';
      compCtx.font = 'bold 12px monospace';
      compCtx.fillText('Σ wᵢ(vᵢx+bᵢ)² + w₀ = ax² + bx + c, so width changes nothing', canvasWidth - 420, 90);
    }
  }
  
  document.getElementById('target-function').addEventListener('change', drawComparison);
  document.getElementById('activation-type').addEventListener('change', drawComparison);
  document.getElementById('num-units').addEventListener('input', function() {
    document.getElementById('units-value').textContent = this.value;
    drawComparison();
  });
  
  drawComparison();
});
</script>

<style>
#relu-components-demo {
  max-width: 800px;
  margin: 0 auto;
  font-family: 'Roboto Mono', monospace;
}

.controls {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
}

.controls label {
  display: inline-block;
  margin: 5px 10px;
  font-size: 14px;
}

.controls input[type="checkbox"] {
  margin-right: 5px;
}

.controls input[type="range"] {
  width: 150px;
  vertical-align: middle;
}

.controls select, .controls button {
  padding: 5px 10px;
  font-size: 14px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background: white;
  cursor: pointer;
}

.controls button:hover {
  background: #e0e0e0;
}

.plots {
  margin: 20px 0;
}

canvas {
  border: 1px solid #ddd;
  border-radius: 4px;
  display: block;
  margin: 10px auto;
  background: white;
}

#nn-architecture {
  width: 100%;
  max-width: 1200px;
  height: 450px;
  border: 2px solid #ddd;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.info {
  background: #f9f9f9;
  padding: 15px;
  border-radius: 8px;
  font-size: 14px;
  text-align: center;
}

.info p {
  margin: 5px 0;
}

.info span {
  font-weight: bold;
  color: #FF5722;
}

#relu-components-demo h3 {
  text-align: center;
  color: #333;
}

#relu-construction {
  margin: 30px 0;
}
</style>
