# TODO promenne
sklad = {
    'mleko':    [30,  5],    # index 0 -> cena; index 1 -> mnozstvi
    'maso':     [100, 1],
    'banan':    [30, 10],
    'jogurt':   [10,  5],
    'chleb':    [20,  5],
    'jablko':   [10, 10],
    'pomeranc': [15, 10], 
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
"""
oddelovac = '=' * 40

# TODO kosik

# TODO Pozdrav a vypsani nabidk

# TODO cely cyklus


# TODO vypis kosiku

print("Vitejte u naseho nakupniho kosiku!  ")
print(oddelovac)
print(nabidka)

kosik={}


while (zbozi:=input("Zadej zbozi: ")) !='Konec':
         
    if zbozi not in sklad:
        print(f'{zbozi.title()} bohuzel neni v nabidce')
        continue

    elif zbozi not in kosik and sklad[zbozi][1]>0 :
        kosik[zbozi]= [sklad[zbozi][0],1]
        sklad[zbozi][1] = sklad[zbozi][1] - 1

    elif zbozi in kosik and sklad[zbozi][1] >0:
        kosik[zbozi][1]+=1
        sklad[zbozi][1] -=1   

    elif sklad[zbozi][1] == 0:
        print(f"Zbozi {zbozi} neni na sklade.")
        continue

    celkova_cena=0
    for zbozi, (cena, kusy) in kosik.items():
        celkova_cena += cena * kusy

else:
    print(kosik)
    print(sklad)
    print(celkova_cena)

