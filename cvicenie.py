# původní slovník se všemi městy
mesta = {
    "Praha": 1_335_084, 
    "Brno": 382_405, 
    "Ostrava": 284_982,
    "Plzen": 175_219, 
    "Liberec": 104_261
}

# klasická smyčka 'for'
nad_sto_tisic_obyv = dict()

for mesto in mesta:
    if mesta[mesto] > 200_000:
        nad_sto_tisic_obyv[mesto] = mesta[mesto]
else:
    print(f"Klasicka smycka: {nad_sto_tisic_obyv}")

# dict comprehensions
nad_sto_tisic_obyv_compr = {
    mesto: mesta[mesto]
    for mesto in mesta
    if mesta[mesto] > 200_000
}
print(f"Dict comprehension: {nad_sto_tisic_obyv_compr}")