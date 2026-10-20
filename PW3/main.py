import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


# SESSION 1: Characterise the data

print("=== SESSION 1 ===")
df_heart = pd.read_csv("heart.csv")
print(f"Heart Dataset Shape: {df_heart.shape}")

continuous_cols = ["age", "chol", "trestbps", "thalach"]

# 2. Histograms / Distributions
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flatten(), continuous_cols):
    sns.histplot(df_heart[col], kde=True, ax=ax, color='skyblue')
    ax.set_title(f"Distribution of {col}")
plt.tight_layout()
plt.savefig("distributions.png")
plt.close()

# 3. Normality Tests (Shapiro-Wilk)
print("\n--- Shapiro-Wilk Normality Test Results ---")
for col in continuous_cols:
    stat, p_val = stats.shapiro(df_heart[col].dropna())
    verdict = "Approximately Normal" if p_val > 0.05 else "Not Normal (p < 0.05)"
    print(f"{col:10s}: W = {stat:.4f}, p-value = {p_val:.4e} -> {verdict}")


# SESSION 2: Draw conclusions

print("\n=== SESSION 2 ===")

# 4. Group Comparison (thalach by target)
g0 = df_heart[df_heart['target'] == 0]['thalach'].dropna() # Healthy
g1 = df_heart[df_heart['target'] == 1]['thalach'].dropna() # Disease

stat_t, p_val_t = stats.ttest_ind(g0, g1)
print(f"Thalach Comparison (Healthy vs Disease):")
print(f"  Healthy Mean: {g0.mean():.2f} ± {g0.sem():.2f} bpm")
print(f"  Disease Mean: {g1.mean():.2f} ± {g1.sem():.2f} bpm")
print(f"  Two-sample t-test p-value: {p_val_t:.4e}")

plt.figure(figsize=(6, 5))
sns.barplot(x='target', y='thalach', data=df_heart, capsize=0.1, errorbar=('ci', 95), palette='Set2')
plt.xticks([0, 1], ['Healthy (0)', 'Disease (1)'])
plt.title("Mean Max Heart Rate (thalach) with 95% CI")
plt.ylabel("Max Heart Rate (thalach)")
plt.savefig("thalach_comparison.png")
plt.close()

# 5. Age vs Thalach Correlation
r_p, p_p = stats.pearsonr(df_heart['age'], df_heart['thalach'])
print(f"\nAge vs Thalach Correlation (Pearson r): {r_p:.3f} (p-value: {p_p:.4e})")

plt.figure(figsize=(7, 5))
sns.regplot(x='age', y='thalach', data=df_heart, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title("Age vs Maximum Heart Rate (thalach)")
plt.savefig("age_vs_thalach.png")
plt.close()


# DATASET 2: Chemical-exposure mystery

print("\n=== DATASET 2: CHEMICAL MYSTERY ===")
df_chem = pd.read_csv("chemicals_cancer.csv")

# 6. Naive Analysis
c_benz = df_chem['benzene'].corr(df_chem['malignancy'])
c_cad = df_chem['cadmium'].corr(df_chem['malignancy'])
print("Naive Correlations with Malignancy:")
print(f"  Benzene: {c_benz:.3f}")
print(f"  Cadmium: {c_cad:.3f}")

# 7. Controlling for Confounder (pollution_index)
subset = df_chem[(df_chem['pollution_index'] > 45) & (df_chem['pollution_index'] < 55)]
c_benz_ctrl = subset['benzene'].corr(subset['malignancy'])
c_cad_ctrl = subset['cadmium'].corr(subset['malignancy'])

print("\nControlled Correlations (Filtered pollution_index 45-55):")
print(f"  Benzene: {c_benz_ctrl:.3f}")
print(f"  Cadmium: {c_cad_ctrl:.3f}")


# BONUS

print("\n=== BONUS: TARGET BALANCING & ENTROPY ===")
props = df_heart['target'].value_counts(normalize=True)
entropy_val = stats.entropy(props, base=2)
print("Target proportions:")
print(props.to_string())
print(f"Shannon Entropy: {entropy_val:.3f} bits (Max is 1.0 bit for binary)")