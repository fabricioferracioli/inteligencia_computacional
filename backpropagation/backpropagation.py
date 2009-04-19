#!/usr/bin/python

from math import exp

#neuronios na camada externa
A = 3

#neuronios na camada oculta
B = 3

#neuronios na camada de saida
C = 1

#entradas [bias, x1, x2]
x = [[1,1,0], [1,0,0], [1,0,1], [1,1,1]]

#saidas esperadas
y = [0,1,0,1]

#w1ij
w1 = [[0,-1],[2,1],[-2,3]]

#w2ij
w2 = [[-1],[3],[-2]]

#hj
h = [1,0,0]

o = C*[0]
d2j = C*[0]
d1j = B*[1]

dw2 = [[0],[0],[0]]
dw1 = [3*[0], 3*[0], 3*[0]]

Eta = 1

def hj(entrada):
    for j in range(1,B):
        expoente = 0
        for i in range(A):
            expoente += w1[i][j-1] * x[entrada][i]
        h[j] = 1 / (1 + exp(-expoente))

def oj():
    for j in range(C):
        expoente = 0
        for i in range(B):
            expoente += w2[i][j] * h[i]
        o[j] = 1 / (1 + exp(-expoente))

def delta2j():
    for j in range(C):
        d2j[j] = o[j] * (1 - o[j]) * (y[j] - o[j])

def delta1j():
    for j in range(1,B):
        somatorio = 0
        for i in range(C):
            somatorio += d2j[i] * w2[j][i]
        d1j[j] = h[j] * (1 - h[j]) * somatorio

def deltaw2ij():
    for i in range(B):
        for j in range(C):
            dw2[i][j] = Eta * d2j[j] * h[i]
            w2[i][j] += dw2[i][j]

def deltaw1ij(entrada):
    for i in range(A):
        for j in range(1,B):
            dw1[i][j-1] = Eta * d1j[j] * x[entrada][i]
            print '%f * %f * %f'%(Eta, d1j[j], x[entrada][i])
            w1[i][j-1] += dw1[i][j-1]

hj(0)
oj()
delta2j()
delta1j()
deltaw2ij()
deltaw1ij(0)

print 'h = %s\n'%(h)
print 'o = %s\n'%(o)
print 'delta2 = %s\n'%(d2j)
print 'delta1 = %s\n'%(d1j)
print 'delta w2 = %s\n'%(dw2)
print 'w2 = %s\n'%(w2)
print 'delta w1 = %s\n'%(dw1)
print 'w1 = %s\n'%(w1)