import numpy as np
import math
from scipy.optimize import brentq
import scipy
import matplotlib.pyplot as plt


pi = math.pi #famoso pi

a=8          #diametro
n1=1.45      #nucleo
n2=1.4       #revestimento
lbd=8.11     #comprimentodeonda

v=(2*pi*a/lbd)*math.sqrt(n1**2-n2**2)    #frequencia normalizada
#v=4

#pontos r e phi
r=np.linspace(0,a,400)
phi=np.linspace(0,2*pi,400)
[r,phi]=np.meshgrid(r,phi)


#calcula os modos
## m0
m0=[]

for x in range(1,11):

    for t in np.linspace((x-1)*pi,(x+1)*pi,500):
        s = scipy.special.jv(0,t)

        if s==0 or abs(s)<=0.01:
            m0=t
    if x*pi>v:
        break


if m0:
    z= (scipy.special.jv(0,m0*r/a)*np.cos(0*phi))
    z = list(map(lambda x:x**2,z))
    x=r*np.cos(phi)
    y=r*np.sin(phi)

    plt.figure(0)
    plt.contourf(x, y, z)
    plt.colorbar()
    plt.show()

## m1
m1=[]

for x in range(1,11):

    for t in np.linspace((x-1)*pi,(x+1)*pi,500):
        s = scipy.special.jv(1,t)

        if s==0 or abs(s)<=0.01:
            m1=t
    if x*pi>v:
        break


if m1:
    z= (scipy.special.jv(1,m1*r/a)*np.cos(1*phi))
    z = list(map(lambda x:x**2,z))
    x=r*np.cos(phi)
    y=r*np.sin(phi)

    plt.figure(1)
    plt.contourf(x, y, z)
    plt.colorbar()
    plt.show()


## m2
m2=[]

for x in range(1,11):

    for t in np.linspace((x-1)*pi,(x+1)*pi,500):
        s = scipy.special.jv(2,t)

        if s==0 or abs(s)<=0.01:
            m2=t
    if x*pi>v:
        break


if m1:
    z= (scipy.special.jv(2,m2*r/a)*np.cos(2*phi))
    z = list(map(lambda x:x**2,z))
    x=r*np.cos(phi)
    y=r*np.sin(phi)

    plt.figure(2)
    plt.contourf(x, y, z)
    plt.colorbar()
    plt.show()
