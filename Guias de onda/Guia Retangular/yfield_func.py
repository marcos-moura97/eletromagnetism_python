####### YfieldFunc
import math
import numpy as np
from eigen import kappa, sigma, gamma, phi, psi

def K1(k0,n_c,n_s,ne):
    return np.sqrt(1+(kappa(k0,n_c,ne)/sigma(k0,n_s,ne))**2)/2


def Y_1(k0,n_c,n_s,ne,y):
    return np.cos(phi(k0,n_c,n_s,ne))*np.exp(sigma(k0,n_s,ne)*y)

def dY_1(k0,n_c,n_s,ne,y):
    return sigma(k0,n_s,ne)*np.cos(phi(k0,n_c,n_s,ne))*np.exp(sigma(k0,n_s,ne)*y)

def Y_2(k0,n_c,n_s,ne,y):
    return np.cos(kappa(k0,n_c,ne)*y - phi(k0,n_c,n_s,ne))

def dY_2(k0,n_c,n_s,ne,y):
    return -kappa(k0,n_c,ne)*np.sin(kappa(k0,n_c,ne)*y - phi(k0,n_c,n_s,ne))

def Y_3(k0,n_c,n_s,ne,y,d):
    return K1(k0,n_c,n_s,ne)*(np.sin(kappa(k0,n_c,ne)*d)*np.exp(-sigma(k0,n_s,ne)*(y-d)) - np.sin(kappa(k0,n_c,ne)*d - 2*phi(k0,n_c,n_s,ne))*np.exp(sigma(k0,n_s,ne)*(y-d)))

def dY_3(k0,n_c,n_s,ne,y,d):
    return -K1(k0,n_c,n_s,ne)*sigma(k0,n_s,ne)*(np.sin(kappa(k0,n_c,ne)*d)*np.exp(-sigma(k0,n_s,ne)*(y-d)) + np.sin(kappa(k0,n_c,ne)*d - 2*phi(k0,n_c,n_s,ne))*np.exp(sigma(k0,n_s,ne)*(y-d)))

def Y_4(k0,n_c,n_a,n_s,ne,y,d,s):
    return K1(k0,n_c,n_s,ne)*(np.sin(kappa(k0,n_c,ne)*d)*np.exp(-sigma(k0,n_s,ne)*s) - np.sin(kappa(k0,n_c,ne)*d - 2*phi(k0,n_c,n_s,ne))*np.exp(sigma(k0,n_s,ne)*s))*np.exp(-gamma(k0,n_a,ne)*(y-d-s))

def dY_4(k0,n_c,n_a,n_s,ne,y,d,s):
    return -gamma(k0,n_a,ne)*K1(k0,n_c,n_s,ne)*(np.sin(kappa(k0,n_c,ne)*d)*np.exp(-sigma(k0,n_s,ne)*s) - np.sin(kappa(k0,n_c,ne)*d - 2*phi(k0,n_c,n_s,ne))*np.exp(sigma(k0,n_s,ne)*s))*np.exp(-gamma(k0,n_a,ne)*(y-d-s))



def YfieldFunc(YY,k0,n_c,n_a,n_s,ne,d,s, RegY):

    if RegY == 1:
        Y = Y_1(k0,n_c,n_s,ne,YY)
        dYdy = dY_1(k0,n_c,n_s,ne,YY)
    elif RegY == 2:
        Y = Y_2(k0,n_c,n_s,ne,YY)
        dYdy = dY_2(k0,n_c,n_s,ne,YY)
    elif RegY == 3:
        Y = Y_3(k0,n_c,n_s,ne,YY,d)
        dYdy = dY_3(k0,n_c,n_s,ne,YY,d)
    elif RegY == 4:
        Y = Y_4(k0,n_c,n_a,n_s,ne,YY,d,s)
        dYdy = dY_4(k0,n_c,n_a,n_s,ne,YY,d,s)

    return [Y,dYdy]
