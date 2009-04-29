#!/usr/bin/python
#bp.py
#Autor: Paulo Roberto Silla 

import math
import numpy as np
#import matplotlib.pyplot as grafico

class SOM:

    def __init__(self, x, it, topologia):
        
        self.x = x
        self.iteracoes = it
        self.alfa = 0.9
        self.w = np.zeros([topologia[0]*topologia[1], len(self.x)])
        
        self.w[0] = [2,2]
        self.w[1] = [3,2]
        self.w[2] = [2,1]
        self.w[3] = [1,3]
        
    def calcula_d(self, entrada):
        vencedor = 0
        d = np.zeros(len(self.w))
        for i in range(len(self.w)):
            for j in range(len(self.x[entrada])):
                d[i] += (self.x[entrada][j] - self.w[i][j])**2
            if (d[i] < d[vencedor]):
                vencedor = i
        print "d = %s" %d
        print "Vencedor: %d" %vencedor
        return vencedor

    def winner_take_all(self, i, entrada):
        for j in range (len(self.w[i])):
            self.w[i][j] += self.alfa * (self.x[entrada][j] - self.w[i][j])
        print "w = \n %s" %self.w
        
    def treina(self):
        for it in range (self.iteracoes):
            print "Iteracao: %d" %(it+1)
            for entrada in range (len(self.x)):
                print "Apresentando entrada: %s" %self.x[entrada]
                winner = self.calcula_d(entrada)
                self.winner_take_all(winner, entrada)
    
if __name__ == "__main__":
    x = [[0,3],[7,2]]
    topologia = [2,2]
    iteracoes = 2
    rede = SOM(x, iteracoes, topologia)
    rede.treina()
    
    