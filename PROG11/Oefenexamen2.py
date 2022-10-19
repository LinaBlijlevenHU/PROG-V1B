# Opdracht 2:
# Schrijf een programma waarin de gebruiker drie getallen kan invullen. Print vervolgens het middelste
# (qua grootte) getal. - https://prnt.sc/FoVpjW0Vdjby

# Vraag de gebruiker om getallen
a = int(input("Voer het eerste getal in: "))
b = int(input("Voer het tweede getal in: "))
c = int(input("Voer het derde getal in: "))

# Zet de getallen in een lijst
lijst = [a, b, c]

# Sorteer de lijst
lijst.sort()

# Pak het element in het midden van de lijst
print(lijst[1])