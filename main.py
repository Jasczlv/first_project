#fare un orologio semplice con python completamente da zero senza usare librerie esterne
#per iniziare il progetto pensare a cosa fare
#creare una variabile per tenere traccia del tempo, capire come far utilizzo di una classe per aiutare a gestire l orologio
#creare un ciclo infinito per aggiornare il tempo ogni secondo
#printare in console il tempo aggiornato

#come si crea un oggetto in python?
#In Python, puoi creare un oggetto definendo una classe e poi istanziando un oggetto da quella classe. Ecco un esempio semplice:

'''
 class Persona:
    def __init__ (self, nome, eta):
        self.nome = nome
        self.eta = eta
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

gianni = Persona("Gianni",24)

gianni.presentazione() */
'''
#importo la libreria time per poter utilizzare la funzione perf_counter che ci permette di misurare il tempo in modo preciso
import time

#definisco la funzione che cicla attraverso il tempo e aggiorna le variabili ore minuti secondi attraverso un ciclo
def mio_orologio():
    ore = 0
    minuti = 0
    secondi = 0

    #prendiamo il punto di partenza assoluto dall'hardware
    tempo_precedente = time.perf_counter()

    #printiamo la partenza a 00:00:00 senno' la prima stampa partirebbe da 00:00:01
    print("00:00:00", end="\r")

    #iniziamo a ciclare il tempo
    while True:

        #creiamo una variabile che prende il tempo attuale ma che viene aggiornato ad ogni ciclo
        tempo_attuale = time.perf_counter()
        
        #avendo stabilito in precedenza il tempo precedente che a differenza del tempo attuale é statico, ora possiamo ad ogni aggiornamento del tempo attuale confrontarli e aggiornare secondi
        if tempo_attuale - tempo_precedente >= 1.0:
            secondi += 1
            if secondi == 60:
                secondi = 0
                minuti += 1
                if minuti == 60:
                    minuti = 0
                    ore += 1
                    if ore == 24:
                        ore = 0
            
            #mostra l'orologio aggiornato
            print(f"{ore:02d}:{minuti:02d}:{secondi:02d}", end="\r")
            
            #aggiorna il punto di riferiment compensando eventuali micro-ritardi
            tempo_precedente += 1.0 

#chiamiamo la funzione per far partire l'orologio
mio_orologio()