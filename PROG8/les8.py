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

while ingevoerd < prijs:
    # Laat de klant geld inwerpen
    print("Voer een bedrag in munten in.")
    inworp = int(input("Hoeveel heb je ingevoerd in eurocenten?\n"))

    # Totaal ingevoerde bedrag updaten
    ingevoerd += inworp

    if (ingevoerd < prijs):
        print(f"Er moet nog {prijs - ingevoerd} betaald worden.")
    else:
        print("Dankjewel voor je aankoop, je wisselgeld komt eraan.")
