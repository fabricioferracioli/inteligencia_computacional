#!/usr/bin/python
# http://retina.anatomy.upenn.edu/~rob/lance/hodgkin_huxley.html
# http://icwww.epfl.ch/~gerstner/SPNM/node14.html
# http://thevirtualheart.org/HHindex.html
# http://www.afodor.net/HHModel.htm
# I = m^3 * h * G_NA * (E - E_NA) + n^4 * G_K * (E - E_K) + G_L * (E - E_L)

import math
import matplotlib.pyplot as plt

def getBh(v):
    return 1 / (math.exp((v + 30)/10) + 1)

def getAh(v):
    return 0.07 * math.exp( v / 20)

def getDh(v, h, dt):
    return (getAh(v) * (1 - h) - getBh(v) * h) * dt

def getBm(v):
    return 4 * math.exp( v / 18)

def getAm(v):
    return (0.1 * (v + 25)) / (math.exp( (v+25)/10  ) -1)

def getDm(v, m, dt):
    return (getAm(v) * (1 - m) - getBm(v) * m) * dt

def getBn(v):
    return 0.125 * math.exp( v / 80 )

def getAn(v):
    return (0.01 * (v + 10)) / (math.exp( (v + 10)/10 ) -1)

def getDn(v, n, dt):
    return (getAn(v) * (1 - n) - getBn(v) * n) * dt

def getN(v):
    return getAn(v) / (getAn(v) + getBn(v))

def getM(v):
    return getAm(v) / (getAm(v) + getBm(v))

def getH(v):
    return getAh(v) / (getAh(v) + getBh(v))

def setV(inV, vr):
    return -1 * inV - vr

def getV(v, vr):
    return -1 * (v + vr)

def plot_graph(x, y):
    plt.plot(x, y, linewidth=1.0)
    plt.xlabel('Tempo (s)')
    plt.ylabel('Voltagem (V)')
    plt.title('Potencial de acao - Neuronio')
    plt.grid(True)
    plt.show()

def hh(v, h, m, n):

    bh = getBh(v)
    ah = getAh(v)
    dh = getDh(v, h, dt)

    bm = getBm(v)
    am = getAm(v)
    dm = getDm(v, m, dt)

    bn = getBn(v)
    an = getAn(v)
    dn = getDn(v, n, dt)

    n4 = n**4
    m3h = m**3*h
    na_atual = gna * m3h * (v - vna)
    k_atual = gk * n4 * (v - vk)

    dv =  -1* dt * ( k_atual + na_atual + gl*(v - vl) ) / cm

    v += dv
    h += dh
    m += dm
    n += dn

    return [v, h, m, n]

tempo_total = 40
t_estimulo = 20


y = []
x = []
i=0

cargaEstimulo = 15
volt_repouso = 65

v = 0
dv = 0.0

cm =1.0
h = 0
m = 0
n = 0

vna = -115
vk = 12
vl = -10.613

gna = 120
gk = 36
gl = 0.3

dt = .005

bh = getBh(v)
ah = getAh(v)
dh = getDh(v, h, dt)

bm = getBm(v)
am = getAm(v)
dm = getDm(v, m, dt)

bn = getBn(v)
an = getAn(v)
dn = getDn(v, n, dt)

n = getN(v)
m = getM(v)
h = getH(v)

while (i < tempo_total):

    v, h, m, n = hh(v, h, m, n)

    x.append(i)
    y.append(getV(v, volt_repouso))

    # estimulo
    if ((abs(t_estimulo - i)) < .0025):
        v = setV(getV(v, volt_repouso) + cargaEstimulo, volt_repouso)

    i += dt

plot_graph(x,y)