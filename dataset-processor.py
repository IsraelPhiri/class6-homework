#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

os.makedirs('plots/class6', exist_ok=True)

wine_df = pd.read_csv('wine.data',sep=',',header=0)

wine_df.columns = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 'total_phenols',
                   'flavanoids','nonflavanoid_phenols', 'proanthocyanins', 'color_intensity', 'hue',
                   'od280 od315_of_diluted_wines','proline']

# Multifeature with size, color, marker and alpha

for i in wine_df:

    plt.style.use("ggplot")
    fig, axes = plt.subplots(1, 1, figsize=(5, 5))
    axes.grid(axis='y', alpha=0.5)

    #while str(i) != 'total_phenols' or i!='color_intensity' or i!='ash':
    axes.scatter(wine_df[str(i)], wine_df['total_phenols'],s=(wine_df[str(i)]*wine_df['total_phenols']),
    label=f''+str(i)+' to total_phenols', color='green', marker='o', edgecolors='w', alpha=0.7)
    axes.scatter(wine_df[str(i)], wine_df['color_intensity'],s=(wine_df[str(i)] * wine_df['color_intensity'])/2,
    label=f''+str(i)+' to color_intensity', color='orange', marker='x', edgecolors='w', alpha=0.7)
    axes.scatter(wine_df[str(i)], wine_df['ash'],s=(wine_df[str(i)] * wine_df['ash']),
                     label=f''+str(i)+' to ash', color='purple', marker='^', edgecolors='w', alpha=0.7)
    axes.set_title(f''+str(i)+' comparisons')
    axes.legend()
    plt.savefig(f'plots/class6/class6-matplotlib_multifeature_scatter_'+str(i)+'.png', format='png')
    plt.clf()

#os.makedirs('plots/seaborn_pairplot', exist_ok=True)

#darkgrid, whitegrid, dark, white, ticks
sns.set(style='darkgrid', palette='coolwarm')

# Wine Pairplot with hue and diag_kind
sns.pairplot(wine_df,hue = 'class', diag_kind='hist')
plt.savefig('plots/class6/class6-seaborn_pairplot.png')


# 3D plot with Alcohol, Color intensity
plt.style.use("ggplot")
fig = plt.figure(figsize=(8, 6))
axes = fig.add_subplot(1,1,1, projection='3d')

xs = wine_df['alcohol']
ys = wine_df['color_intensity']
zs = wine_df['proline']
axes.scatter(xs, ys, zs, color='green', s=50, alpha=0.6, edgecolors='w')

axes.set_xlabel('Alcohol')
axes.set_ylabel('Color Intensity')
axes.set_zlabel('Proline')
plt.savefig('plots/class6/class6-matplotlib_scatter_3d.png')

plt.close()

