#!/usr/bin/env pythonw

import matplotlib.pyplot as plt
import numpy as np

dataLA = [20, 14, 23]
dataSF = [11, 18, 28]

pos = np.arange(0, 5, 2)
width = 0.5

fig, ax = plt.subplots(1)

ax.bar(pos, dataLA, width=width)
ax.bar(pos+width, dataSF, width=width)

ax.set_ylabel('Count')
ax.set_xlabel('Classes')
ax.set_xticks(pos + width / 2)
ax.set_xticklabels(('A', 'B', 'C'))

ax.legend(['LA', 'SF'])

fig.savefig('bar.png', dpi=300)