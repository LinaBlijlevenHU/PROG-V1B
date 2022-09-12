# Requests the user’s name
naam = input("Voer je naam in a.u.b. ")

# Requests the user’s age
leeftijd = int(input("Voer je leeftijd in a.u.b. "))

# Prints a message saying whether the user is eligible to vote or not
if (leeftijd >= 18):
    print("Je mag stemmen!")
else:
    print("Je mag niet stemmen.")