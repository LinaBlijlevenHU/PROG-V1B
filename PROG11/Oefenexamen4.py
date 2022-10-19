# Opdracht 4:
# Schrijf een programma waarin een gebruiker getallen moet invoeren. Dit gaat door totdat de gebruiker ‘stop’ intoetst.
# De getallen moeten met elkaar vermenigvuldigd worden. Print het resultaat. - https://prnt.sc/xkYL5YKbrfSO
import math

# Begin leeg, zodat we altijd één getal vragen
vraag_getal = True

# Product van de lijst (met for-loop)
lijst_product2 = 1

# Vraag om getallen tot de gebruiker stop zegt
while vraag_getal:

    # Vraag om een nieuw getal
    getal = input("Voer een getal in a.u.b. (of typ 'stop' om te stoppen) ")

    # Moeten we stoppen?
    if (getal == "stop"):
        vraag_getal = False
    else:
        # Vermenigvuldigen het getal (als int) met het product tot nu toe
        lijst_product2 = int(getal) * lijst_product2

print(f"Klaar met getallen vragen.")

# Product van de lijst (met math, als je een lijst hebt gemaakt)
#lijst_product1 = math.prod(getallenlijst)
#print(f"Het product van de lijst is {lijst_product1}")

print(f"Het product van de lijst is {lijst_product2}")