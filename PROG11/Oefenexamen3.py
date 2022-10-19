# Opdracht 3:
# De afstand tussen twee coördinaten kan je uitrekenen met de volgende formule:
# https://prnt.sc/z-KlTT_Ksvgb

# Let op: worteltrekken doe je met math.sqrt() of machtsverheffen met exponent 0.5!
# Schrijf een programma waarin de gebruiker twee coördinaten moet invoeren. Print de afstand
# (afgerond op 4 decimalen). - https://prnt.sc/n1C2mVrHzuw4

# Importeer de math module
import math

# Vraag apart de x en y van de coordinaten op.
x1 = int(input("x van coord 1: "))
y1 = int(input("y van coord 1: "))
x2 = int(input("x van coord 2: "))
y2 = int(input("y van coord 2: "))

# AANPAK 1
# Formule in een keer (zonder Math)
ans1 = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# AANPAK 2
# Bereken het gekwadrateerde verschil tussen de coordinaten (met Math)
x_diff = (x2 - x1)**2
y_diff = (y2 - y1)**2
# Trek de wortel van de verschillen
ans2 = math.sqrt(x_diff + y_diff)

print(f"De (Euclidische) afstand tussen de coordinaten is {round(ans1, 4)}")
print(f"De (Euclidische) afstand tussen de coordinaten is {round(ans2, 4)}")

