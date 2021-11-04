""" Baseado no capítulo 10 do Orfanidis
 acha os betas de cada material resolvendo a equação transcedental
 relacionada e plota o perfil de campo do plasmon de estruturas DMD 
 (dielétrico/metal/dielétrico) como a de baixo
           _________________________
           |                       |       x
           |       n1 = SiO2       |       ^
           |                       |       |
           -------------------------       |
           |     n2 = grafeno      |       -----> z
           -------------------------      /
           |                       |     /
           |      n3 = SiO2         |     y
           |                       |
           -------------------------

"""

import matplotlib.pyplot as plt
import numpy as np
import math


def encontra_beta():
    """ Resolve a equação transcedental e retorna beta """
    
    # importando os  indices de refração e constantes
    global n1, n2, n3
    global a, lbd, k0
    
    P = 1
    phi = 0
    dx = 1e-7

    d = 2*a
    V = k0*d*np.sqrt(n1**2 - n2**2)
        

    divsn = 0.01
    eps = 1e-3
    b0 = 1-eps
    b1 = b0
    b2 = b1-divsn
    
    F1 = (V/2)*np.sqrt(1-b1)- np.arctan(np.sqrt(b1/(1-b1)))

    while divsn>eps:
        F2 = (V/2)*np.sqrt(1-b2) - np.arctan(np.sqrt(b2/(1-b2)))
        
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
        
    neff = np.sqrt(b*(n1**2-n2**2)+n2**2)

    beta = neff*k0
    
    return beta

""" Constantes fundamentais """

c = 3e8  #velocidade da luz no vácuo
mu0 = 4*(22/7)*10**-7 * 10**-6  #permeabilidade no vácuo
epsilon0 = 1/(c**2 * mu0)  #permissividade no vácuo

n1 = 1.55 # SiO2
n2 = 1 # Grafeno
n3 = n1

d_g = 2E-9

ep_sio2 = n1**2 * epsilon0
ep_graf = n2**2 * epsilon0

a = 20e-9 #comprimento do nucleo

# acha a constante de propagação
lbd = 1.55e-6 # um
k0 = 2*math.pi/lbd 

""" Cálculo dos vetores de onda"""

beta = encontra_beta()

# número/vetor de onda
k_x = k0*np.sqrt((ep_sio2*ep_graf)/(ep_sio2+ep_graf))
k_1 = np.sqrt(beta**2-k0**2*ep_sio2)

k_2 = k_1
k_z1 = k0*np.sqrt((ep_sio2**2)/(ep_sio2+ep_graf))
k_z2 = k0*np.sqrt((ep_graf**2)/(ep_sio2+ep_graf))

# Constante de propagação
gamma = np.sqrt(beta**2 + k0**2*np.abs(ep_graf))

# constantes de atenuação
alpha_c = np.sqrt(beta**2 - k0**2*ep_sio2) #k1


p_c = ep_graf/ep_sio2

psi = 0 #é 0 pois p_c = p_s


""" Calculando Ex """


x_values = np.linspace(-4,4,601)*a
Ex = np.zeros(len(x_values))

for i in enumerate(x_values):
    index = i[0]
    x1 = i[1]
    
    Ex_function = lambda x: np.cosh(gamma*a - psi)*np.exp(alpha_c*(x+a)) if (x<-a) else (np.cosh(gamma*a + psi)*np.exp(-alpha_c*(x-a)) if(x>a) else (np.cosh(gamma*x + psi) if(np.abs(x)<=a) else 0))
    
    Ex[index] = Ex_function(x1)
    
    
""" PLOT """

plt.fill([-1, 1, 1, -1], [min(np.real(Ex))-.25,min(np.real(Ex))-.25,max(np.real(Ex))+.25,max(np.real(Ex))+.25], "#D3D3D3");
plt.plot(x_values/a, np.real(Ex));
plt.plot([0, 0],[min(np.real(Ex))-.25, max(np.real(Ex))+.25],'k--')
plt.xlabel('x/a (um)');
plt.ylabel('|Ex|');
plt.title('Perfil de campo surface plasmon')