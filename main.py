"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tomáš Hutňan
email: tomas.hutnan@internationalsos.cz
"""

#Texty k analyze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Registrovaní uživatelé
REGISTERED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

#Prihlasovani
cara=("-" * 40)
user=input("username:")
password=input("password:")
print(cara)

if user in REGISTERED_USERS:
    if REGISTERED_USERS[user]== password:
        print("Welcome to the app,", user, "\nWe have", len(TEXTS), "texts to be analysed.")
    else:
        print("Incorrect password, terminating the program..")
        quit()  
else:
    print("Unregistered user, terminating the program..")
    quit()  



#Vyber textu
text_number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
if not text_number.isdigit() or not (1 <= int(text_number) <= len(TEXTS)):
    print("Zly vyber, ukoncujem program...")
    exit()

print(cara)


#Lists tagging
zoznam_slov=TEXTS[int(text_number) -1].split() 
pocet_slov=len(zoznam_slov) 
ciste_slova = [slovo.strip(".,!?") for slovo in zoznam_slov if slovo.strip(".,!?")]


#Pocty
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
numeric_sum = 0
vyskyt_dlzok = {}

for slovo in ciste_slova: 
    if slovo.istitle():
        titlecase_count += 1
    if slovo.isupper():
        uppercase_count += 1
    if slovo.islower():
        lowercase_count += 1
    if slovo.isdigit():
        numeric_count += 1
        numeric_sum += int(slovo)

    dlzka = len(slovo)
    if dlzka in vyskyt_dlzok:
        vyskyt_dlzok[dlzka] += 1
    else:
        vyskyt_dlzok[dlzka] = 1

#Vystup
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print(cara)
print('LEN|  OCCURENCES  |NR.')
print(cara)

#Graf
for dlzka in sorted(vyskyt_dlzok):
    pocet = vyskyt_dlzok[dlzka]
    hviezdicky = "*" * pocet
    print(f"{dlzka:>3} | {hviezdicky:<15} | {pocet}")
