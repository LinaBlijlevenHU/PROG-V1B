'''
Dit is een lange comment
Heel lang
Meerdere regels
'''

###########
# Lijsten # 
###########

# Maak een lijstje van leerlingen
leerlingen = ['Michali', 'Tyler', 'Ali', 'Tiago', 'Daan', 'Stan', 'Max']
leerlingen2 = ['Tijn', 'Bas', 'Marnix', 'Anmar']

# Kijk of Bas in het lijstje met leerlingen staat
print('Bas' in leerlingen)
print('Max' not in leerlingen)

# Verschillende applicaties van de + operator
#1 + 3                               # Addition
#'Lina' + ' ' + 'Blijleven'          # String concatenation
#leerlingen + leerlingen2            # List concatenation

# Voeg alle leerlingen bij elkaar
print(leerlingen + leerlingen2)

# Vermenigvuldig een lijst
print(2 * leerlingen)

# Selecteer Ali uit de eerste lijst met leerlingen
print(leerlingen[2])

# Print de hoeveelheid leerlingen
alle_leerlingen = leerlingen + leerlingen2
print(len(alle_leerlingen))

# Print de eerste uit het alfabet en de laatste uit het alfabet
print(min(alle_leerlingen))
print(max(alle_leerlingen))

# Bereken een som
dobbelsteen = [1, 2, 3, 4, 5, 6]
print(sum(dobbelsteen))

# Pas de leerling op index 2 aan
alle_leerlingen[2] = 'Fadil'

# Print onze lijsten om het verschil te zien
print(leerlingen)
print(alle_leerlingen)

# Maak een string aan en pak hier een index uit
naam = 'Douwe'
print(naam[2])

# Pas zijn naam aan door een letter te vervangen
# Let op: Dit werkt niet, want strings kun je niet aanpassen. Lijsten wel.
# naam[2] = 'l'

# Voeg een naam toe aan de lijst
alle_leerlingen.append("Floris")
print(alle_leerlingen)

# Tel hoe vaak de naam Robin voorkomt in de lijst met leerlingen
print(alle_leerlingen.count("Robin"))

# Vind de index waar een item als eerste voorkomt
print(alle_leerlingen.index('Tiago'))

# Verwijder de laatste leerling en geef deze terug
print(alle_leerlingen.pop())

# Verwijder een item uit de lijst
alle_leerlingen.remove('Bas')
print(alle_leerlingen)

# Sorteer de leerlingen op alfabet
alle_leerlingen.sort()
print(alle_leerlingen)

# Sorteer de leerlingen op omgekeerd alfabet
alle_leerlingen.reverse()
print(alle_leerlingen)

###################
# Lijst vs. tuple #
###################

# Aanmaken
lst = ['a', 'b', 'c']       # mutable/aanpasbaar
tup = ('a', 'b', 'c')       # immutable/niet aanpasbaar

# Indexeren
lst[0]
tup[0]

# Aanpassen van individuele elementen
# Let op: dit kun je dus niet doen bij een tuple.
lst[1] = 'd'               
#tup[1] = 'd'


# Waarom zou je een tuple gebruiken?
# Soms hebben we een lijst nodig die je niet aan kan passen.

# Voorbeeld van een functie
def statistieken(lst):
    m = gemiddelde(lst)

    return (m, 0, 0)
    
# Functie om een gemiddelde te berekenen 
# (Hulpfunctie)
def gemiddelde(lst):
    return sum(lst) / len(lst)

# Bereken de statistische informatie over een lijst
(gem, med, std_afwijking) = statistieken([1, 2, 3, 4, 5])