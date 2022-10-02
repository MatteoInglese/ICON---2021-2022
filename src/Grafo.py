import numpy as np

class Grafo:
    #Inizializza grafo
    def __init__(self, grafoDict=None, orientato=True):
        self.grafoDict = grafoDict or {}
        self.orientato = orientato
        self.numero = 0
        if not orientato:
            self.conversioneNonOrientato()
            
    #Converte un grafo orientato in non orientato
    def conversioneNonOrientato(self):
        for a in list(self.grafoDict.keys()):
            for (b, dist) in self.grafoDict[a].items():
                self.grafoDict.setdefault(b, {})[a] = dist
                
    #Aggiunge un collegamento tra nodo A e B con un relativo peso, nel caso di grafo non orientato, aggiunge un ulteriore
    #collegamente da nodo B a nodo A
    def connessione(self, A, B, distanza=1):
        self.grafoDict.setdefault(A, {})[B] = distanza
        if not self.orientato:
            self.grafoDict.setdefault(B, {})[A] = distanza
            
    #Prende i nodi adiacenti
    def get(self, a, b=None):
        links = self.grafoDict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
        
    #Restituisce lista di nodi
    def nodi(self):
        s1 = set([k for k in self.grafoDict.keys()])
        s2 = set([k2 for v in self.grafoDict.values() for k2, v2 in v.items()])
        nodi = s1.union(s2)
        return list(nodi)
    
    #Rimuove dal grafo una regione (nodo)
    def rimuovi(self, listaRegioni, nomeRegione):
        for i in range (len(listaRegioni)):
            if(self.grafoDict[listaRegioni[i].name].get(nomeRegione) != None):
               self.grafoDict[listaRegioni[i].name].pop(nomeRegione)
        self.grafoDict.pop(nomeRegione)
    
    def PrezzoFinale(self, numero):
        self.numero = numero
    
class Nodo:
    #Inizializza un nodo
    def __init__(self, nome:str, genitore:str):
        self.nome = nome
        self.genitore = genitore
        #Distanza da nodo iniziale
        self.g = 0
        #Distanza da nodo obiettivo
        self.h = 0
        #Costo totale delle distanze
        self.f = 0
    #Effettua comparazione tra nodi
    def __eq__(self, other):
        return self.nome == other.nome
    #Ordina i nodi in base al costo
    def __lt__(self, other):
         return self.f < other.f
    #Stampa i nodi
    def __repr__(self):
        return ('({0},{1})'.format(self.nome, self.f))


class Regione:
    # Initialize the class
    def __init__(self, name: str):
        self.name = name
        self.tasse = ImponiTasse()



#Genera casualmente un numero che poi sara la % delle tasse
def ImponiTasse():
    numeroCasuale = np.random.randint(50)

    return numeroCasuale




#Calcola il costo del percorso reale da un nodo A ad un nodo B
def calcoloCostoReale(partenza, target):
    costo = partenza * ((target/100)+1)

    return costo

#Stima il costo del percorso da un nodo A ad un nodo B
def calcoloEuristica (partenza, target):
    euristica = partenza * ((target/100)+1)

    return euristica

#Serve per trovare il percorso da una regione A ad una regione B nel grafo
#Restituisce un vettore che mantiene tutte le euristiche per le regioni che ci sono in mezzo tra A e B
def vettoreEuristiche (regione:Regione, lista):
    euristiche = {}
    for i in range (len(lista)):
            euristiche[lista[i].name] = calcoloEuristica(regione.tasse, lista[i].tasse)
    return euristiche

#Verifica che un nodo adiacente sia stato inserito nella lista dei nodi aperti
def verificaAggiuntaNeighbour(open, neighbour):
    for node in open:
        if (neighbour == node and neighbour.f > node.f):
            return False
    return True



#Ricerca A*
def ricercaAStar(prezzoiniziale ,grafo, euristiche, partenza: Regione, arrivo: Regione):

    open = []
    closed = []
    nodoPartenza = Nodo(partenza.name, None)
    nodoPartenza.g = prezzoiniziale
    nodoArrivo = Nodo(arrivo.name, None)
    open.append(nodoPartenza)
    tmp = 0
    while len(open) > 0:
        open.sort()
        nodoCorrente = open.pop(0)
        closed.append(nodoCorrente)
        
        if nodoCorrente == nodoArrivo:
            path = []
            while nodoCorrente != nodoPartenza:
                path.append(nodoCorrente.nome)
                nodoCorrente = nodoCorrente.genitore
            path.append(nodoPartenza.nome)
            return path[::-1]
        neighbours = grafo.get(nodoCorrente.nome)
        for key, value in neighbours.items():
            neighbour = Nodo(key, nodoCorrente)
            if (neighbour in closed):
                continue
            neighbour.g = (nodoCorrente.g) * ((grafo.get(nodoCorrente.nome, neighbour.nome)/100)+1)
            neighbour.h = euristiche.get(neighbour.nome)
            neighbour.f = neighbour.g * ((neighbour.h/100)+1)
            
            tmp = neighbour.f
            grafo.PrezzoFinale(tmp)
            if (verificaAggiuntaNeighbour(open, neighbour) == True):
                open.append(neighbour)
    
    return None

lista = []
Turchia = Regione("Turchia")
lista.append(Turchia)
Italia = Regione("Italia")
lista.append(Italia)
Inghilterra = Regione("Inghilterra")
lista.append(Inghilterra)
Egitto = Regione("Egitto")
lista.append(Egitto)
EmiratiArabiUniti = Regione("EmiratiArabiUniti")
lista.append(EmiratiArabiUniti)
Singapore = Regione("Singapore")
lista.append(Singapore)
SudAfrica = Regione("SudAfrica")
lista.append(SudAfrica)
Argentina = Regione("Argentina")
lista.append(Argentina)
Panama = Regione("Panama")
lista.append(Panama)
Cuba = Regione("Cuba")
lista.append(Cuba)
Alaska = Regione("Alaska")
lista.append(Alaska)
Taiwan = Regione("Taiwan")
lista.append(Taiwan) 
Indonesia = Regione("Indonesia")
lista.append(Indonesia)
NuovaGuinea = Regione("NuovaGuinea")
lista.append(NuovaGuinea)
CoreaDelSud = Regione("CoreaDelSud")
lista.append(CoreaDelSud)
Giappone = Regione("Giappone")
lista.append(Giappone)
NewYork = Regione("NewYork")
lista.append(NewYork)
Washington = Regione("Washington")
lista.append(Washington)
Danimarca = Regione("Danimarca")
lista.append(Danimarca)

#Genera il grafo con le relative connessioni pesate tra i nodi
def generaGrafo():

    grafo = Grafo()

    grafo.connessione(Italia.name, Egitto.name, calcoloCostoReale(Italia.tasse, Egitto.tasse))
    grafo.connessione(Egitto.name, Singapore.name, calcoloCostoReale(Egitto.tasse, Singapore.tasse))
    grafo.connessione(Singapore.name, Taiwan.name, calcoloCostoReale(Singapore.tasse, Taiwan.tasse))
    grafo.connessione(Taiwan.name, CoreaDelSud.name, calcoloCostoReale(Taiwan.tasse, CoreaDelSud.tasse))
    grafo.connessione(CoreaDelSud.name, Giappone.name, calcoloCostoReale(CoreaDelSud.tasse, Giappone.tasse))
    grafo.connessione(Giappone.name, Alaska.name, calcoloCostoReale(Giappone.tasse, Alaska.tasse))
    grafo.connessione(Alaska.name, Washington.name, calcoloCostoReale(Alaska.tasse, Washington.tasse))
    grafo.connessione(Washington.name, Panama.name, calcoloCostoReale(Washington.tasse, Panama.tasse))
    grafo.connessione(Panama.name, Cuba.name, calcoloCostoReale(Panama.tasse, Cuba.tasse))
    grafo.connessione(Cuba.name, NewYork.name, calcoloCostoReale(Cuba.tasse, NewYork.tasse))
    grafo.connessione(NewYork.name, Italia.name, calcoloCostoReale(NewYork.tasse, Italia.tasse))
    grafo.connessione(Cuba.name, SudAfrica.name, calcoloCostoReale(Cuba.tasse, SudAfrica.tasse))
    grafo.connessione(SudAfrica.name, Singapore.name, calcoloCostoReale(SudAfrica.tasse, Singapore.tasse))
    grafo.connessione(EmiratiArabiUniti.name, Egitto.name, calcoloCostoReale(EmiratiArabiUniti.tasse, Egitto.tasse))
    grafo.connessione(EmiratiArabiUniti.name, Singapore.name, calcoloCostoReale(EmiratiArabiUniti.tasse, Singapore.tasse))
    grafo.connessione(Turchia.name, Egitto.name, calcoloCostoReale(Turchia.tasse, Egitto.tasse))
    grafo.connessione(Turchia.name, Italia.name, calcoloCostoReale(Turchia.tasse, Italia.tasse))
    grafo.connessione(NewYork.name, Inghilterra.name, calcoloCostoReale(NewYork.tasse, Inghilterra.tasse))
    grafo.connessione(Inghilterra.name, Danimarca.name, calcoloCostoReale(Inghilterra.tasse, Danimarca.tasse))
    grafo.connessione(Argentina.name, Inghilterra.name, calcoloCostoReale(Argentina.tasse, Inghilterra.tasse))
    grafo.connessione(Panama.name, Inghilterra.name, calcoloCostoReale(Panama.tasse, Inghilterra.tasse))
    grafo.connessione(Panama.name, Italia.name, calcoloCostoReale(Panama.tasse, Italia.tasse))
    grafo.connessione(Panama.name, Argentina.name, calcoloCostoReale(Panama.tasse, Argentina.tasse))
    grafo.connessione(Italia.name, SudAfrica.name, calcoloCostoReale(Italia.tasse, SudAfrica.tasse))
    grafo.connessione(NuovaGuinea.name, Singapore.name, calcoloCostoReale(NuovaGuinea.tasse, Singapore.tasse))
    grafo.connessione(NuovaGuinea.name, Giappone.name, calcoloCostoReale(NuovaGuinea.tasse, Giappone.tasse))
    grafo.connessione(Giappone.name, Washington.name, calcoloCostoReale(Giappone.tasse, Washington.tasse))
    grafo.connessione(EmiratiArabiUniti.name, SudAfrica.name, calcoloCostoReale(EmiratiArabiUniti.tasse, SudAfrica.tasse))
    grafo.connessione(Danimarca.name, Washington.name, calcoloCostoReale(Danimarca.tasse, Washington.tasse))
    grafo.connessione(Panama.name, Giappone.name, calcoloCostoReale(Panama.tasse, Giappone.tasse))
    grafo.connessione(Taiwan.name, Giappone.name, calcoloCostoReale(Taiwan.tasse, Giappone.tasse))
    grafo.connessione(SudAfrica.name, Argentina.name, calcoloCostoReale(SudAfrica.tasse, Argentina.tasse))
    grafo.connessione(Indonesia.name, Taiwan.name, calcoloCostoReale(Indonesia.tasse, Taiwan.tasse))
    grafo.connessione(Indonesia.name, Giappone.name, calcoloCostoReale(Indonesia.tasse, Giappone.tasse))
    grafo.connessione(Indonesia.name, NuovaGuinea.name, calcoloCostoReale(Indonesia.tasse, NuovaGuinea.tasse))

    grafo.conversioneNonOrientato()


    return grafo

#Trova percorso da nodo A a nodo B
def trovaPercorso(prezzoiniziale,partenza, arrivo):
    regionePartenza = None
    regioneArrivo = None
    for i in range(len(lista)):
        if lista[i].name.lower() == partenza.lower():
            regionePartenza = lista[i]
        if lista[i].name.lower() == arrivo.lower():
            regioneArrivo = lista[i]

    if (regionePartenza == None or regioneArrivo == None):
        print("Inserimento errato!")
        return
    grafo = generaGrafo()

    euristiche = vettoreEuristiche(regioneArrivo, lista)

    percorso = ricercaAStar(prezzoiniziale ,grafo, euristiche, regionePartenza, regioneArrivo)
    print("Prezzo del prodotto tassato: ")
    print(grafo.numero)
    print("\nIl prodotto farà questo percorso per arrivare a destinazione : ")
    print(percorso)