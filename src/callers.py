from sklearn import tree
import joblib
import numpy as np
from expert_system import start_exsys
import Grafo as grf
from constraint import *
from CspConsulente import CspConsulente


def soil_classifier():
    # LOADING MODEL
    classifier = joblib.load("../models/dt.sav")

    # WELCOME MEX
    print("Benvenuto nel sistema di classificazione del suolo di Ninomae!\n")

    # INSERT CLIMATIC DATA
    print("Inserirsci i dati climatici:\n")
    temperature = input("Temperatura (media, in gradi Celsius): \n")
    humidity = input("Umidità: \n")
    rainfall = input("Precipitazioni (annuali, in mm): \n")

    # INSERT SOIL DATA
    print("Inserirsci i risultati delle analisi del terreno:\n")
    n = input("Percentuale di Azoto: \n")
    p = input("Percentuale di Fosforo: \n")
    k = input("Percentuale di Potassio: \n")
    ph = input("Ph: \n")

    # CLASSIFY THE SOIL
    tmp = [n, p, k, temperature, humidity, ph, rainfall]
    x = (np.array(tmp)).reshape(1, -1)
    soil_type = classifier.predict(x)
    print("Il terreno è adatto alle colture di ", (np.array2string(soil_type)).upper())

def graph_serach():
    print(
        "E interessato a sapere il percorso che fara il prodotto se lo acquista dall'estero e il suo prezzo finale? \n")
    print("O è più interessato al tempo che servirà per spedirlo?\n")

    preferenza = input("inserisci 1 per il prezzo, o 2 per il tempo\n")
    while preferenza != "1" and preferenza != "2":
        preferenza = input("Hai sbagliato, inserisci 1 per il prezzo, o 2 per il tempo\n")

    destinatario = input("Inserisci la nazione in cui verra consegnato (es. Italia): \n")
    provenienza = input("Inserisci la nazione di provenienza (es. Giappone): \n")

    if preferenza == "1":
        prezzoiniziale = input(
            "Inserisci il prezzo con cui il prodotto viene acquistato nella nazione di provenienza: \n")
        prezzoiniziale = int(prezzoiniziale)
        grf.trovaPercorso(prezzoiniziale, destinatario, provenienza, preferenza)
    if preferenza == "2":
        grf.trovaPercorso(0, destinatario, provenienza, preferenza)

        # grf.trovaPercorso(10,"italia", "giappone", "1")  #Riga di test rapido per l'A*

def CSP_turnation():
    # Blocco per il csp
    c = CspConsulente()  # Crea il csp
    n = c.getTurniDisponibili()  # variabile a cui assegno il numero di turni max, e nel farlo gli visualizza
    turno = int(input("Digita il numero del turno corrispondente al giorno e orario in cui vuole la consulenza:\n"))
    while turno > n or turno < 0:
        turno = int(input("E stato inserito un numero non valido, riprova:\n"))

    c.printTurnoScelto(turno)  # visualizza la scelta fatta dall'utente