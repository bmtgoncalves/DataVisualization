#!/usr/bin/env pythonw

import matplotlib.pyplot as plt

data = [17, 18, 20, 22, 24]

fig = plt.figure(figsize=(10,10))
ax = plt.gca()
ax.pie(data, labels=data)
ax.legend(["A", "B", "C", "D", "E"])
fig.savefig('pie.png', dpi=300)