#fare un orologio semplice con python completamente da zero senza usare librerie esterne
#per iniziare il progetto pensare a cosa fare
#creare una variabile per tenere traccia del tempo, capire come far utilizzo di una classe per aiutare a gestire l orologio
#creare un ciclo infinito per aggiornare il tempo ogni secondo
#printare in console il tempo aggiornato

#come si crea un oggetto in python?
#In Python, puoi creare un oggetto definendo una classe e poi istanziando un oggetto da quella classe. Ecco un esempio semplice:

class Persona:
    def __init__ (self, nome, eta):
        self.nome = nome
        self.eta = eta
    def presentazione(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

gianni = Persona("Gianni",24)

gianni.presentazione()
