# Frisdrank-machine met lijsten

def selecteer_product(producten, keuze):
    '''
    Checkt of een bepaald product in de bestaande producten staat

    :param      list        Lijst met producten
    :param      string      De keuze van de gebruiker
    :return     mixed       Product of None
    '''
    # Voor alle producten
    for p in producten:

        # Selecteer de productnaam
        productnaam = p[0]

        # Vergelijk case insensitive de productnaam met de keuze
        # van de gebruiker
        if keuze.lower() == productnaam.lower():
            return p                                    #[productnaam, prijs]

    # We hebben de hele lijst doorzocht, maar de keuze
    # staat er niet in
    return None

def kies_product(producten):
    # Zo lang we geen geldig product hebben
    while True:
        # Laat de gebruiker kiezen
        keuze = input("Welk product wil je? ")

        # Probeer het product te selecteren uit de lijst
        product = selecteer_product(producten, keuze)

        # Als we nu een geldig product hebben zijn we klaar
        if (product != None):
            return product
        else:
            print("Sorry, dat product bestaat niet, kies opnieuw.")
            print_producten(producten)

def print_producten(producten):
    '''
    Print alle producten

    :param  list    De lijst met producten
    '''
    for product in producten:
        print(f"{product[0]}: ${product[1]}")

producten = [
    ['Coca Cola', 1.00],
    ['Fanta', 1.15],
    ['Sprite', 0.90]
]

print("Hallo, welkom bij de frisdrankautomaat.")
print_producten(producten)

product = kies_product(producten)
print(f"Je hebt {product} besteld.")