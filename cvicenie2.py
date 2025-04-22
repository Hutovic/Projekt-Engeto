# Zadané hodnoty
kosik = dict()
oddelovac = "=" * 40

sklad = {
    "mleko": [30, 5],
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}

# Dynamický výpis nabídky ze slovníku (aby sa preklepy neopakovali ako pomenrac)
def vypis_nabidku():
    print("+-----------+--------+")
    print("| POTRAVINA |  CENA  |")
    print("+-----------+--------+")
    for k, v in sklad.items():
        print(f"| {k.ljust(9)} | {str(v[0]).rjust(6)},- |")
    print("+-----------+--------+")

# Úvodní sekce
print("Vitejte u naseho nakupniho kosiku!".center(len(oddelovac)))
print(oddelovac)
vypis_nabidku()

# Hlavný cyklus
while True:
    select = input("Vložit do košíku (q = konec): ").lower()

    if select == 'q':
        break

    if select not in sklad:
        print(f"Zboží '{select}' není v nabídce.")
        continue

    if sklad[select][1] == 0:
        print(f"Zboží '{select}' není skladem.")
        continue

    if select in kosik:
        kosik[select][1] += 1
    else:
        kosik[select] = [sklad[select][0], 1]

    sklad[select][1] -= 1
    print(f"Přidáno do košíku: {select}")

# Výpis obsahu košíku
print(oddelovac)
print("Obsah vašeho košíku:")
print("+-----------+--------+-------+")
print("| ZBOŽÍ     |  CENA  | KUSŮ  |")
print("+-----------+--------+-------+")
for zbozi, (cena, kusy) in kosik.items():
    print(f"| {zbozi.ljust(9)} | {str(cena).rjust(6)},- | {str(kusy).rjust(5)} |")
print("+-----------+--------+-------+")
