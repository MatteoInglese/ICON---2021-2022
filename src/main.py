# -*- coding: utf-8 -*-
from callers import *

#NAV MENU
print("*====== PROGETTO ICON 2021/2022 ======*\n")
print("Matteo Inglese 723032,\n"
      "Fabio Abbondanza 718937\n")
while(True):
    print("\nMenu di navigazione, digita un numero per accedere a un blocco del progetto:\n\n")
    print("[1] Classificatore del terreno")
    print("[2] Sistema esperto per malattie del caffe")
    print("[3] Ricerca percorso spedizione")
    print("[4] Generatore di turni per la consulenza")
    print("\n[0] Esci")

    choise = input("\n==> ")
    ch = float(choise)
    match ch:
        case 1:
            soil_classifier()
        case 2:
            exsys()
        case 3:
            graph_search()
        case 4:
            CSP_turnation()
        case 0:
            quit()
        case _:
            print("Input non valido!")