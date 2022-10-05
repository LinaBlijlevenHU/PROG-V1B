# Frisdrank-machine met dictionaries
# Voorbeeld uit de les van 05/10/2022

def print_producten(producten):
    '''
    Print alle producten

    :param  list    De lijst met producten
    '''
    for productnaam, prijs in producten.items():
        print(f"{productnaam}: ${prijs}")

def selecteer_product(producten, keuze):
    '''
    Checkt of een bepaald product in de bestaande producten staat

    :param      dict        Dictionary met producten
    :param      string      De keuze van de gebruiker
    :return     mixed       Product dict of None
    '''
    if (keuze in producten.keys()):
        return {
            'naam': keuze,
            'prijs': producten[keuze]
        }
    else:
        return None

def kies_product(producten):
    '''
    Laat de gebruiker opnieuw selecteren tot we een geldig product hebben.

    :param  list    Lijst met producten
    :return dict    Product (naam en prijs)
    '''

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

producten = {
    'Coca Cola': 1.00,
    'Fanta': 1.15,
    'Sprite': 0.90
}

print("Hallo, welkom bij de frisdrankautomaat.")
print_producten(producten)
product = kies_product(producten)
print(f"Je hebt {product['naam']} besteld. Dit kost {product['prijs']}")