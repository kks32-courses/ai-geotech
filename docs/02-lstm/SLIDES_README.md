# LSTM Slides - Image Placeholders

The slides `lstm-slides.tex` have been created with placeholder images. To complete the presentation, add the following images to the `docs/02-lstm/` directory:

## Required Images

### 1. **liquefaction_damage.jpg**
- **Location:** Frame 3
- **Description:** Photo showing liquefaction damage during an earthquake
- **Suggested sources:**
  - USGS Earthquake Hazards Program
  - PEER (Pacific Earthquake Engineering Research Center)
  - Search: "liquefaction damage Niigata" or "liquefaction Christchurch"

### 2. **effective_stress.png**
- **Location:** Frame 4
- **Description:** Diagram showing effective stress concept and pore pressure buildup
- **Suggested sources:**
  - Geotechnical textbooks
  - Create using TikZ or search: "effective stress principle diagram"

### 3. **vanishing_gradient.png**
- **Location:** Frame 9
- **Description:** Graph showing gradient magnitude decay over time steps
- **Suggested sources:**
  - Search: "vanishing gradient problem RNN"
  - Christopher Olah's blog
  - d2l.ai Deep Learning book

### 4. **lstm_overview.png**
- **Location:** Frame 11
- **Description:** Comparison of RNN vs LSTM showing constant gradient flow
- **Suggested sources:**
  - Search: "LSTM architecture Christopher Olah"
  - URL: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
  - Analytics Vidhya LSTM tutorial

### 5. **gradient_flow.png**
- **Location:** Frame 17
- **Description:** Diagram showing how cell state acts as gradient highway
- **Suggested sources:**
  - d2l.ai LSTM chapter
  - Search: "LSTM gradient highway"

### 6. **shielding_lstm.png**
- **Location:** Frame 19
- **Description:** Plot showing how LSTM captures shielding effect
- **Note:** Generate from your notebook results after training!

### 7. **exp_data.png**
- **Location:** Frame 20
- **Description:** Sample experimental data from cyclic simple shear test
- **Note:** Generate from your notebook (sample_df visualization)

### 8. **training_history.png**
- **Location:** Frame 23
- **Description:** Training and validation loss curves
- **Note:** Generate from your notebook after training

### 9. **predictions.png**
- **Location:** Frame 24
- **Description:** LSTM predictions vs experimental measurements
- **Note:** Generate from your notebook test results

### 10. **model_comparison.png**
- **Location:** Frame 25
- **Description:** LSTM vs PM4Sand/PDMY02 comparison
- **Note:** Optional - can reference from Choi & Kumar (2023) paper

## How to Add Images

1. **Download/create images** and save them in `docs/02-lstm/`
2. **Name them exactly** as listed above (case-sensitive!)
3. **Recommended format:** PNG or JPG
4. **Recommended resolution:** At least 1200x800 pixels for clarity

## Generating Images from Your Notebook

Run the following cells in `lstm-liquefaction.ipynb` and save the plots:

```python
# For exp_data.png (Cell 10)
# Save the cyclic simple shear test plot

# For training_history.png (Cell 25/29)
# Save the training loss plot

# For predictions.png (Cell 29/33)
# Save the LSTM predictions vs experimental plot
```

## Free Image Resources

- **LSTM Diagrams:** https://colah.github.io/posts/2015-08-Understanding-LSTMs/
- **RNN Architectures:** https://d2l.ai/chapter_recurrent-modern/lstm.html
- **Geotechnical:** USGS.gov, PEER.berkeley.edu
- **Neural Networks:** TensorFlow/PyTorch documentation

## Compiling the Slides

```bash
cd docs/02-lstm
pdflatex lstm-slides.tex
pdflatex lstm-slides.tex  # Run twice for references
```

The slides will work even without images (placeholders will show), but adding images makes them much more effective!

## Slides Overview

**Total slides:** 29 pages
**Sections:**
1. Introduction to Liquefaction (4 slides)
2. Traditional Approaches and Limitations (2 slides)
3. Recurrent Neural Networks (3 slides)
4. Long Short-Term Memory (LSTM) (7 slides)
5. LSTM for Liquefaction Prediction (4 slides)
6. Results and Performance (4 slides)
7. Conclusions and Future Work (2 slides)

**Target audience:** Geotechnical engineers with basic ML knowledge
**Duration:** ~30-40 minutes with discussion
