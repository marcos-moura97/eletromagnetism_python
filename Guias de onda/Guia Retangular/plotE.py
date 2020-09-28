####### PlotE
import numpy as np
import matplotlib.pyplot as plt
import math

from xfield_func import XfieldFunc
from yfield_func import YfieldFunc

def plotE(n_e, vm, u, w, beta, D, N, k0):
    d = D[0] #Espessura do core
    h = D[1] #Espessura do rib
    t = D[2] #Espessura do cladding
    a = D[3]
    s = [h,t]

    n_c = N[0]
    n_s = N[1]
    n_a = N[2]

    c = 3e8
    omega = k0*c
    mu0 = 4*math.pi*1e-7
    ep0 = (mu0*c**2)**-1

    XX = np.linspace(-(a+10e-6), a+10e-6, 50,dtype="complex_")
    YY = np.linspace(-3e-6, d+h+3e-6, 50,dtype="complex_")
    l = [len(XX), len(YY)]
    X = np.zeros(l[0],dtype="complex_")
    dXdx = X
    dXdx2 = X
    Y = np.zeros(l[1],dtype="complex_")
    dYdy = Y
    Zx = np.zeros([l[1], l[0]],dtype="complex_")
    for m in range((len(u)-1)):

        beta1 = beta[m+1]

        for i in range(l[0]):
            if abs(XX[i]) <= a:
                n_ = n_e[0]
                RegX = 1
                s = h
            elif XX[i] < -a:
                n_ = n_e[1]
                RegX = 2
                s = t
            elif XX[i] > a:
                n_ = n_e[1]
                RegX = 3
                s = t

            X_ = XfieldFunc(XX[i], u, w, m, a, RegX)
            X[i] = X_[0]
            dXdx[i] = X_[1]
            dXdx2[i] = X_[2]

            for k in range(l[1]):
                if YY[k] < 0:
                    RegY = 1
                    n = n_s
                elif (YY[k] >= 0) and (YY[k] < d):
                    RegY = 2
                    n = n_c
                elif (YY[k] >= d) and (YY[k] < d+s):
                    RegY = 3
                    n = n_s
                else:
                    RegY = 4
                    n = n_a

                K = omega*ep0*n**2*beta1
                x = np.linspace((n_s), n_c, 100,dtype="complex_")
                ind = np.where(x == n_)
                n_ = x[(len(x)-1)-ind[0][0]]
                Y_ = YfieldFunc(YY[k],k0,n_c,n_a,n_s,n_,d,s, RegY)
                #print(X[k])
                Y[k] = Y_[0]
                #print(Y_[0],Y[k])
                dYdy[k] = Y_[1]
                Hy = X_[0]*Y_[0]#X[i]*Y[k]
                #print(Y_[0],Y[k])
                dHydx2 = X_[2]*Y_[0]#dXdx2[i]*Y[k]
                Ex = omega*mu0/beta1*Hy + dHydx2/K
                Zx[k,i] = Ex


    plt.figure()
#    fig, ax = plt.subplots(1, 1)
    #ax.hold(True)
 #   colorbar;
    plt.contourf(XX, YY, Zx)
    plt.plot([-(a+10e-6), -a, -a, a, a, a+10e-6], [d+t, d+t, d+h, d+h, d+t, d+t], 'k')
    plt.plot([-(a+10e-6), a+10e-6], [d, d], 'k')
    plt.plot([-(a+10e-6), a+10e-6], [0, 0], 'k')

    plt.xticks([-a,a], ['-a','a'])
    plt.yticks([0,d,d+t, d+h], ['0','d','d+t','d+h'])
    plt.show()

    #title(['E^x_{' int2str(m+1) int2str(vm) '}'])

