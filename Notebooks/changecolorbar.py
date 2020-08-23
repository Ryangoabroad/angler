import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np

x = np.linspace(0,10,1000)
I = np.sin(x)*np.cos(x[:, np.newaxis])
#I = np.sin(x)*np.cos(x)
#plt.imshow(I, cmap='RdBu')
plt.imshow(I, cmap='PuOr')
#plt.imshow(I, cmap='jet')
#plt.imshow(I, cmap='rainbow')
#plt.imshow(I, cmap='cubehelix')
#plt.imshow(I, cmap='magma')
#plt.imshow(I, cmap='plasma')
#plt.imshow(I, cmap='Oranges')
plt.colorbar()
plt.show()