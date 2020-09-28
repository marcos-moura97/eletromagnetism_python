####### YDisper
import numpy as np
import matplotlib.pyplot as plt
from eigen import kappa, sigma, gamma, phi, psi

def disperFunciton(k0,n_c,n_s,n_a,d,s,x,x1):
    if type(x) == np.ndarray:
        return np.sin(kappa(k0,n_c,x)*d - 2*phi(k0,n_c,n_s,x[::-1])) - np.sin(kappa(k0,n_c,x)*d)*np.exp(-2*(sigma(k0,n_s,x)*s+psi(k0,n_s,n_a,x)))
    else:
        return np.sin(kappa(k0,n_c,x)*d - 2*phi(k0,n_c,n_s,x1)) - np.sin(kappa(k0,n_c,x)*d)*np.exp(-2*(sigma(k0,n_s,x)*s+psi(k0,n_s,n_a,x)))



def yDisper(k0, N, D):

    d = D[0] #Espessura do core
    h = D[1] #Espessura do rib
    t = D[2] #Espessura do cladding
    s = [h,t]

    n_c = N[0]
    n_s = N[1]
    n_a = N[2]


    x = np.linspace((n_s), n_c, 100,dtype="complex_")

    #Equação de dispersão
    n_e = np.zeros([10, 2],dtype="complex_")

    for i in range(len(s)):

        f = disperFunciton(k0,n_c,n_s,n_a,d,s[i],x,x)
        plt.plot(x,f)
        plt.title("índices efetivos são as raízes desse gráfico")

        plt.plot([n_s,n_c], [0,0], 'k')

        ind = 0
        for k in range(len(x)):
            f1 = disperFunciton(k0,n_c,n_s,n_a,d,s[i],x[k],x[(len(x)-1)-k])

            if (f1==0 or abs(f1)<=0.01) and (x[k] != n_s and x[k] != n_c):
                n_e[ind][i]=x[k]
                ind = ind+1
            if ind==10:
                break
    return n_e

