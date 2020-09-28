## Padrões da difração de Fraunhofer no experimento de fenda dupla

import numpy as np
import matplotlib.pyplot as plt
import math

pi = math.pi

b = 0.1
a = 0.4
l = 632
f = .5

theta = np.arange(-.04,.04,0.00001)
beta=pi*(b/1000)/(l/1e9)*np.sin(theta)

#escala
alpha=pi*(a/1000)/(l/1e9)*np.sin(theta)
y=4*(np.sin(beta)**2/beta**2)*(np.cos(alpha)**2)

#distribuição
plt.plot(theta*f*1000,y)

plt.title('Difração de Fraunhofer')
plt.xlabel('Posição da tela [nm]')
plt.ylabel('Itensidade')
plt.show()
