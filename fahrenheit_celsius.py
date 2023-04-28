""" I dette programmet skal vi ta inn en temperatur i fahrenheit og omgjøre den til celcius.
Første delen av programet lager jeg en variabler og setter verdien selv. Senere gjør jeg om programmet
slik at man ber brukeren input i form av en temperatur. Jeg lager en formel som gjør utregningen fra
fahrenheit til celcius. Jeg sørger også for at både temperaturen før og etter omgjøring har en tallveri,
altså ikke er en string.
"""
"""
temp = 80
"""
temp = (int(input("Skriv inn en temperatur i fahrenheit i form av et heltall")))

print("Temperaturen er", temp, "grader fahrenheit")

temp_cel = (float(temp - 32) * 5/9)

print("Temperaturen i celcius er", round(temp_cel, 2))
"""Her runder jeg av slik at jeg ikke får flere enn to desimaler når vi printer ut temperaturen i celcius."""

"""
Sjekker hvilken datatype temperaturene har

print(type(temp))
print(type(temp_cel))
"""
