####### Main
import math

from ydisper import yDisper
from xdisper import xDisper
from plotE import plotE

pi = math.pi
lbd = 1.32e-6
k0 = 2*pi/lbd

n_c = 3.50125
n_s = 3.5
n_a = 3
N = [n_c,n_s,n_a]

d = 6.5e-6
h = 3e-6
t = 1e-6
a = 8e-6
D = [d,h,t,a]

n_e = yDisper(k0, N, D)

#for i in range(len(n_e[:,1])):
n_eff = n_e[0,:]
print(n_eff)
u, w, beta = xDisper(n_eff, D, N, k0)
plotE(n_eff, 0, u, w, beta, D, N, k0)
