# Task 1: Exploring and Visualizing the Iris Dataset

## Task Objective

Load, inspect, and visualize the Iris dataset to understand data distributions and relationships between features across different flower species. The goal is to practice core data exploration skills using pandas, matplotlib, and seaborn.

---

## Dataset Used

**Name:** Iris Dataset  
**Source:** Built-in dataset from the `seaborn` library (`sns.load_dataset('iris')`)  
**Size:** 150 rows × 5 columns  
**Features:**

| Column | Type | Description |
|---|---|---|
| sepal_length | float64 | Sepal length in cm |
| sepal_width | float64 | Sepal width in cm |
| petal_length | float64 | Petal length in cm |
| petal_width | float64 | Petal width in cm |
| species | string | Flower species (setosa, versicolor, virginica) |

**Class distribution:** 50 samples per species — perfectly balanced, no missing values.

---

## Models Applied

This task focuses on **Exploratory Data Analysis (EDA)** — no machine learning models were applied.

Tools and methods used:

- `pandas` — data loading, `.head()`, `.info()`, `.describe()`, `.value_counts()`
- `seaborn` — scatter plot, box plots
- `matplotlib` — histograms, plot customization and saving

---

## Key Results and Findings

### 1. Scatter Plot (Petal Length vs Petal Width)
- **Setosa** is completely separate from the other two species — easily distinguishable by petal size alone.
- **Versicolor** and **Virginica** overlap slightly, making them harder to separate.
- Petal features are the strongest indicators of species.

### 2. Histograms (Feature Distributions)
- **Petal length** shows a clear bimodal distribution: setosa clusters at 1–2 cm while versicolor and virginica range from 3–7 cm.
- **Sepal width** is the most normally distributed feature with the least separation between species.
- **Petal width** mirrors petal length — very effective at separating setosa from the rest.

### 3. Box Plots (Spread and Outliers)
- **Sepal width** has the most outliers across all species.
- **Petal length** and **petal width** show very clean, tight boxes for setosa with almost no overlap with other species.
- **Virginica** has the largest spread in petal dimensions, making it the most variable species.

### Summary Table — Descriptive Statistics

| Feature | Mean | Std Dev | Min | Max |
|---|---|---|---|---|
| Sepal Length | 5.84 | 0.83 | 4.3 | 7.9 |
| Sepal Width | 3.06 | 0.44 | 2.0 | 4.4 |
| Petal Length | 3.76 | 1.77 | 1.0 | 6.9 |
| Petal Width | 1.20 | 0.76 | 0.1 | 2.5 |

**Overall conclusion:** Petal measurements are far more useful than sepal measurements for distinguishing iris species. Setosa is trivially separable; versicolor and virginica require more nuanced analysis.

---

## Output Files

| File | Description |
|---|---|
| `task1.py` | Main Python script |
| `scatter.png` | Scatter plot — petal length vs petal width |
| `histograms.png` | Histograms — all 4 features by species |
| `boxplots.png` | Box plots — spread and outliers by species |
| `README.md` | This file |
