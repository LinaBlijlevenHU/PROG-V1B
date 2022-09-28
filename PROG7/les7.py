# Voor de for-loop voorbeelden zie /PROG5/exercises.py

prijs, betaald = 113, 100

# One-way if-statement: gebruikt alleen een if
if (prijs > betaald):
    print("Je hebt niet genoeg betaald.")

prijs, betaald = 113, 330

# Two-way: gebruikt if + else
if (prijs > betaald):
    print("Je hebt niet genoeg betaald.")
else:
    print("Je hebt genoeg betaald, je wisselgeld wordt nu berekend.")

prijs, betaald = 113, 113

# Multi-way
# Met if, elif (evt. meerdere keren) en else
# Zeer geschikte structuur voor bijvoorbeeld kijken naar de waarde van een enkele variabele.
# Als twee if-statements gerelateerd zijn gebruik je één structuur (if/elif/else),
# als ze ongerelateerd zijn gebruik je losse statements.
if (prijs > betaald):
    print("Je hebt niet genoeg betaald.")
elif (prijs == betaald):
    print("Je hebt genoeg betaald, je krijgt geen wisselgeld.")
else: # prijs < betaald
    print("Je hebt genoeg betaald, je wisselgeld wordt nu berekend.")

# Multi-way met nested if-structuur
# Een if-statement kan vervolgens nog meer if-statements bevatten.
if (prijs > betaald):
    print("Je hebt niet genoeg betaald.")
else: # prijs <= betaald
    # Als we genoeg betaald hebben printen we altijd de volgende zin.
    print("Bedankt voor uw aankoop! Neem uw product uit.")

    # Vervolgens geven we meer informatie betreffende het wisselgeld.
    if (prijs == betaald):
        print("Je krijgt geen wisselgeld.")
    else: # prijs < betaald
        print("Je wisselgeld wordt nu berekend.")

print("\n\n\n")
# Volgorde van condities
score = -50

# Waarom is de volgorde hier zo belangrijk?
# De volgorde bepaalt welke condities impliciet zijn. Als we eerst kijken of iets <n is,
# worden alle negatieve gevallen hier ook naar True geevalueerd. Dit betekent dat je
# dan eventueel een if-statement activeert terwijl dat niet de bedoeling is.
if (score < 0):
    print("Sorry, je moet de toets nog herkansen.")
elif (score < 55): # score >= 0
    print("Sorry, je hebt een onvoldoende")
else:
    print("Je hebt een voldoende!")

print("\n\n\n")
# Iteration loop pattern (met karakters)
# Open een file en lees de content in een string in
infile = open('test.txt')
content = infile.read()
# Loop over alle karakters van een bestand (we geven geen end mee,
# dus alle karakters komen op een nieuwe regel)
for char in content:
    print(char)
# Sluit de file af, deze hebben we niet meer nodig.
infile.close()

# Iteration loop pattern (met regels)
# Open de file opnieuw voor het volgende voorbeeld
infile = open('test.txt')
# Lees alle regels in een array in
lines = infile.readlines()
# Loop over alle regels van een bestand
for line in lines:
    # Split de regels op spaties, zodat we een lijst van woorden terug krijgen.
    print(line.split())
# Sluit de file weer af.
infile.close()

print("\n\n\n")
# Counter loop pattern
pets = ['Koe', 'Konijn', 'Kip']

# For-each loop
# Hier hoeven we niet na te denken over wat op welke index staat: dat
# regelt python!
for animal in pets:
    print(animal)

# For-loop (dit gebeurt hierboven impliciet)
# Hier gebruiken we range i.c.m. de lengte van de lijst
# om over de indices te loopen. Dit kan dus makkelijker met de loop hierboven,
# maar is wel de juiste aanpak voor programmeertalen zonder for-each loop.
for i in range(len(pets)):
    print(pets[i])

# Accumulator loop pattern
# Zie exercises in PROG5: hier bouwen we een som, string en lijst op.

print("\n\n\n")
# Oefening:
# Write function acronym() that:
# • takes a phrase (i.e., a string) as input
# • returns the acronym for the phrase
def acronym(tekst):
    '''
    Creates an acronym for a string

    @param  string  Phrase
    @param  string  The new acronym
    '''

    # Houd een string voor het acronym bij
    ac = ''

    # Zin opsplitsen in woorden
    woorden = tekst.split()

    # Voor elk woord
    for woord in woorden:

        # Selecteer de eerste letter en maak er een hoofdletter van
        letter = woord[0].upper()

        # Voeg de letter toe aan de string
        ac += letter

    # Geef het hele acronym terug
    return ac

print(acronym("Be right back")) # BRB
print(acronym("Ik ga even thee halen")) #IGETH

print("\n\n\n")
# Nested loop pattern
# 1A, 1B, 1C, 1D, 2A...?
# 1A, 2A, 3A, 4A, 1B...?
for i in range(1, 5):
    for j in ['A', 'B', 'C', 'D']:
        print(f"Klas {i}{j}")

for i in ['A', 'B', 'C', 'D']:
    for j in range(1, 5):
        print(f"Klas {j}{i}")

print("\n\n\n")
# Herhaling list slicing
lijst = [1, 2, 3, 4, 5, 6]
print(lijst[:2])    # tot index 2
print(lijst[2:])    # vanaf index 2
print(lijst[:])     # hele lijst!

print("\n\n\n")
# Two-dimensional lists
infile = open('kaartnummers.txt')
lines = infile.readlines()

# Houd een nieuwe array bij voor de data
personen = []

# Voor elke regel
for line in lines:
    # Verwijder het \n karakter
    cleanline = line.strip("\n")

    # Maak een lijst [kaartnummer, naam]
    persoon = cleanline.split(', ')

    # Voeg deze persoon toe aan de lijst met personen
    personen.append(persoon)

print(personen)

# Loop over de personen en print hun informatie
for persoon in personen:
    kaartnummer, naam = persoon[0], persoon[1]
    print(f"{naam} heeft kaartnummer {kaartnummer}")

# Nested loop pattern and 2-D lists
# Print alle informatie uit een tweedimensionale array
for regel in personen:
    for informatie in regel:
        print(informatie)

print("\n\n\n")
# Oefening
# Implement function pixels() that takes as input:
# • a two-dimensional list of integer entries (representing the values of pixels of an image)
# and returns the number of entries that are positive (i.e., the number of pixels that are
# not dark). Your function should work on two-dimensional lists of any size.
lijst = [[44, 34, 54, 55], [-43, -45, 44, 66], [45, 76, 42, 19], [-19, 24, 55, 55]]