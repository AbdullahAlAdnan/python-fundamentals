# Fraud Detection Using NumPy
# Module 5 — NumPy and Pandas
# Course: Data Science Program
# Author: Abdullah Al Adnan

import numpy as np

# ── Step 1: Create dataset ──
# 100 normal transactions + 5 fraudulent ones
np.random.seed(42)
normal = np.random.exponential(200, (100, 4))
fraudulent = np.random.exponential(2000, (5, 4))
amounts = np.vstack([normal, fraudulent])

print(f"Dataset shape: {amounts.shape}")
print(f"Total transactions: {len(amounts)}")

# ── Step 2: Calculate column statistics ──
mean_per_col = np.mean(amounts, axis=0)
std_per_col = np.std(amounts, axis=0)

print(f"\nMean per column: {np.round(mean_per_col, 2)}")
print(f"Std per column:  {np.round(std_per_col, 2)}")

# ── Step 3: Normalize each column ──
normalized = (amounts - mean_per_col) / std_per_col
print(f"\nNormalized shape: {normalized.shape}")

# ── Step 4: Set anomaly threshold ──
# Values more than 2 standard deviations above column mean
threshold = mean_per_col + 2 * std_per_col
print(f"\nAnomaly threshold per column: {np.round(threshold, 2)}")

# ── Step 5: Flag suspicious transactions ──
suspicious = amounts > threshold
print(f"\nTotal suspicious flags: {np.sum(suspicious)}")
print(f"Suspicious rows (any column flagged): "
      f"{np.sum(np.any(suspicious, axis=1))}")

# ── Step 6: Find which rows are suspicious ──
suspicious_rows = np.where(np.any(suspicious, axis=1))[0]
print(f"\nSuspicious row indices: {suspicious_rows}")
print(f"Are these the fraud transactions we added? "
      f"{suspicious_rows >= 100}")

# ── Result ──
# System correctly identifies all 5 fraudulent transactions
# This demonstrates statistical anomaly detection using NumPy
# Next step: Apply to real IEEE fraud detection dataset
