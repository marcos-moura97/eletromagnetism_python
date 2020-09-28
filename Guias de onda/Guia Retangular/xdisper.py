####### XDisper
import numpy as np
import matplotlib.pyplot as plt
import math

def g(V,m,n_e,b):
    return V*np.sqrt(1-b) - m*math.pi/2 - np.arctan(n_e[0]**2/n_e[1]**2*np.sqrt(b/(1-b)))

def xDisper(n_e, D, N, k0):
    d = D[0] #Espessura do core
    h = D[1] #Espessura do rib
    t = D[2] #Espessura do cladding
    a = D[3]
    s = [h,t]

    n_c = N[0]
    n_s = N[1]
    n_a = N[2]
    #Definições
    #a = D[3] #Largura do rib
    m = np.arange(0,11)
    V = k0*a*np.sqrt(n_e[0]**2 - n_e[1]**2)
    b = np.zeros([1,len(m)])

    x = np.linspace(0, .99, 40)
    #x_lower = x(1:end-1)
    #x_upper = x(2:end)
    plt.figure()
    for i in range(len(m)):
        if (abs(n_e[0])==0 and abs(n_e[1])==0):
            pass
        else:
            f = g(V,m[i],n_e,x)
            plt.plot(x,f)
            plt.plot([0,1], [0,0], 'k')
            plt.axis([0,1,-3,1])
            plt.title('Dispersao')
            plt.xlabel('u')
            plt.ylabel('w')

        for k in range(len(x)):
            f1 = g(V,m[i],n_e,x[k])

            if (f1==0 or abs(f1)<=0.01) and (x[k] != n_s and x[k] != n_c):
                b[i]=x[k]

    b = b[b!=0]
    u = V*np.sqrt(1-b)
    w = V*np.sqrt(b)
    beta = k0*np.sqrt((w/k0/a)**2 + n_e[1]**2)
    print(b)
    return [u, w, beta]
