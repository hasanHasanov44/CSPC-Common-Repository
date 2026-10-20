# PW3: Data, Distributions, Testing, and Causation

## Session 1: Characterise the data
1. **Distributions:** `age` is symmetric; `chol` and `trestbps` are right-skewed; `thalach` is left-skewed.
2. **Normality (Shapiro-Wilk):** All continuous variables (`age`, `chol`, `trestbps`, `thalach`) have $p < 0.05$, so none are strictly normally distributed.

## Session 2: Draw conclusions
1. **Heart Rate vs Disease:**
   - **Healthy:** $158.38 \pm 1.50$ bpm | **Disease:** $139.26 \pm 1.92$ bpm
   - **t-test:** $p = 3.46 \times 10^{-14}$
   - **Conclusion:** Heart disease patients reach a significantly lower max heart rate.
2. **Age vs Thalach:** Pearson $r = -0.394$ ($p < 0.0001$). Max heart rate decreases as age increases.

## Dataset 2: Chemical Mystery
1. **Naive Correlation:** Benzene = $0.385$, Cadmium = $0.880$ (Cadmium looks like the main cause).
2. **Controlled for Confounder (`pollution_index` 45–55):**
   - Benzene = $0.658$, Cadmium = $-0.040$
3. **Conclusion:** **Benzene** is the real cause of malignancy. Cadmium was a spurious correlation caused by the confounding variable `pollution_index`.

## Bonus
- **Target Entropy:** $0.995 \text{ bits}$ (Balanced dataset, high unpredictability).