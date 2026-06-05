import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
output_dir = os.path.dirname(os.path.abspath(__file__))

df = sns.load_dataset('iris')

print("LOADING THE DATASET")
print("\n.shape")
print(df.shape)
print("\n.columns")
print(df.columns.tolist())
print("\n.head()")
print(df.head())

print("INSPECTION")
print("\n.info()")
df.info()
print("\n.describe()")
print(df.describe().round(2))
print("\nSpecies counts")
print(df['species'].value_counts())

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
labels   = ['Sepal Length (cm)', 'Sepal Width (cm)', 'Petal Length (cm)', 'Petal Width (cm)']
palette  = ['#378ADD', '#1D9E75', '#D4537E']

# Scatter Plot
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(
    data=df, x='petal_length', y='petal_width',
    hue='species', style='species',
    palette=palette, s=80, ax=ax
)
ax.set_title('Scatter Plot: Petal Length vs Petal Width', fontsize=13, pad=12)
ax.set_xlabel('Petal Length (cm)')
ax.set_ylabel('Petal Width (cm)')
ax.legend(title='Species', framealpha=0.7)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'scatter.png'), dpi=140, bbox_inches='tight')
plt.close()
print("\nSaved scatter.png")
 
#Histograms
fig, axes = plt.subplots(2, 2, figsize=(10, 7))
axes = axes.flatten()
 
for i, (feat, label) in enumerate(zip(features, labels)):
    for sp, color in zip(df['species'].unique(), palette):
        axes[i].hist(
            df[df['species'] == sp][feat],
            bins=12, alpha=0.6, color=color, label=sp, edgecolor='white'
        )
    axes[i].set_title(label, fontsize=11)
    axes[i].set_xlabel('Value (cm)')
    axes[i].set_ylabel('Count')
    if i == 0:
        axes[i].legend(title='Species', fontsize=8)
 
fig.suptitle('Histograms — Feature Distributions by Species', fontsize=13, y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'histograms.png'), dpi=140, bbox_inches='tight')
plt.close()
print("Saved histograms.png")
 
#Box Plots 
fig, axes = plt.subplots(1, 4, figsize=(13, 5))
 
for i, (feat, label) in enumerate(zip(features, labels)):
    sns.boxplot(
        data=df, x='species', y=feat,
        palette=palette, width=0.5, linewidth=1.2,
        flierprops=dict(marker='o', markersize=4, linestyle='none'),
        ax=axes[i]
    )
    axes[i].set_title(label, fontsize=10)
    axes[i].set_xlabel('')
    axes[i].set_ylabel('cm' if i == 0 else '')
    axes[i].tick_params(axis='x', rotation=15, labelsize=8)
 
fig.suptitle('Box Plots — Spread & Outliers by Species', fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'boxplots.png'), dpi=140, bbox_inches='tight')
plt.close()
print("Saved boxplots.png")