"""
1. Nei, dette programmet vil ikke kjøre. De første tre kodelinjene ser greie ut, men i fjerde kodelinje
prøver man å addere sammen en string og et heltall, to forskjellige datatyper, noe som ikke funker.

2. Selv om brukeren blir bedt om å taste inn et heltall, kan man aldri være sikker på at de faktisk gjør dette.
Hvis brukeren hadde skrevet inn bokstaver, vil ikke int()funksjonen funke.
Hvis brukeren faktisk taster inn et heltall, er det ikke beskrevet hva som skal skje hvis tallet er
høyere enn 10. Det er ofte lurt å ha med else, slik at hvis ikke if kjører, får brukeren en beskjed.
Som nevnt i forrige deloppgave vil ikke funksjonen kjøre i det hele tatt. Hvis man
derimot hadde brukt komma isteden for pluss, og heller satt faktorene etter hverandre isteden for å prøve å
legge de sammen, ville nok dette vært en bedre løsning.
"""

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
