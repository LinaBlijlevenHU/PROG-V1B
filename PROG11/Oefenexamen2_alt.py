# Opdracht 2:
# Schrijf een programma waarin de gebruiker drie getallen kan invullen. Print vervolgens het middelste
# (qua grootte) getal. - https://prnt.sc/FoVpjW0Vdjby

# Vraag de gebruiker om getallen
a = int(input("Voer het eerste getal in: "))
b = int(input("Voer het tweede getal in: "))
c = int(input("Voer het derde getal in: "))

# Lijst met de getallen
lijst = [a, b, c]

# Stel een waarde in voor de min en de max
min = getallen[0]
max = getallen[0]

# We loopen over de getallen
for i in getallen:
    # Hebben we een kleiner getal gevonden?
    if i < min:
        # Werk de minimale waarde bij
        min = i
    # Hebben we een groter getal gevonden?
    if i > max:
        # Werk de maximale waarde bij
        max = i

# Stel de waarde in voor de mid
mid = getallen[0]

# We loopen nogmaals over de getallen
for i in getallen:
    # Zoek het getal dat niet de min is en niet de max.
    if i is not min and i is not max:
        # Stel de mid in
        mid = i

print(f"Het middelste getal is: {mid}")