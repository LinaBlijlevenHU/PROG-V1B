# Importeer het hele bestand hulpfuncties
# Je kunt nu methodes hieruit gebruiken met hulpfuncties.functienaam()
# Let op: dit kan langzaam zijn. Als we maar één methode nodig hebben kunnen
# we beter de aanpak hieronder gebruiken.
import hulpfuncties

# Importeer een enkele methode uit het bestand hulpfuncties.
# Je kunt deze nu gebruiken alsof hij direct in het bestand staat.
from hulpfuncties import opsommen2

# Maak een string aan met wat willekeurige hoofdletters.
a = "Hallo, WelkOm bij de les"
# Print deze met alleen kleine letters. (We hebben ook .upper() en .capitalize())
print(a.lower())

# Gebruik een functie uit een bestand dat we geimporteerd hebben.
# We specificeren hier ook het bestand/de module.
som = hulpfuncties.opsommen([1, 2, 3, 4, 5, 6])
print(som)

# Gebruik een geimporteerde functie direct.
# Let op: hier staat dus geen hulpfuncties met een punt voor.
som2 = opsommen2([1, 2, 3, 5, 4, 3])
print(som2)