# Opdracht 1:
# Schrijf een functie isPositiefEnKleinerDan(x, y) waarin je bepaalt of gegeven getal ‘x’ een positief getal is,
# en kleiner dan getal ‘y’. De parameters x en y zijn van het type int. De functie geeft True terug als dat zo is,
# anders False.
def isPositiefEnKleinerDan(x, y):
    '''
    Bepaal of een gegeven getal x positief is en kleiner dan y.

    @param  int
    @param  int
    '''
    return (x >= 0) and (y > x)

print(isPositiefEnKleinerDan(0, 4))