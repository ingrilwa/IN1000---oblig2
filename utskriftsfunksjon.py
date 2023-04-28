""" I dette programmet tar vi inn navn og sted fra brukeren, to verdier som settes i to forskjellige variabler.
Vi setter dette inn i en egendefinert funksjon, slik at vi kan kalle på denne flere ganger. Etter vi har tatt
inn innformasjon fra brukeren bruker vi dette og printer ut en setning som inneholder verdiene de skrev inn.
Når vi kaller på funksjonen flere ganger, spør vi også brukeren flere ganger, og de har mulighet til å
legge inn forskjellige verdier hver gang. 
"""

def utskriftsfunksjon():
    navn = input("Skriv inn navn")
    sted = input("Hvor kommer du fra?")
    print("Hei, " + navn + "! Du er fra " + sted + ".")

utskriftsfunksjon()
utskriftsfunksjon()
utskriftsfunksjon()
