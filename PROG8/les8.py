##############
# While-loop #
##############

# Stel wisselgeld in
wisselgeld = 212
# Houd een aantal 50 cent muntjes bij om terug te geven
aantal50 = 0

# Kunnen we nog een 50 cent muntje uitdelen?
while wisselgeld > 50:
    # Tel een muntje op bij het aantal
    aantal50 += 1

    # Verminder het wisselgeld
    wisselgeld -= 50

    # Print de tussenstap voor de duidelijkheid
    print(f"Totaal {aantal50} muntjes uitbetaald, wisselgeld is nu {wisselgeld}")

# Print het totale aantal bepaald door de loop uit
print(f"Je krijgt {aantal50} 50 cent muntjes.")
print("\n\n")

####################
# Break & continue #
####################

# Lijst met namen
namen = ['Rick', 'Anmar', 'Tijn', 'Douwe']

# For-loop met break (breek de loop af na een bepaald punt)
for naam in namen:
    # Als Tijn binnenkomt, breek ik het begroeten af
    # Door de volgorde wordt ook Tijn niet meer begroet.
    if (naam == "Tijn"):
        break

    # Begroet de leerling
    print(f"Hallo {naam}")

print("\n\n")

# For-loop met continue: sla een iteratie over
for naam in namen:
    # We zeggen geen hallo tegen Tijn :(
    if (naam == "Tijn"):
        continue

    # We zeggen hallo tegen de leerling
    print(f"Hallo {naam}")

print("\n\n")

###################################
# Break, continue en nested loops #
###################################

# Print de tafels van 1-10
for i in range(1, 11):
    # Print de tafel voor een getal i door te loopen over de getallen
    # van 1-10
    for j in range(1, 11):
        # Sla 7xn in de tafel van n over
        if (j == 7):
            continue

        # Print het onderdeel van de tafel
        print(f"{i} * {j} = {i*j}")

    # Stop na de tafel van 7
    if (i == 7):
        break

print("\n\n")
# Houd het aantal ingevoerde centen bij
ingevoerd = 0
# Prijs van het product
prijs = 212

# Voorbeeldje voor geld blijven invoeren tot er genoeg is ingevoerd.
# while ingevoerd < prijs:
#     # Laat de klant geld inwerpen
#     print("Voer een bedrag in munten in.")
#     inworp = int(input("Hoeveel heb je ingevoerd in eurocenten?\n"))
#
#     # Totaal ingevoerde bedrag updaten
#     ingevoerd += inworp
#
#     if (ingevoerd < prijs):
#         print(f"Er moet nog {prijs - ingevoerd} betaald worden.")
#     else:
#         print("Dankjewel voor je aankoop, je wisselgeld komt eraan.")

print("\n\n")

################
# Dictionaries #
################

producten = {
    'Coca Cola': 1.00,
    'Fanta': 1.15,
    'Sprite': 0.90
}

# Print alle waarden in een dictionary uit
for productnaam, prijs in producten.items():
    print(f"{productnaam} kost {prijs}")

############################
# Werken met keys & values #
############################

# Maak een lijst van de namen met een goede oude for-loop
namen = []
for naam in producten.keys():
    namen.append(naam)
print(namen)

# Maak een lijst van de namen met list comprehension
namen2 = [naam for naam in producten.keys()]
print(namen2)

# Print de prijzen
print(producten.values())

print("\n\n")

#
#

# producten = {
#     'A1': {
#         'naam': 'Coca Cola',
#         'prijs': 1.00,
#     },
#     'A2': {
#         'naam': 'Fanta',
#         'prijs': 1.15,
#     },
#     'A3': {
#         'naam': 'Sprite',
#         'prijs': 0.90
#     }
# }
#
# print("Selecteer je product:")
#
# # Voor elke knop gelinkt aan een product
# for knop, product in producten.items():
#     # Selecteer de informatie over het product (uit de dictionary)
#     productnaam = product['naam']
#     prijs = product['prijs']
#
#     # Printen we de informatie over het product.
#     print(f"{knop}: {productnaam} kost {prijs}")
#
# print(f"Bij knop A1 hoort product {producten['A1']['naam']}")

##########################
# Dicts voor frequenties #
##########################

def frequency(itemList):
    'returns frequency of items in itemList'

    # Maak een dictionary met tellers aan
    counters = {}

    # Voor elk item in de lijst
    for item in itemList:

        # Hebben we al een teller voor dit item?
        if item in counters:
            # Verhoog de teller
            counters[item] += 1

            # Print de nieuwe waarde van de teller
            print(f"We hebben het getal {item} nu {counters[item]} keer gezien.")

        # Maak een teller aan
        else:
            # Maak de teller aan
            counters[item] = 1

            # Print een boodschap voor de gebruiker
            print(f"We zien het getal {item} nu voor het eerst.")
    return counters

# Bepaal de frequenties van een lijst
freqs = frequency([1, 2, 2, 4, 5, 6, 4, 6, 6, 6, 6])

# Check of we een teller hebben voor het getal 3 in de frequenties
if (3 in freqs.keys()):
    print(f"Het getal 3 komt {freqs[3]} voor.")
# Als we dat niet hebben komt het getal niet voor.
else:
    print("Het getal 3 komt niet voor in de lijst.")

# https://www.w3schools.com/python/ref_dictionary_get.asp
# Kijk of we een teller voor 3 hebben, gebruik anders default waarde 0
aantal3 = freqs.get(3, 0)
print(f"Het getal 3 komt {aantal3} keer voor")