# -*- coding: utf-8 -*-
from constraint import *


class CspConsulente():

    #costruttore della classe
    #creo il "problema" con problem() dato dalla libreria constraint
    #in seguito aggiungo le variabili con i loro domini
    #e poi aggiungo i vincoli
    
    def __init__(self):
        self.consulente = Problem()
        
        self.consulente.addVariable("giorni",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
        self.consulente.addVariable("disponibilitaStrumenti",["Disponibile","Non Disponibile"])
        self.consulente.addVariable("Orario",["mattina","pomeriggio"])
        self.consulente.addVariable("Auto",["si","no"])
        
        self.consulente.addConstraint(lambda giorni, disponibilitaStrumenti: giorni >=3 and giorni <=28 if disponibilitaStrumenti == "Disponibile" else None,["giorni","disponibilitaStrumenti"])
        self.consulente.addConstraint(lambda giorni, Orario: giorni == 21 if Orario == "mattina" else giorni >=21 and giorni <=30 if Orario == "pomeriggio" else None,["giorni","Orario"])
        self.consulente.addConstraint(lambda giorni, Auto: giorni == 21 or giorni ==27 or giorni ==23 if Auto == "si"  else None,["giorni","Auto"])
        
        self.solution = None    #lista delle soluzioni


    # trova le soluzioni al problema
    # e le visualizza in modo che sia interpretabile per l'utente
    # infine, restituisce il numero massimo di turni disponibili
    def getTurniDisponibili(self):

        self.solution = self.consulente.getSolutions()  #restituisce la lista delle soluzioni
        numTurni = 0

        if len(self.solution) > 0:

            print("Turni disponibili per la consulenza\n")

            while numTurni < len(self.solution):
                
                print("Turno [%d], Giorno: %d, Orario: %s\n" %(numTurni,self.solution[numTurni]['giorni'],self.solution[numTurni]['Orario']))
                numTurni = numTurni + 1
            
            numTurni = numTurni-1
               
        else:
            print("Non c'è nessun turno disponibilità\n")

        return numTurni

    
    # visualizza il turno che è stato scelto dall'utente
    # il parametro n passato come argomento è il numero massimo di turni disponibili
    # dato da getTurniDisponibili()
    def printTurnoScelto(self, n):

        if n >= 0 and n < len(self.solution):
            print("Hai selezionato il turno: [%d], Giorno: %d, Orario: %s\n\n"%(n,self.solution[n]['giorni'],self.solution[n]['Orario']))