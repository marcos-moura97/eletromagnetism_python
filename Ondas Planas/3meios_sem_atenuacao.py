# Este programa calcula os campos totais nos tres meios. A onda eletromagnetica
# incide a partir do meio 1. O meio 3 eh infinito e, portanto, nao ha reflexao neste meio.
# A incidencia eh plana, i.e, normal ou perpendicular. A espessura 'd' do meio 2 eh dada
# em numero de comprimentos de onda (nco).

import math
import numpy as np
import matplotlib.pyplot as plt

#############################ENTRADA DE DADOS###########################################

pi = math.pi
# Essas dimensoes nao importam para o aumento de temperatura
# dimensao a
a=8e-2
a_cm=a*100

# dimensao b
b=5e-2
b_cm=b*100


Area = a*b # area em metros quadrados

#Frequencia em Hz. A frequencia eh UNICA. O que muda de um
#meio para o outro eh o comprimento de onda e a velocidade de fase.
f=2.45e9 #Frequencia em Hz, frequencia do forno de micro ondas = 2.45 GHz = 2.45e9

m_Emaxmais_=20000  #Emaxmais no meio 1, amplitude do campo incidente
fimaisgrau_=0      #Fase de Emaxmais no meio 1 em graus, pode ser = 0

# Os dados abaixo sao usados apenas para calcular o aquecimento do meio 2
Tempo = 60              #Tempo de exposicao da onda eletromagnetica em segundos
Densidade = 1000        #Densidade do meio 2 em kg por metro cubico
CalorEspecifico = 4180  #Calor Especifico do meio 2 em Joule/(kg ?C)

d2_sobre_Lambda2 = 2.11     #numero de lambdas_2 do meio 2
d1_sobre_Lambda1 = 0.75     #numero de lambdas_1 para tracar o grafico no meio 1
d3_sobre_Lambda3 = 0.75     #numero de lambdas_3 para tracar o grafico no meio 3

nt=5                        #numero de tempos, onde cada tempo correpondente a um grafico
wt_final=30*pi/180
wt_inicial=100*pi/180


#################################### PARAMETROS ELETRICOS DOS 3 MEIOS ############################
epsilonrelativo=np.zeros(3)
mirelativo=np.zeros(3)
sigma=np.zeros(3)
# Entre com os parametros do Meio 1
epsilonrelativo[0]=1    #permissividade relativa do meio 1
mirelativo[0]=1         #permeabilidade relativa do meio 1
sigma[0]=0              #condutividade do meio 1

# Entre com os parametros do Meio 2
# condutividade da agua potavel 500e-6, agua do mar 50000e-6
epsilonrelativo[1]=81   #permissividade relativa do meio 2
mirelativo[1]=1         #permeabilidade relativa do meio 2
sigma[1]=0.6            #condutividade do meio 2

# Entre com os parametros do Meio 3
epsilonrelativo[2]=1    #permissividade relativa do meio 3
mirelativo[2]=1         #permeabilidade relativa do meio 3
sigma[2]=0              #condutividade do meio 3


#################################### INICIO DOS CALCULOS ##########################################

fimais_ = pi / 180 * fimaisgrau_              #transforma fimais de graus para radianos
Emaxmais_ = m_Emaxmais_ * np.exp(1j*fimais_)  #Emaxmais é um número complexo
epsilonzero=1e-9/(36*pi)
mizero=4*pi*1e-7
w=2*pi*f                                     #omega=w=frequencia angular (rd/s)

n_meios= np.arange(1,4,dtype=complex)        #faz n=1, 2 e 3 nas expressoes abaixo, i.e., varre os 3 meios

######### Inicio das matrizes

epsilon = np.zeros(3,dtype=complex)
mi = np.zeros(3,dtype=complex)
sigmasobre = np.zeros(3,dtype=complex)
fator1 = np.zeros(3,dtype=complex)
raiz1 = np.zeros(3,dtype=complex)
raiz2 = np.zeros(3,dtype=complex)
raiz3 = np.zeros(3,dtype=complex)
alfa = np.zeros(3,dtype=complex)
beta = np.zeros(3,dtype=complex)
gama = np.zeros(3,dtype=complex)
raiz4 = np.zeros(3,dtype=complex)
raiz5 = np.zeros(3,dtype=complex)
modulo_eta = np.zeros(3,dtype=complex)
teta = np.zeros(3,dtype=complex)
tetagrau = np.zeros(3,dtype=complex)
eta = np.zeros(3,dtype=complex)
lbd = np.zeros(3,dtype=complex)
velocidadefase = np.zeros(3,dtype=complex)

for n in range(3):
    epsilonrelativo3meios=epsilonrelativo[n]
    sigma3meios=sigma[n]
    epsilon[n]=epsilonrelativo[n]*epsilonzero
    mi[n]=mirelativo[n]*mizero
    sigmasobre[n]=sigma[n]/(w*epsilon[n])
    fator1[n]=w*np.sqrt(mi[n]*epsilon[n])/math.sqrt(2)
    raiz1[n]=np.sqrt(1+sigmasobre[n] **2)
    raiz2[n]=np.sqrt(raiz1[n]-1)
    raiz3[n]=np.sqrt(raiz1[n]+1)
    alfa[n]=fator1[n]*raiz2[n]           #alfa = fator de atenuacao
    beta[n]=fator1[n]*raiz3[n]           #beta = fator de fase
    gama[n]=alfa[n] + 1j*beta[n]         #gama = alfa + j beta

    raiz4[n]=np.sqrt(mi[n]/epsilon[n])
    raiz5[n]=np.sqrt(raiz1[n])

    modulo_eta[n]=raiz4[n]/raiz5[n]                 #modulo da impedancia intrinseca
    teta[n]=0.5*math.atan2(sigma[n],(w*epsilon[n]))     #fase da impedancia intrinseca
    tetagrau[n]=teta[n] *180/pi
    eta[n]=modulo_eta[n]*np.exp(1j*teta[n])         #eta=impedancia intrinseca, com modulo e fase

    lbd[n]=2*pi/beta[n]                             #comprimento de onda
    velocidadefase[n]=w/beta[n]                     #velocidade de fase = veloc. da onda incidente ou da refletida


###################################################
d=d2_sobre_Lambda2*lbd[1]
d1=-d1_sobre_Lambda1*lbd[0]
d3=d3_sobre_Lambda3*lbd[2]
print('d2 = ',(d.real*100),' cm')
S1_sem_reflexao=m_Emaxmais_**2/(240*pi)
###################################################


############ Calculo dos coeficientes de reflexao nos 3 meios, a comecar do meio 3 ############

Z2em0=eta[2]                                                   #impedancia no meio 2 em z=0
Creflexao2em0=(Z2em0-eta[1]) / (Z2em0+eta[1])                  #coef. de reflexao no meio 2 em z=0
modulo_Creflexao2em0 = abs(Creflexao2em0)                      #modulo do coeficiente de reflexao no meio 2 em z=0
fase_Creflexao2em0 = np.log(Creflexao2em0)                     #fase do coeficiente de reflexao no meio 2 em z=0
fase_Creflexao2em0 = fase_Creflexao2em0.imag
fase_Creflexao2em0grau= fase_Creflexao2em0 *180/pi

Creflexao2em_d=Creflexao2em0 * np.exp(-2 * gama[1] *d)         #coef. de reflexao no meio 2 em z=-d
modulo_Creflexao2em_d = abs(Creflexao2em_d)
fase_Creflexao2em_d = np.log(Creflexao2em_d)
fase_Creflexao2em_d = fase_Creflexao2em_d.imag
fase_Creflexao2em_dgrau=fase_Creflexao2em_d*180/pi
Z2em_d = eta[1] * (1+Creflexao2em_d) / (1-Creflexao2em_d)      #impedancia no meio 2 em z=-d
Z1em0 = Z2em_d                                                 #impedancia no meio 1 em z=0
Creflexao1em0 = (Z1em0-eta[0]) / (Z1em0+eta[0])
modulo_Creflexao1em0 = abs(Creflexao1em0)
fase_Creflexao1em0 = np.log(Creflexao1em0)
fase_Creflexao1em0 = fase_Creflexao1em0.imag
fase_Creflexao1em0grau=fase_Creflexao1em0*180/pi

################ Calcula a amplitude do campo refletido no meio 1 ###################
Emaxmais = np.zeros(3,dtype=complex)
Emaxmais[0] = Emaxmais_
Emaxmenos = np.zeros(3,dtype=complex)
m_Emaxmenos = np.zeros(3,dtype=complex)
fimenos = np.zeros(3,dtype=complex)
fimenosgrau = np.zeros(3,dtype=complex)
fimais = np.zeros(3,dtype=complex)
fimais[0] = fimais_
fimaisgrau = np.zeros(3,dtype=complex)
fimaisgrau[0] = fimaisgrau_
m_Emaxmais = np.zeros(3,dtype=complex)
m_Emaxmais[0] = m_Emaxmais_


for n in range(3):
    Emaxmenos[0] = Emaxmais[0] * Creflexao1em0
    m_Emaxmenos[0] = abs(Emaxmenos[0])                       #modulo de Emaxmenos no meio 1
    fimenos[0] = np.log(Emaxmenos[0])                        #fase de Emaxmenos no meio 1
    fimenos[0] = fimenos[0].imag
    fimenosgrau[0]=fimenos[0] *180/pi
    ######### Calcula o campo total no meio 1 em z=0 ##########
    E1em0 = Emaxmais[0] + Emaxmenos[0]
    ## Calcula as amplitudes do campo incidente e refletido no meio 2
    E2em_d = E1em0                                          #continuidade do campo total na interface entre os meios 1 e 2
    Emaxmais[1] = (E2em_d * np.exp(-gama[1] * d)) / (1+Creflexao2em_d)
    m_Emaxmais[1] = abs(Emaxmais[1])
    fimais[1] = np.log(Emaxmais[1])
    fimais[1] = fimais[1].imag
    fimaisgrau[1]=fimais[1]*180/pi
    Emaxmenos[1] = Emaxmais[1]* Creflexao2em0
    m_Emaxmenos[1] = abs(Emaxmenos[1])
    fimenos[1] = np.log(Emaxmenos[1])
    fimenos[1] = fimenos[1].imag
    fimenosgrau[1]=fimenos[1]*180/pi
    ############ Calcula o campo total no meio 2 em z=0
    E2em0 = Emaxmais[1] + Emaxmenos[1]
    ############## Calcula a amplitude do campo incidente no meio 3 (so tem incidente)
    Emaxmais[2] = E2em0
    m_Emaxmais[2] = abs(Emaxmais[2])
    fimais[2] = np.log(Emaxmais[2])
    fimais[2] = fimais[2].imag
    fimaisgrau[2]=fimais[2]*180/pi
    Emaxmenos[2] = 0
    m_Emaxmenos[2] = 0
    fimenos[2] = 0
    fimenosgrau[2]=fimenos[2]*180/pi

############### ESCREVE E PLOTA AS EQUACOES DE ONDA E ENVOLTORIAS NOS 3 MEIOS ############

#figure % abre uma tela para tracar o grafico das ondas

passo = (wt_final-wt_inicial)/(nt-1)

#axis([(d1-d)   d3    -inf    inf])

######## meio 1 #########
n=0
for wt in np.arange(wt_inicial, wt_final, passo):
    z = np.linspace((d1-d), -d, 4000)
    z1= z+d
    e = m_Emaxmais[n] * np.exp(-alfa[n] *z1) * np.cos(wt-beta[n]*z1+fimais[n]) + m_Emaxmenos[n] * np.exp(alfa[n]*z1) * np.cos(wt+beta[n]*z1+fimenos[n])
    plt.plot(z,e,'b')

    Emais=m_Emaxmais[n]*np.exp(-alfa[n]*z1)
    Emenos=m_Emaxmenos[n]*np.exp(alfa[n]*z1)
    env=np.sqrt(Emais**2 + Emenos**2 + 2*Emais*Emenos*np.cos(2*beta[n]*z1+fimenos[n]-fimais[n]))
    plt.plot(z,env,'k',z,-env,'k')

maxEnvoltoria_1=max(env)

######## meio 2 #########
n = 1

for wt in np.arange(wt_inicial, wt_final, passo):
    z = np.linspace(-d, 0, 4000)
    e = m_Emaxmais[n] * np.exp(-alfa[n] *z) * np.cos(wt-beta[n]*z+fimais[n]) + m_Emaxmenos[n] * np.exp(alfa[n]*z) * np.cos(wt+beta[n]*z+fimenos[n])
    plt.plot(z,e,'b')
    Emais = m_Emaxmais[n]*np.exp(-alfa[n]*z)
    Emenos = m_Emaxmenos[n]*np.exp(alfa[n]*z)
    env=np.sqrt(Emais**2 + Emenos**2 + 2*Emais*Emenos*np.cos(2*beta[n]*z+fimenos[n]-fimais[n]))
    plt.plot(z,env,'r',z,-env,'r')

maxEnvoltoria_2=max(env)

####################### colore o meio 3 #######################
if maxEnvoltoria_1>maxEnvoltoria_2:
    M=maxEnvoltoria_1

else:
    M=maxEnvoltoria_2

cor=[.5,.5,1]
X=[ 0,0,-d,-d,0]
Y=[-M,M,M,-M,-M]
plt.fill(X,Y,facecolor=cor,alpha=0.5,edgecolor='b',linewidth=3)

d_str = 'd = '+str(d.real/lbd[1].real)+' λ'
plt.text(-d/2, -0.9*M , d_str )

######## meio 3 #########

n = 2
for wt in np.arange(wt_inicial, wt_final, passo):
    z = np.linspace(0, d3, 4000)
    e = m_Emaxmais[n] * np.exp(-alfa[n] *z) * np.cos(wt-beta[n]*z+fimais[n]) + m_Emaxmenos[n] * np.exp(alfa[n]*z) * np.cos(wt+beta[n]*z+fimenos[n])
    plt.plot(z,e,'b')
    Emais=m_Emaxmais[n]*np.exp(-alfa[n]*z)
    Emenos=m_Emaxmenos[n]*np.exp(alfa[n]*z)
    env=np.sqrt(Emais**2 + Emenos**2 + 2*Emais*Emenos*np.cos(2*beta[n]*z+fimenos[n]-fimais[n]))
    plt.plot(z,env,'k',z,-env,'k')

plt.title('Campo Elétrico Total nos 3 meios')
plt.xlabel('z  (m)')
plt.ylabel('E  (V/m)')
plt.grid()
plt.show()

########### CALCULO DO VETOR DE POYNTING ou DENSIDADE DE POTENCIA (S) ###########

##### Meio 1
n=0
z = np.linspace((d1-d), -d)
z1= z+d
E = Emaxmais[n]* np.exp(-gama[n]*z1) + Emaxmenos[n]* np.exp(gama[n]*z1)  #Campo E
H = Emaxmais[n]* np.exp(-gama[n]*z1) / eta[n] - Emaxmenos[n]* np.exp(gama[n]*z1) / eta[n]  #Campo H
Creflexao1=Creflexao1em0 * np.exp(2 * gama[n]*z1)    #calcula os coeficientes de reflexão no meio 1

S = 0.5 * (E*np.conj(H)).real #Vetor de Poynting S = 1/2 *(E x H)

plt.plot(z*100,S,'b')
plt.grid()

##### Meio 2
n=1
z = np.linspace(-d, 0, 200);
E = Emaxmais[n]* np.exp(-gama[n]*z) + Emaxmenos[n]* np.exp(gama[n]*z)  #Campo E
H = Emaxmais[n]* np.exp(-gama[n]*z) / eta[n] - Emaxmenos[n]* np.exp(gama[n]*z) / eta[n]  #Campo H

S = 0.5 * (E*np.conj(H)).real #Vetor de Poynting S = 1/2 *(E x H)

plt.plot(z*100,S,'r')

##### Meio 3
n = 2
z = np.linspace(0, d3)
E = Emaxmais[n]* np.exp(-gama[n]*z) + Emaxmenos[n]* np.exp(gama[n]*z)  #Campo E
H = Emaxmais[n]* np.exp(-gama[n]*z) / eta[n] - Emaxmenos[n]* np.exp(gama[n]*z) / eta[n]  #Campo H

S = 0.5 * (E*np.conj(H)).real #Vetor de Poynting S = 1/2 *(E x H)

plt.plot(z*100,S,'b')

plt.title('Módulo do Vetor de Poynting |S|')
plt.xlabel('z  (cm)')
plt.ylabel('|S|  (V/m)')
plt.show()

