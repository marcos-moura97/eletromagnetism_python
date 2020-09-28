####### XfieldFunc
import math
import numpy as np

def X_1(u1,a,varPhi,x):
    return np.cos(u1/a*x - varPhi)

def dX_1(u1,a,varPhi,x):
    return -u1/a*np.sin(u1/a*x - varPhi)

def dX2_1(u1,a,varPhi,x):
    return -((u1/a)**2)*np.cos(u1/a*x - varPhi)

def X_2(u1,w1,a,varPhi,x):
    return np.cos(u1 + varPhi)*np.exp(w1/a*(x+a))

def dX_2(u1,w1,a,varPhi,x):
    return w1/a*np.cos(u1 + varPhi)*np.exp(w1/a*(x+a))

def dX2_2(u1,w1,a,varPhi,x):
    return ((w1/a)**2)*np.cos(u1 + varPhi)*np.exp(w1/a*(x+a))

def X_3(u1,w1,a,varPhi,x):
    return np.cos(u1 - varPhi)*np.exp(-w1/a*(x-a))

def dX_3(u1,w1,a,varPhi,x):
    return -w1/a*np.cos(u1-varPhi)*np.exp(-w1/a*(x-a))

def dX2_3(u1,w1,a,varPhi,x):
    return ((w1/a)**2)*np.cos(u1-varPhi)*np.exp(-w1/a*(x-a))


def XfieldFunc(XX, u, w, m, a, RegX):
    u1 = u[m+1]
    w1 = w[m+1]
    varPhi = m*math.pi/2



    if RegX == 1:
        X =  X_1(u1,a,varPhi,XX)
        dXdx = dX_1(u1,a,varPhi,XX)
        dXdx2 = dX2_1(u1,a,varPhi,XX)

    elif RegX == 2:
        X = X_2(u1,w1,a,varPhi,XX)
        dXdx = dX_2(u1,w1,a,varPhi,XX)
        dXdx2 = dX2_2(u1,w1,a,varPhi,XX)

    elif RegX == 3:
        X = X_3(u1,w1,a,varPhi,XX)
        dXdx = dX_3(u1,w1,a,varPhi,XX)
        dXdx2 = dX2_3(u1,w1,a,varPhi,XX)
    return [X,dXdx,dXdx2]
