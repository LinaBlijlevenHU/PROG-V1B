#######
# 5.2 #
#######

# Maak een lijst aan
getallenlijst = [1, 2, 3, 4, 5, 2, 4, 6, 5]

# Functie om lijstelementen bij elkaar op te tellen
def opsommen(lijst):

    # Som
    som = 0

    # Voor elk element in de lijst
    for e in lijst:
        # Tel het element op bij de totale som
        som = som + e

    return som

# Gebruik de ingebouwde sum methode
def opsommen2(lijst):
    return sum(lijst)

# Bereken de som
#print(opsommen(getallenlijst))

#######
# 5.6 #
#######

# Schrijf (en test) de functie wijzig() met één parameter: letterlijst.
# Zorg dat de functie de lijst leegt en de letters [ ‘d’, ‘e’, ‘f’ ] toevoegt.
# Er is geen return-waarde!
def wijzig(lijst):
    lijst.clear()
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')

# Test je programma als volgt:
lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

# Uitvoer:
# ['a', 'b', 'c']
# ['d', 'e', 'f']

# Q: Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
# A: Als je simpelweg de lijst deze waarde probeert te geven (zie voorbeeld voor waar zij op doelen)
# bestaat de waarde voor de lijst alleen binnen de functie. Als je het resultaat print met deze functie
# staat er dus nog steeds ['a', 'b', 'c'] in de lijst, deze is zelf niet aangepast.
#
# Voorbeeld (fout):
# def wijzig(lijst):
#   lijst = ['d', 'e', 'f']

# Q: Werkt jouw functie ook met een string-parameter? Probeer dit! Waarom werkt het wel/niet?
# A: Nee. String zijn immutable/kunnen niet aangepast worden.

# Q: Welke rol speelt (im)mutabiliteit in deze vraag?
# A: Strings zijn immutable, lijsten zijn mutable. Daarom kunnen we dit alleen toepassen op een lijst.