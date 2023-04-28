"""
Denne oppgaven svarer på siste oppgave, lag ditt eget program.
I denne oppgaven skal du lage en quiz. Spør brukeren om 2-5 spørsmål. Brukeren får kun neste spørsmål hvis
første spørsmål er riktig besvart. Kjør en if-test som sjekker svarene og printer ut resultatet til brukeren.
Sørg for at svarene skal ha riktig datatype og at programmet tolerer om svarene blir skrevet på forskjellige måter
(feks med stor og liten bokstav). Quizen kan handle om hva du vil.
"""

print("Hei og velkommen til denne quizen! Du skal nå få svare på 3 spørsmål.")

hovedstad = input("Hva er hovedstaden i Estland?")

if hovedstad == "Talinn" or "tallinn":
    farge = input("Hvilken farge får man hvis man blander blå og gul?")
    if farge == "grønn" or "Grønn":
        dager = int(input("Hvor mange dager er det i et år?"))
        if dager == 365:
            print("Gratulerer! Du klarte hele quizen. 3/3 riktige!")
        else:
            print("Beklager, så nære! 2/3 riktige")
    else:
        print("Beklager, det er feil. 1/3 riktige")
else:
    print("Du svarte feil. 0/3 riktige")
