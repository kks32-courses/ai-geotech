#!/usr/bin/env python3
"""Generate figures for MLP slides from consolidation notebook"""

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim

torch.manual_seed(42)
np.random.seed(42)

plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Parameters
S_final = 100.0
alpha = 0.5

# Field measurements
t_measured = np.array([0, 0.5, 1, 1.5, 2, 3, 4, 6, 8, 10])
S_true = S_final * (1 - np.exp(-alpha * t_measured))
S_measured = S_true + np.random.normal(0, 1.5, len(t_measured))
S_measured = np.maximum(S_measured, 0)

# Dense evaluation
t_dense = np.linspace(0, 10, 200)
S_dense = S_final * (1 - np.exp(-alpha * t_dense))

# Convert to tensors
T_train = torch.FloatTensor(t_measured.reshape(-1, 1))
S_train = torch.FloatTensor(S_measured.reshape(-1, 1))
T_eval = torch.FloatTensor(t_dense.reshape(-1, 1))

print("Generating figures...")

# Figure 1: Field data
plt.figure(figsize=(10, 6))
plt.scatter(t_measured, S_measured, s=120, color='black', label='Field measurements', zorder=5, edgecolors='white', linewidths=2)
plt.plot(t_dense, S_dense, 'k--', linewidth=2, label=r'True: $S(t) = 100(1-e^{-0.5t})$', alpha=0.7)
plt.axhline(S_final, color='gray', linestyle=':', linewidth=2, alpha=0.6)
plt.xlabel('Time (years)', fontweight='bold')
plt.ylabel('Settlement (mm)', fontweight='bold')
plt.title('1D Consolidation: Field Measurements', fontweight='bold', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.xlim(-0.5, 10.5)
plt.ylim(-5, 110)
plt.tight_layout()
plt.savefig('figs/consolidation-field-data.png', dpi=150, bbox_inches='tight')
print("✓ consolidation-field-data.png")
plt.close()

# Figure 2: Linear model failure
class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)
    def forward(self, t):
        return self.linear(t)

model_linear = LinearModel()
optimizer = optim.Adam(model_linear.parameters(), lr=0.1)
criterion = nn.MSELoss()

for epoch in range(1000):
    optimizer.zero_grad()
    S_pred = model_linear(T_train)
    loss = criterion(S_pred, S_train)
    loss.backward()
    optimizer.step()

with torch.no_grad():
    S_pred_linear = model_linear(T_eval).numpy()

plt.figure(figsize=(10, 6))
plt.scatter(t_measured, S_measured, s=120, color='black', label='Field data', zorder=5, edgecolors='white', linewidths=2)
plt.plot(t_dense, S_dense, 'k--', linewidth=2, label='True curve', alpha=0.7)
plt.plot(t_dense, S_pred_linear, 'r-', linewidth=3, label='Linear model', alpha=0.8)
plt.axhline(S_final, color='gray', linestyle=':', linewidth=2, alpha=0.6)
plt.xlabel('Time (years)', fontweight='bold')
plt.ylabel('Settlement (mm)', fontweight='bold')
plt.title('Linear Model Fails: Cannot Capture Exponential Decay', fontweight='bold', fontsize=14)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.xlim(-0.5, 10.5)
plt.ylim(-5, 110)
plt.tight_layout()
plt.savefig('figs/linear-consolidation-failure.png', dpi=150, bbox_inches='tight')
print("✓ linear-consolidation-failure.png")
plt.close()

# Figure 3: Tanh fit
class SingleLayerNN(nn.Module):
    def __init__(self, n_hidden=10):
        super().__init__()
        self.fc1 = nn.Linear(1, n_hidden)
        self.fc2 = nn.Linear(n_hidden, 1)
    def forward(self, t):
        return self.fc2(torch.tanh(self.fc1(t)))

model_tanh = SingleLayerNN(n_hidden=10)
optimizer = optim.Adam(model_tanh.parameters(), lr=0.01)

for epoch in range(2000):
    optimizer.zero_grad()
    S_pred = model_tanh(T_train)
    loss = criterion(S_pred, S_train)
    loss.backward()
    optimizer.step()

with torch.no_grad():
    S_pred_tanh = model_tanh(T_eval).numpy()

plt.figure(figsize=(10, 6))
plt.scatter(t_measured, S_measured, s=120, color='black', label='Field data', zorder=5, edgecolors='white', linewidths=2)
plt.plot(t_dense, S_dense, 'k--', linewidth=2, label='True curve', alpha=0.7)
plt.plot(t_dense, S_pred_tanh, 'b-', linewidth=3, label='MLP (10 neurons, Tanh)')
plt.axhline(S_final, color='gray', linestyle=':', linewidth=2, alpha=0.6)
plt.xlabel('Time (years)', fontweight='bold')
plt.ylabel('Settlement (mm)', fontweight='bold')
plt.title('Single Layer Network with Tanh: Excellent Fit', fontweight='bold', fontsize=14)
plt.legend(fontsize=11, loc='lower right')
plt.grid(alpha=0.3)
plt.xlim(-0.5, 10.5)
plt.ylim(-5, 110)
plt.tight_layout()
plt.savefig('figs/consolidation-tanh-fit.png', dpi=150, bbox_inches='tight')
print("✓ consolidation-tanh-fit.png")
plt.close()

# Figure 4: Width comparison
widths = [1, 5, 10, 20, 50]
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
axes = axes.flatten()

for idx, w in enumerate(widths):
    model = SingleLayerNN(n_hidden=w)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    for epoch in range(2000):
        optimizer.zero_grad()
        S_pred = model(T_train)
        loss = criterion(S_pred, S_train)
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        S_pred = model(T_eval).numpy()

    ax = axes[idx]
    ax.scatter(t_measured, S_measured, s=80, color='black', label='Data', zorder=5, edgecolors='white', linewidths=1.5)
    ax.plot(t_dense, S_dense, 'k--', linewidth=2, label='True', alpha=0.7)
    ax.plot(t_dense, S_pred, 'b-', linewidth=2, label='MLP')
    ax.axhline(S_final, color='gray', linestyle=':', linewidth=1, alpha=0.6)
    ax.set_title(f'{w} neurons (MSE: {np.mean((S_pred - S_dense.reshape(-1,1))**2):.2f})', fontweight='bold')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Settlement (mm)')
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3)
    ax.set_xlim(-0.5, 10.5)
    ax.set_ylim(-5, 110)

axes[-1].axis('off')
plt.suptitle('Network Width Comparison', fontweight='bold', fontsize=16)
plt.tight_layout()
plt.savefig('figs/consolidation-width-comparison.png', dpi=150, bbox_inches='tight')
print("✓ consolidation-width-comparison.png")
plt.close()

# Figure 5: Activation comparison
class MLPActivation(nn.Module):
    def __init__(self, activation='tanh', n_hidden=32):
        super().__init__()
        self.fc1 = nn.Linear(1, n_hidden)
        self.fc2 = nn.Linear(n_hidden, n_hidden)
        self.fc3 = nn.Linear(n_hidden, 1)
        if activation == 'relu':
            self.act = nn.ReLU()
        elif activation == 'tanh':
            self.act = nn.Tanh()
        elif activation == 'sigmoid':
            self.act = nn.Sigmoid()
    def forward(self, t):
        t = self.act(self.fc1(t))
        t = self.act(self.fc2(t))
        return self.fc3(t)

activations = ['relu', 'tanh', 'sigmoid']
colors = {'relu': 'red', 'tanh': 'blue', 'sigmoid': 'green'}
results = {}

for act in activations:
    model = MLPActivation(activation=act, n_hidden=32)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    for epoch in range(3000):
        optimizer.zero_grad()
        S_pred = model(T_train)
        loss = criterion(S_pred, S_train)
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        S_pred = model(T_eval).numpy()
    results[act] = S_pred

plt.figure(figsize=(12, 6))
plt.scatter(t_measured, S_measured, s=120, color='black', label='Field data', zorder=5, edgecolors='white', linewidths=2)
plt.plot(t_dense, S_dense, 'k--', linewidth=2, label='True curve', alpha=0.7)
for act in activations:
    mse = np.mean((results[act] - S_dense.reshape(-1,1))**2)
    plt.plot(t_dense, results[act], color=colors[act], linewidth=2.5,
             label=f'{act.upper()} (MSE={mse:.1f})', alpha=0.8)
plt.axhline(S_final, color='gray', linestyle=':', linewidth=2, alpha=0.6)
plt.xlabel('Time (years)', fontweight='bold')
plt.ylabel('Settlement (mm)', fontweight='bold')
plt.title('Activation Function Comparison: Tanh Best for Bounded Problems', fontweight='bold', fontsize=14)
plt.legend(fontsize=11, loc='lower right')
plt.grid(alpha=0.3)
plt.xlim(-0.5, 10.5)
plt.ylim(-5, 110)
plt.tight_layout()
plt.savefig('figs/consolidation-activation-comparison.png', dpi=150, bbox_inches='tight')
print("✓ consolidation-activation-comparison.png")
plt.close()

# Figure 6: Optimizers
def train_optimizer(opt_name, lr=0.01, epochs=2000):
    model = MLPActivation('tanh', n_hidden=16)
    if opt_name == 'SGD':
        optimizer = optim.SGD(model.parameters(), lr=lr)
    elif opt_name == 'Momentum':
        optimizer = optim.SGD(model.parameters(), lr=lr, momentum=0.9)
    elif opt_name == 'Adam':
        optimizer = optim.Adam(model.parameters(), lr=lr)

    losses = []
    for epoch in range(epochs):
        optimizer.zero_grad()
        S_pred = model(T_train)
        loss = criterion(S_pred, S_train)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())

    with torch.no_grad():
        S_pred = model(T_eval).numpy()
    return losses, S_pred

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
optimizers = ['SGD', 'Momentum', 'Adam']
colors_opt = {'SGD': 'red', 'Momentum': 'blue', 'Adam': 'green'}
opt_results = {}

for opt in optimizers:
    losses, S_pred = train_optimizer(opt)
    opt_results[opt] = {'losses': losses, 'pred': S_pred}

# Predictions
ax1.scatter(t_measured, S_measured, s=120, color='black', label='Field data', zorder=5, edgecolors='white', linewidths=2)
ax1.plot(t_dense, S_dense, 'k--', linewidth=2, label='True curve', alpha=0.7)
for opt in optimizers:
    ax1.plot(t_dense, opt_results[opt]['pred'], color=colors_opt[opt], linewidth=2, label=opt, alpha=0.8)
ax1.axhline(S_final, color='gray', linestyle=':', linewidth=2, alpha=0.6)
ax1.set_xlabel('Time (years)', fontweight='bold')
ax1.set_ylabel('Settlement (mm)', fontweight='bold')
ax1.set_title('Predictions: All Converge', fontweight='bold')
ax1.legend()
ax1.grid(alpha=0.3)
ax1.set_xlim(-0.5, 10.5)
ax1.set_ylim(-5, 110)

# Loss curves
for opt in optimizers:
    ax2.plot(opt_results[opt]['losses'], color=colors_opt[opt], linewidth=2, label=opt, alpha=0.7)
ax2.set_xlabel('Epoch', fontweight='bold')
ax2.set_ylabel('Loss (MSE)', fontweight='bold')
ax2.set_title('Training Loss: Adam Fastest', fontweight='bold')
ax2.set_yscale('log')
ax2.legend()
ax2.grid(alpha=0.3)

plt.suptitle('Optimizer Comparison: SGD vs Momentum vs Adam', fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig('figs/consolidation-optimizers.png', dpi=150, bbox_inches='tight')
print("✓ consolidation-optimizers.png")
plt.close()

# Figure 7: Shallow vs Deep
class DeepNN(nn.Module):
    def __init__(self, n_hidden=16):
        super().__init__()
        self.fc1 = nn.Linear(1, n_hidden)
        self.fc2 = nn.Linear(n_hidden, n_hidden)
        self.fc3 = nn.Linear(n_hidden, 1)
    def forward(self, t):
        t = torch.tanh(self.fc1(t))
        t = torch.tanh(self.fc2(t))
        return self.fc3(t)

model_shallow = SingleLayerNN(n_hidden=10)
model_deep = DeepNN(n_hidden=16)

for model in [model_shallow, model_deep]:
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    for epoch in range(2000):
        optimizer.zero_grad()
        S_pred = model(T_train)
        loss = criterion(S_pred, S_train)
        loss.backward()
        optimizer.step()

with torch.no_grad():
    S_shallow = model_shallow(T_eval).numpy()
    S_deep = model_deep(T_eval).numpy()

plt.figure(figsize=(12, 6))
plt.scatter(t_measured, S_measured, s=120, color='black', label='Field data', zorder=5, edgecolors='white', linewidths=2)
plt.plot(t_dense, S_dense, 'k--', linewidth=2, label='True curve', alpha=0.7)
plt.plot(t_dense, S_shallow, 'b-', linewidth=2, label='Shallow (1 layer, 10 neurons)', alpha=0.7)
plt.plot(t_dense, S_deep, 'g-', linewidth=2.5, label='Deep (2 layers, 16-16)')
plt.axhline(S_final, color='gray', linestyle=':', linewidth=2, alpha=0.6)
plt.xlabel('Time (years)', fontweight='bold')
plt.ylabel('Settlement (mm)', fontweight='bold')
plt.title('Shallow vs Deep Networks: Both Work for Smooth Functions', fontweight='bold', fontsize=14)
plt.legend(fontsize=11, loc='lower right')
plt.grid(alpha=0.3)
plt.xlim(-0.5, 10.5)
plt.ylim(-5, 110)
plt.tight_layout()
plt.savefig('figs/consolidation-shallow-deep.png', dpi=150, bbox_inches='tight')
print("✓ consolidation-shallow-deep.png")
plt.close()

print("\n✅ All figures generated successfully!")
