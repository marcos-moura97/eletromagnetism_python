import numpy as np
import matplotlib.pyplot as plt
import math

pi = math.pi

n1 = 3.38       #nucleo
n2 = 3.3        #revestimento
n3 = 3          #substrato

d = 2.5E-6      #distancia
a = d/2

c = 3E8         #velocidade da luz no vácuo
mi0 = 4*pi*10**-7#permeabilidade no vácuo


aa=0
m=0

lbd = 1E-6#np.arange(1E-6,1E-4,1E-7) #comprimentos de onda



#while aa==0: #para variar o modo
#for lbd in lambd: #para variar V

k0 = 2*math.pi/lbd

P = 1
phi = 0

dx = 1E-7

V = k0*d*math.sqrt(n1**2 - n2**2)

divsn = .01
eps = 1E-6
b0 = 1-eps
b1 = b0
b2 = b1-divsn


F1 = (V/2)*math.sqrt(1-b1)-m*pi/2 - math.atan(math.sqrt(b1/(1-b1))) #ghatak


while divsn>eps:

    F2 = (V/2)*math.sqrt(1-b2)-m*pi/2 - math.atan(math.sqrt(b2/(1-b2)))

    if(F1*F2<0):
        b2 = (b1+b2)/2
        divsn = divsn/2
    else:
        b1=b2
        b2 = b1-divsn
        F1=F2


b = (b1+b2)/2
if b<0:
    b=0


## p/ TM

divsn = .01
b1 = b0
b2 = b1-divsn

F1_ = (V/2)*math.sqrt(1-b1)-m*pi/2 - math.atan((n1/n2)**2*math.sqrt(b1/(1-b1))) #ghatak

while divsn>eps:

    F2_ = (V/2)*math.sqrt(1-b2)-m*pi/2 - math.atan(((n1/n2)**2)*math.sqrt(b2/(1-b2)))

    if(F1_*F2_<0):
        b2 = (b1+b2)/2
        divsn = divsn/2
    else:
        b1=b2
        b2 = b1-divsn
        F1_=F2_

b_ = (b1+b2)/2

if b_<0:
    b_=0



neff = math.sqrt(b*(n1**2-n2**2)+n2**2)
k0 = 2*pi/lbd
beta = neff*k0
gamma = (n2**2-n3**2)/(n1**2 - n2**2)

phi=0
A=1

## Dispersão de Campo nas 3 áreas
x1= np.arange(-2E-6,-a,dx*10E-2)

k = math.sqrt(k0**2 * n1**2 - beta**2)
sigma = math.sqrt(beta**2 - k0**2 * n3**2)
ksi = math.sqrt(beta**2 - k0**2 * n2**2)

Ey1 = A*math.cos((k)*a - phi)*np.exp(ksi*(x1+a)) #x<-a



x2 = np.arange(-a,a,dx)


k = math.sqrt(k0**2*  n1**2 - beta**2)
sigma = math.sqrt(beta**2 - k0**2 * n2)

Ey2= A*np.cos(k*x2 + phi) #-a<x<a



x3 = np.arange(a,2E-6,dx*10E-2)

k = math.sqrt(k0**2 * n1**2 - beta**2)
sigma = math.sqrt(beta**2 - k0**2 * n3**2)

Ey3 = A*math.cos(k*a + phi)*np.exp(-sigma*(x3-a)) #x>a


plt.plot(x1,Ey1,'b')
plt.plot(x2,Ey2,'b')
plt.plot(x3,Ey3,'b')
plt.plot([-a,-a],[0,A],'k--')
plt.plot([a,a],[0,A],'k--')
plt.xticks([-a,a], ['-a','a'])
plt.xlabel('y')
plt.ylabel('Ey')

plt.show()
