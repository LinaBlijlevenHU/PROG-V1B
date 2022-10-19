# Opdracht 5:
# Schrijf een programma waarin je de gebruiker een string laat invoeren. Gebruik vervolgens een for-loop om de
# omgekeerde string te printen. - https://prnt.sc/pxh6mG2GI0-U

# Vraag om input van de gebruiker
zin = input("Voer een string in: ")

# String om op te bouwen
omgekeerd = ""

# Vooraan de string toevoegen
for i in zin:
    omgekeerd = i + omgekeerd
    print(omgekeerd)