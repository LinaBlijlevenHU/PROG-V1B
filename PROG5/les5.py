def pythagoras(a, b):
    'Bereken de lengte van een lange zijde met de stelling van Pythagoras'
    # Bereken a^2 + b^2
    ab = a**2 + b**2
    # Neem daar de wortel van
    c = ab**(1/2)
    return c

# Bereken de lengte van de lange zijde
print(pythagoras(3, 4))

# Wat staat er nu in c?
# Error: de waarde blijft binnen de functie
#print(c)

# Print getallen in een range
for i in range(5):
    print(i)

# Wat staat er nu in i?
print(i)