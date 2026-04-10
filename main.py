#fare un orologio semplice con python completamente da zero senza usare librerie esterne
#per iniziare il progetto pensare a cosa fare
#creare una variabile per tenere traccia del tempo
#creare un ciclo infinito per aggiornare il tempo ogni secondo
#printare in console il tempo aggiornato

#come si crea un oggetto in python?
#In Python, puoi creare un oggetto definendo una classe e poi istanziando un oggetto da quella classe. Ecco un esempio semplice:
#voglio una classe unrelated al progetto solo per capire come funziona con commenti che spiegano tutto

class Persona:
    """A class to represent a person with a name and age."""
    def __init__ (self, nome, eta):
        self.nome = nome
        self.eta = eta
    def presentazione(self):
        """Print a greeting with the person's name and age."""
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

ianis = Persona("Ianis",24)

ianis.presentazione()
