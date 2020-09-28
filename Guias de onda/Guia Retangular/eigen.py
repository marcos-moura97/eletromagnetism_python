####### Eigen
import numpy as np
import math


def kappa(k0,n_c,ne):
    return k0*np.sqrt(n_c**2 - ne**2)

def sigma(k0,n_s,ne):
    return k0*np.sqrt(ne**2 - n_s**2)

def gamma(k0,n_a,ne):
    return k0*np.sqrt(ne**2 - n_a**2)

def phi(k0,n_c,n_s,ne):
    #return np.arctan2(abs(sigma(k0,n_c,ne)),abs(kappa(k0,n_s,ne)))
    return np.arctan((sigma(k0,n_c,ne)/kappa(k0,n_s,ne)))

def psi(k0,n_s,n_a,ne):
    return np.arctanh(sigma(k0,n_s,ne)/gamma(k0,n_a,ne))
