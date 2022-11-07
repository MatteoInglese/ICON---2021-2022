from sklearn import tree
import joblib
import numpy as np
from expert_system import start_exsys
import Grafo as grf
from constraint import *
from CspConsulente import CspConsulente
from question_system import ask
from expert_system import start_exsys


def soil_classifier():
    # LOADING MODEL
    classifier = joblib.load("../models/dt.sav")

    # WELCOME MEX
    print("\n\n==========                                                         ==========\n")
    print("******     MINISTERO DELL'AGICOLTURA E DELLA SOVRANITA' ALIMENTARE     ******\n")
    print("==========                                                         ==========\n")

    print("Sistema di classificazione del terreno.")
    print("Assicurati di avere a disposizione le analisi climatiche e del terreno!")

    choice = True
    while(choice == True):
        # INSERT CLIMATIC DATA
        print("\nInserirsci i dati climatici")
        temperature = input("Temperatura (media, in gradi Celsius): ")
        humidity = input("Umidità: ")
        rainfall = input("Precipitazioni (annuali, in mm): \n")

        # INSERT SOIL DATA
        print("Inserirsci i risultati delle analisi del terreno")
        n = input("Percentuale di Azoto: ")
        p = input("Percentuale di Fosforo: ")
        k = input("Percentuale di Potassio: ")
        ph = input("Ph: \n")

        # CLASSIFY THE SOIL
        tmp = [n, p, k, temperature, humidity, ph, rainfall]
        x = (np.array(tmp)).reshape(1, -1)
        soil_type = classifier.predict(x)
        print("Il terreno è adatto alle colture di ", (np.array2string(soil_type)).upper())
        choice = ask("\nVuoi eseguire un'altra analisi?")

def exsys():
    print("<=== SISTEMA DI DIAGNOSI MALATTIE FOGLIARI ===>")

    choice = True
    while (choice == True):
        start_exsys()
        choice = ask("\nVuoi eseguire un'altra diagnosi?")

def graph_search():
    print("\n\n<<<<<<<< ARASAKA EXPEDITION >>>>>>>>")

    print("\nBenvenuto nel sistema logistico dell'Arasaka!")

    choice = True
    while (choice == True):
        print("Seleziona il criterio da usare nel calcolo del percorso ottimale per la tua spedizione:\n")

        print("[1] Costo della spedizione")
        print("[2] Tempi di consegna")

        preferenza = input("\n==>")
        while preferenza != "1" and preferenza != "2":
            preferenza = input("Input non valido.")

        grf.mostraScali()

        destinatario = input("Inserisci lo scalo di partenza (es. Italia): \n")
        provenienza = input("Inserisci lo scalo di arrivo (es. Giappone): \n")

        if preferenza == "1":
            prezzoiniziale = input(
                "Inserisci il prezzo con cui il prodotto viene acquistato nella nazione di provenienza: \n")
            prezzoiniziale = int(prezzoiniziale)
            grf.trovaPercorso(prezzoiniziale, destinatario, provenienza, preferenza)
        if preferenza == "2":
            grf.trovaPercorso(0, destinatario, provenienza, preferenza)

        choice = ask("\nVuoi calcolare un'altra spedizione?")

def CSP_turnation():
    print("\n\n==========                                                         ==========\n")
    print("******     MINISTERO DELL'AGICOLTURA E DELLA SOVRANITA' ALIMENTARE     ******\n")
    print("==========                                                         ==========\n")

    print("SISTEMA DI TURNAZIONE PER LE CONSULENZE E LE ANALISI\n")

    c = CspConsulente()  # Crea il csp
    n = c.getTurniDisponibili()  # variabile a cui assegno il numero di turni max, e nel farlo gli visualizza
    turno = int(input("Digita il numero del turno corrispondente al giorno e orario in cui vuole la consulenza:\n"))
    while turno > n or turno < 0:
        turno = int(input("E stato inserito un numero non valido, riprova:\n"))

    c.printTurnoScelto(turno)  # visualizza la scelta fatta dall'utente