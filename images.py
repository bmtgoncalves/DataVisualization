import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

img=mpimg.imread('viridis.jpg')

# Matrix from https://github.com/MaPePeR/jsColorblindSimulator/blob/master/colorblind.js

ColorMatrixMatrixes = {
 'Achromatomaly': np.array([[61.8, 32, 6.2],
                            [16.3, 77.5, 6.2],
                            [16.3, 32, 51.6]])/100,

 'Achromatopsia': np.array([[29.9, 58.7, 11.4],
                            [29.9, 58.7, 11.4],
                            [29.9, 58.7, 11.4]])/100,

 'Deuteranomaly': np.array([[80, 20, 0],
                            [25.833, 74.167, 0],
                            [0, 14.167, 85.833]])/100,

 'Deuteranopia': np.array([[62.5, 37.5, 0],
                           [70, 30, 0],
                           [0, 30, 70]])/100,

 'Normal': np.array([[100, 0, 0],
                     [0, 100, 0],
                     [0, 0, 100]])/100,

 'Protanomaly': np.array([[81.667, 18.333, 0],
                          [33.333, 66.667, 0],
                          [0, 12.5, 87.5]])/100,

 'Protanopia': np.array([[56.667, 43.333, 0],
                         [55.833, 44.167, 0],
                         [0, 24.167, 75.833]])/100,

 'Tritanomaly': np.array([[96.667, 3.333, 0],
                          [0, 73.333, 26.667],
                          [0, 18.333, 81.667]])/100,

 'Tritanopia': np.array([[95, 5, 0],
                         [0, 43.333, 56.667],
                         [0, 47.5, 52.5]])/100
 }

fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)

names = sorted(ColorMatrixMatrixes.keys())

for i in range(len(names)):
  version = names[i]
  transformation = ColorMatrixMatrixes[version]

  img_flat = img.reshape(img.shape[0] * img.shape[1], 3)
  new_img_array = np.dot(img_flat, transformation.T).astype('uint8')
  new_img = new_img_array.reshape(img.shape)

  row = i//3
  col = i%3
  axs[row][col].imshow(new_img)
  axs[row][col].set_title(version)
  axs[row][col].axis('off')

fig.subplots_adjust(hspace=0.1, wspace=0.1)#, bottom=0, right=None, top=0.05,
               # wspace=0.05, hspace=0)

fig.set_size_inches(9, 12)
fig.tight_layout()
fig.savefig('images2.png', dpi=300)