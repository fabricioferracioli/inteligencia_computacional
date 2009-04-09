#!/usr/bin/python
# http://retina.anatomy.upenn.edu/~rob/lance/hodgkin_huxley.html
# http://icwww.epfl.ch/~gerstner/SPNM/node14.html
# http://thevirtualheart.org/HHindex.html
# I = m^3 * h * G_NA * (E - E_NA) + n^4 * G_K * (E - E_K) + G_L * (E - E_L)

#I : the total ionic current across the membrane
#m : the probability that 1 of the 3 required activation particles has contributed to the activation of the Na gate (m^3 : the probability that all 3 activation particles have produced an open channel)
#h : the probability that the 1 inactivation particle has not caused the Na gate to close
#G_Na : Maximum possible Sodium Conductance (about 120 mOhms^-1/cm2)
#E : total membrane potential (about -60 mV)
#E_Na : Na membrane potential (about 55 mV)
#n : the probability that 1 of 4 activation particles has influenced the state of the K gate.
#G_K : Maximum possible Potassium Conductance (about 36 mOhms^-1/cm2)
#E_K : K membrane potential (about -72 mV)
#G_L : Maximum possible Leakage Conductance (about .3 mOhms^-1/cm2)
#E_L : Leakage membrane potential (about -50 mV)

#Valores iniciais
# G_Na    120 mOhms^-1/cm2
# G_K 36 mOhms^-1/cm2
# G_L .3 mOhms^-1/cm2
# E   -60 mV
# E_Na    55 mV
# E_K -72 mV
# E_L -50 mV

G = {'NA': (120 * 10**(-6))**(-1),'K': (36 * 10**(-6))**(-1),'L': (0.3 * 10**(-6))**(-1)}
E = {0: -60 * 10**(-6), 'NA': 55 * 10**(-6), 'K': -72 * 10**(-6), 'L': -50 * 10**(-6)}
