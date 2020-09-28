import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

pi = math.pi       #Famoso pi

Emaxmais = 10      #Amplitude do campo incidente
FimaisGraus = 0    #Fase Finais (graus) da amplitude do campo incidente
Emaxmenos = 10     #Amplitude do campo refletido
FimenosGraus = 0   #Fase Fimenos (graus) da amplitude do campo refletido
nco = 2            #Numero de comprimentos de onda para o tracado do grafico.

# Chamei de ng o Numero de Graficos de ondas desejado. Comece com ng=1,
# depois faca ng = 2, 3, 4,...,18,...,36,... para voce ver a formacao da onda
ng=18 #Numero de graficos de ondas desejado.

# Chamei de step a defasagem em graus (wt) de um grafico para outro.
# Se o step for 5 graus, e.g., entao, para termos uma volta completa no circulo
# trigonometrico, teremos que fazer ng = 72, pois 72x5=360 graus, isto significa
# que a defasagem entre o primeiro e o ultimo grafico eh 360 graus. Um bom par
# eh ng=36 e step=10. (e.g.= exempli gratia (Latim) = por exemplo)
step = 20 #Defasagem em graus de um grafico para outro



####################### SOBRE O FILME ################
n = 2     #Numero de vezes de repeticao do filme
fps = 1   #Numero de quadros por segundo (frames por segundo) do filme


################### INICIO DOS CALCULOS ################
eps=2.2204e-16 #para evitar dividir por 0
SWR=(Emaxmais+Emaxmenos)/((Emaxmais-Emaxmenos)+eps)

modulo_Coeficiente_Reflexao = (SWR-1)/(SWR+1)

Perda_de_Retorno_dB= 20 * math.log10(modulo_Coeficiente_Reflexao)

Fimais = FimaisGraus*pi/180    #transforma graus para radianos
Fimenos = FimenosGraus*pi/180  #transforma graus para radianos
Bzmax = nco*2*pi               #transforma graus para radianos

################## INICIO DAS MATRIZES ################
Bz = np.linspace(0, Bzmax,100) #faz Bz (Beta_z) variar linearmente espacado de 0 a Bzmax
OndaIncidente = np.zeros([ng,len(Bz)]) #inicia a matriz que guardará o valor da onda incidente de todos os ng gráficos
OndaRefletida = np.zeros([ng,len(Bz)]) #inicia a matriz que guardará o valor da onda refletida de todos os ng gráficos
OndaTotal = np.zeros([ng,len(Bz)])     #inicia a matriz que guardará o valor total da onda para todos os ng gráficos

ims=[]
fig = plt.figure()
for k in range(ng):          # Equivale a variar o tempo. Cada valor de k equivale a um dado tempo (wt)
    wtGraus = step*(k-1)       # faz omega_t variar em graus, comecando em 0 graus
    wt = wtGraus*pi/180        # transforma omega_t de graus para radianos
    Envoltoria=np.sqrt(Emaxmais**2 + Emaxmenos**2 + 2*Emaxmais*Emaxmenos*np.cos(2*Bz+Fimenos-Fimais))

    #Armazena nas matrizes os valores dos graficos incidente, refletido e total para cada tempo
    OndaIncidente[k] = Emaxmais*np.cos(wt-Bz+Fimais)
    OndaRefletida[k] = Emaxmenos*np.cos(wt+Bz+Fimenos)
    OndaTotal[k]= OndaIncidente[k] + OndaRefletida[k] #Emaxmais*np.cos(wt-Bz+Fimais)+Emaxmenos*np.cos(wt+Bz+Fimenos)

    #Plota o grafico da envoltoria e das tres ondas, incidente, refletida e total, simultaneamente.
#    im = plt.imshow(OndaRefletida, animated=True)
#    ims.append([im])

#ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
#                                repeat_delay=1000)
    plt.plot(Bz,Envoltoria,'g--', Bz,-Envoltoria,'g--', label="Envoltória")
    plt.plot(Bz,OndaTotal[k],'b', label="Onda Total")
    plt.plot(Bz,OndaIncidente[k],'r--', label="Onda Incidente")
    plt.plot(Bz,OndaRefletida[k],'k--', label="Onda Refletida")

    legend = plt.legend(loc='upper right', shadow=True, fontsize='small')

    # Put a nicer background color on the legend.
    legend.get_frame().set_facecolor('C0')
    plt.show()




