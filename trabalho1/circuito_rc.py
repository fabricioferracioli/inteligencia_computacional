#!/usr/bin/python
#Vc = V(1-e^-(t/R*c)) -> carga
#Vr = V(e^-(t/R*c)) -> descarga
#Valores iniciais
#R = 100 * 10^3
#C = 100 * 10^(-6)
#V = 10

import math
import matplotlib.pyplot as plt

R = 100000
c = 100 * 10**(-5)
V = 50
Vc = Vr = 0
den = R*c
x = []
y = []
for t in range(300):
    Volt = 0
    if t >= 9 and t < 200:
        expoente = -t/den
        Vc = V * (1 - math.exp(expoente))
        Volt = Vc
    elif t == 200:
        expoente = -(t - 200)/den
        Vr = Vc * (math.exp(expoente))
        Volt = Vr
    elif t > 200:
        expoente = -(t - 200)/den
        Vr = Vr * (math.exp(expoente))
        Volt = Vr
    y.append(Volt)
    x.append(t)

    print '[%f, %f]'%(Vc, Vr)
plt.plot(x,y)
plt.show()