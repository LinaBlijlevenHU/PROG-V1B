#######
# 5.1 #
#######

# Functie voor drie getallen (opsommen)
def opsommen(a, b, c):
    return a + b + c

a, b, c = 1, 2, 3
#print(opsommen(a, b, c))

#######
# 5.2 #
#######
# Accumulator loop pattern (getallen)
def opsommen(lijst):

    # Integer om bij op te tellen
    som = 0

    # Voor elk getal in de lijst
    for getal in lijst:
        # Tel het huidige getal op bij de huidige som (+ voor optellen)
        som += getal

    # Geef de volledige som terug
    return som

lijst = [1, 2, 3, 4, 5, 6]
print(opsommen(lijst))

# Accumulator loop pattern (vermenigvuldigen)
def product(lijst):

    # Integer om mee te vermenigvuldigen
    prod = 1

    # Voor elk getal in de lijst
    for getal in lijst:
        # Tel het huidige getal op bij de huidige som (+ voor optellen)
        prod *= getal            # som = som * getal

    # Geef de volledige som terug
    return prod

lijst = [1, 2, 3, 4, 5, 6]
print(product(lijst))

# Accumulator loop pattern (met letters/strings)
def samenvoegen(lijst):

    # Lege string om bij op te tellen
    resultaat = ''

    # Voor elke letter in de lijst
    for letter in lijst:
        # Voeg de huidige letter toe aan de resultaat string (+ voor concatenation)
        resultaat += letter     # resultaat = resultaat + letter
                                # (andersom) resultaat = letter + resultaat

    # Geef de volledige string terug
    return resultaat

letterlijst = ['a', 'b', 'c', 'd']
print(samenvoegen(letterlijst))             # abcd

# Accumulator loop pattern (met lijst)
def kwadratenlijst(lijst):
    '''
    Geef een lijst met kwadraten van de elementen in de input lijst terug.

    @param  list    lijst met getallen
    @param  list    lijst met kwadraten
    '''

    # Lege lijst om het resultaat bij te houden
    resultaat = []

    # Loop over alle getallen
    for getal in lijst:

        # Toevoegen van het kwadraat aan de lijst (append)
        resultaat.append(getal**2)

    # Geef het volledige resultaat terug
    return resultaat

getallenlijst = [1, 2, 3, 4, 5, 6]
print(kwadratenlijst(getallenlijst))        # Gewenste output: [1, 4, 9, 16, 25, 36]

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