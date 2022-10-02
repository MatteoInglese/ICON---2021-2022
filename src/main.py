# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 11:07:21 2022

@author: lncln
"""
from sklearn import tree
import joblib
import numpy as np
from expert_system import start_exsys
import Grafo as grf

def soil_classifier():
    
    
    #LOADING MODEL
    classifier = joblib.load("../models/dt.sav")
    
    
    #WELCOME MEX
    print("Benvenuto nel sistema di classificazione del suolo di Inomae!\n")
    
    
    #INSERT CLIMATIC DATA
    print("Inserirsci i dati climatici:\n")
    temperature = input("Temperatura (media, in gradi Celsius): \n")
    humidity = input("Umidità: \n")
    rainfall = input("Precipitazioni (annuali, in mm): \n")
    
    
    #INSERT SOIL DATA
    print("Inserirsci i risultati delle analisi del terreno:\n")
    n = input("Percentuale di Azoto: \n")
    p = input("Percentuale di Fosforo: \n")
    k = input("Percentuale di Potassio: \n")
    ph = input("Ph: \n")
    
    
    #CLASSIFY THE SOIL
    tmp = [n, p, k, temperature, humidity, ph, rainfall]
    x = (np.array(tmp)).reshape(1, -1)
    soil_type = classifier.predict(x)
    print("Il terreno è adatto alle colture di ", (np.array2string(soil_type)).upper())
    
    #schtella
    print("E interessato a sapere il percorso che fara il prodotto se lo acquista dall'estero? \n")
    destinatario = input("Inserisci la nazione in cui verra consegnato (es. Italia): \n")
    provenienza = input("Inserisci la nazione di provenienza (es. Giappone): \n")
    prezzoiniziale = input("Inserisci il prezzo con cui il prodotto viene acquistato nella nazione di provenienza: \n")
    prezzoiniziale = int(prezzoiniziale)
    grf.trovaPercorso(prezzoiniziale , destinatario, provenienza)
#90,42,43,20.87974371,82.00274423,6.502985292000001,202.9355362,
#85,58,41,21.77046169,80.31964408,7.038096361,226.6555374
soil_classifier()