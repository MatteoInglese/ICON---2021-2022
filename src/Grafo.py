import numpy as np

class Grafo:
    #Costruttore del grafo
    def __init__(self, grafoDict=None, orientato=True):
        self.grafoDict = grafoDict or {}
        self.orientato = orientato
        self.CostoFinale = 0
        if not orientato:
            self.conversioneNonOrientato()
            
    #Se il grafo è orientato viene convertito in non orientato con questo metodo
    def conversioneNonOrientato(self):
        for a in list(self.grafoDict.keys()):
            for (b, dist) in self.grafoDict[a].items():
                self.grafoDict.setdefault(b, {})[a] = dist

                
    #Crea un arco con relativo peso tra il nodo A e il nodo B, in caso il grafo sia non orientato lo crea in entrambe le direzioni
    def connessione(self, A, B, distanza=1):
        self.grafoDict.setdefault(A, {})[B] = distanza
        
        if not self.orientato:
            self.grafoDict.setdefault(B, {})[A] = distanza
 
            
    #Restituisce i nodi adiacenti
    def get(self, a, b=None):
        links = self.grafoDict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
 
        
    #Restituisce lista di tutti i nodi
    def nodi(self):
        s1 = set([k for k in self.grafoDict.keys()])
        s2 = set([k2 for v in self.grafoDict.values() for k2, v2 in v.items()])
        nodi = s1.union(s2)
        return list(nodi)
    
    #Rimuove dal grafo una Nazione (nodo)
    def rimuovi(self, listaRegioni, nomeNazione):
        for i in range (len(listaRegioni)):
            if(self.grafoDict[listaRegioni[i].name].get(nomeNazione) != None):
               self.grafoDict[listaRegioni[i].name].pop(nomeNazione)
        self.grafoDict.pop(nomeNazione)
    
    
    #Avvalora l'attributo costofinale del grafo
    def PrezzoFinale(self, CostoFinale):
        self.CostoFinale = CostoFinale


    
class Nodo:

    def __init__(self, nome:str, genitore:str):     #Costruttore del nodo
        self.nome = nome
        self.genitore = genitore
        self.g = 0        #Distanza da nodo iniziale
        self.h = 0        #Distanza da nodo obiettivo
        self.f = 0        #Costo totale delle distanze
        
    
    def __eq__(self, other):    #Effettua comparazione tra nodi
        return self.nome == other.nome
    
    
    def __lt__(self, other):    #Ordina i nodi in base al costo
         return self.f < other.f
     

    def __repr__(self):         #Stampa i nodi
        return ('({0},{1})'.format(self.nome, self.f))


class Nazione:
            
    def __init__(self, name: str):  #costruttore di nazione
        self.name = name
        self.tasse = ImponiTasse()



#Genera casualmente un numero che rappresenta quella che sarà la % delle tasse
def ImponiTasse():
    RandomNumber = np.random.randint(50)

    return RandomNumber




#Calcola il costo del percorso reale da un nodo A ad un nodo B
def calcoloCostoReale(partenza, target):
    costo = partenza * ((target/100)+1)

    return costo

#Stima il costo del percorso da un nodo A ad un nodo B
def calcoloEuristica (partenza, target):
    euristica = partenza * ((target/100)+1)

    return euristica



#Restituisce un vettore contenente tutte le euristiche per le nazioni che sono presenti tra A e B
def vettoreEuristiche (Nazione:Nazione, lista):
    euristiche = {}
    for i in range (len(lista)):
            euristiche[lista[i].name] = calcoloEuristica(Nazione.tasse, lista[i].tasse)
    return euristiche

#Verifica che un nodo adiacente sia stato inserito nella lista dei nodi aperti
def verificaAggiuntaNeighbour(open, neighbour):
    for node in open:
        if (neighbour == node and neighbour.f > node.f):
            return False
    return True



#Algoritmo di ricerca A*
def ricercaAStar(prezzoiniziale ,grafo, euristiche, partenza: Nazione, arrivo: Nazione):

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
Turchia = Nazione("Turchia")
lista.append(Turchia)
Italia = Nazione("Italia")
lista.append(Italia)
Inghilterra = Nazione("Inghilterra")
lista.append(Inghilterra)
Egitto = Nazione("Egitto")
lista.append(Egitto)
EmiratiArabiUniti = Nazione("EmiratiArabiUniti")
lista.append(EmiratiArabiUniti)
Singapore = Nazione("Singapore")
lista.append(Singapore)
SudAfrica = Nazione("SudAfrica")
lista.append(SudAfrica)
Argentina = Nazione("Argentina")
lista.append(Argentina)
Panama = Nazione("Panama")
lista.append(Panama)
Cuba = Nazione("Cuba")
lista.append(Cuba)
Alaska = Nazione("Alaska")
lista.append(Alaska)
Taiwan = Nazione("Taiwan")
lista.append(Taiwan) 
Indonesia = Nazione("Indonesia")
lista.append(Indonesia)
NuovaGuinea = Nazione("NuovaGuinea")
lista.append(NuovaGuinea)
CoreaDelSud = Nazione("CoreaDelSud")
lista.append(CoreaDelSud)
Giappone = Nazione("Giappone")
lista.append(Giappone)
NewYork = Nazione("NewYork")
lista.append(NewYork)
Washington = Nazione("Washington")
lista.append(Washington)
Danimarca = Nazione("Danimarca")
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

#Metodo che trova e stampa il percorso tra A e B, e il costo del prodotto tassato
def trovaPercorso(prezzoiniziale,partenza, arrivo):
    NazionePartenza = None
    NazioneArrivo = None
    for i in range(len(lista)):
        if lista[i].name.lower() == partenza.lower():
            NazionePartenza = lista[i]
        if lista[i].name.lower() == arrivo.lower():
            NazioneArrivo = lista[i]

    if (NazionePartenza == None or NazioneArrivo == None):
        print("Inserimento errato!")
        return
    grafo = generaGrafo()

    euristiche = vettoreEuristiche(NazioneArrivo, lista)

    percorso = ricercaAStar(prezzoiniziale ,grafo, euristiche, NazionePartenza, NazioneArrivo)
    print("Prezzo del prodotto tassato: ")
    print(grafo.CostoFinale)
    print("\nIl prodotto farà questo percorso per arrivare a destinazione : ")
    print(percorso)