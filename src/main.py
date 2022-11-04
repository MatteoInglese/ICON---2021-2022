# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 11:07:21 2022

@author: lncln
"""
from callers import *
from expert_system import start_exsys

#NAV MENU
print("*====== PROGETTO ICON 2021/2022 ======*\n")
print("\nMatteo Inglese 123456789,\n"
      "Fabio Abbondanza 123456789\n")
while(True):
    print("Menu di navigazione, digita un numero per accedere a un blocco:\n\n")
    print("[1] Classificatore del terreno")
    print("[2] Sistema esperto per malattie del caffe")
    print("[3] Ricerca percorso spedizione")
    print("[4] CSP")
    print("\n[0] Esci")

    choise = input("==> ")
    ch = float(choise)
    match ch:
        case 1:
            soil_classifier()
        case 2:
            start_exsys()
        case 3:
            graph_search()
        case 4:
            CSP_turnation()
        case 0:
            quit()
        case _:
            print("Input non valido!")