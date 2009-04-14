import math;

x =[[1, 0, 0], [1, 0, 1], [1, 1, 1], [1, 1, 0]]
p = [-1, -1, 1, 1]
TETA = 0
GAMA = 0.1
w = [0.0, 0.0, 0.0]

#Calcula o novo w
def calcula_deltaw(o,i):
    print "Recalculando w"
    for j in range(3):
        w[j] = w[j] + (GAMA*(p[i]-o)*x[i][j])

if __name__== "__main__":
    i = 0
    while i < 4:
        print "Apresentando a entrada %d para a rede" %(i+1)

        recalc = False
        #fica no while ate encontrar a saida desejada (o == p[i])
        while True:
            a = ((x[i][0]*w[0]) + (x[i][1]*w[1]) + (x[i][2]*w[2])) - TETA
            if a >= 0.0:
                o = 1
            else:
                o = -1
            #verifica se a saida encontrada eh igual a desejada
            if o == p[i]:
                #verifica se w foi recalculado para a entrada corrente
                if recalc:
                    #volta para a primeira entrada
                    i = 0
                else:
                    #continua para a proxima entrada
                    i +=1
                break
            #se nao for, recalcula o w e marca para que todas as entradas sejam 
            #recalculadas com o novo w
            else:
                recalc = True
                calcula_deltaw(o,i)
    print "w final calculado: %s" %w

    
            
                
            

