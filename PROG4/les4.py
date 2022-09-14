'''
Volgorde van if-else statements.
Voer de volgende voorbeelden eens uit, zodat je goed kan zien hoe ze verschillen.

Welke versie vindt jij het duidelijkst?
'''

# Stel een leeftijd in
leeftijd = 18

# Twee if-statements
print("VERSIE 1")
if (leeftijd >= 16):
    print("Vanaf nu mag je scooter rijden")
if (leeftijd >= 18):
    print("Vanaf nu mag je drinken")

# If + elif (hoog naar laag)
print("VERSIE 2")
if (leeftijd >= 18):
    print("Vanaf nu mag je drinken")
elif (leeftijd >= 16):
    print("Vanaf nu mag je scooter rijden")

# If + elif (laag naar hoog)
print("VERSIE 3")
if (leeftijd >= 16):
    print("Vanaf nu mag je scooter rijden")
elif (leeftijd >= 18):
    print("Vanaf nu mag je drinken")