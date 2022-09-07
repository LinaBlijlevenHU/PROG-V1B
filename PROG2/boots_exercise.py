# Lijst met prijzen van laarzen
lst = [159.99, 205.95, 160.00, 128.83, 175.49]

# a. Voeg een prijs toe aan de lijst
lst.append(160.00)

# b. Hoeveel verkopers hebben de laarzen voor 160?
lst.count(160.00)

# c. Minimale prijs
min_price = min(lst)

# d. Vind de index met deze minimale prijs
lst.index(min_price)

# e. Verwijder deze prijs uit de lijst
lst.remove(min_price)

# f. Sorteer de webshops van goedkoop naar duur
lst.sort()