# Hidden Markov Model for Market Regimes

This repository contains the implementation of a Hidden Markov Model (HMM) to detect market regimes as per the second assignment for the course MTL106 : Probability and Stochastic Processes. The objective is to classify financial market regimes (Bullish or Bearish) based on asset return data.

## Problem Overview

The assignment involves detecting market regimes from simulated asset returns using HMMs. This is achieved by applying the Baum-Welch algorithm to learn the model parameters and subsequently using the trained model to classify regimes. The data is simulated with Gaussian distributions representing bullish and bearish market conditions.

### Key Concepts
- **Hidden Markov Models (HMM):** Statistical models to infer hidden states (market regimes) from observable data (asset returns).
- **Baum-Welch Algorithm:** Used to estimate the HMM parameters. 
- **Regimes:** Bullish (positive mean, low variance) and Bearish (slight negative mean, higher variance).

## Input Format

1. **Transition Matrix (A):** The first line contains four values `a00`, `a01`, `a10`, `a11` (e.g., `0.7 0.3 0.4 0.6`).
2. **Initial State Probabilities (π):** The second line contains two values `π0`, `π1` (e.g., `0.6 0.4`).
3. **Number of Time Steps (T):** The third line contains an integer `T` (e.g., `100`).
4. **Returns Data (Y):** The subsequent `T` lines contain one return value per line (e.g., `0.5`, `-0.2`, etc.).

## Output Format

For each of the `T` days, the output specifies the market regime:
- **"Bullish"** for a bullish regime.
- **"Bearish"** for a bearish regime.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MTL106-HMM-Market-Regimes.git
   cd MTL106-HMM-Market-Regimes
   ```

2. Place your input files in the repository directory.

3. Run the main script with the input file:
   ```bash
   python main.py input_file > output_file
   ```

## Examples

### Input (sample file: `input1`)
```
0.7 0.3 0.4 0.6
0.6 0.4
5
0.1
-0.2
0.5
-0.4
0.3
```

### Output (sample file: `test1`)
```
Bullish
Bearish
Bullish
Bearish
Bullish
```

## Dependencies

This implementation uses only the Python Standard Library. Ensure you have Python 3.7+ installed.
