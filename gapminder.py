#!/usr/bin/env pythonw

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import numpy as np
import pandas as pd

data = pd.read_csv('gapminder.csv')

colors = np.array([
    '#5A6FFA',
    '#E60DA1',
    "#7E7E7E",
    "#B7F025",
    "#FF9A1E"])

continents = [
    'Africa',
    'Americas',
    'Asia',
    'Europe',
    'Oceania']


patches = []

fig = plt.figure()
ax = plt.gca()

for i in range(5):
    continent = data[data['Continent']==i]
    ax.scatter(continent['GDP'],continent['LifeExpectancy'], s=(continent['Population'])/300000, c=colors[i], alpha=0.7)

ax.set_xscale('log')

for i in range(len(continents)):
    ax.text(300, 83-i*2, continents[i], color=colors[i])

ax.set_xlabel('GDP Per Capita')
ax.set_ylabel('Life LifeExpectancy')

fig.tight_layout()
fig.savefig('gapminder.png', dpi=300)