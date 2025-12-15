
# Tento program vypíše čísla od 1 do 100.
# Každé páté číslo (tj. násobek čísla 5) označí hvězdičkou.

# Funkce range(1, 101) vytvoří posloupnost čísel od 1 do 100
# (horní hranice 101 se nezapočítává)
for cislo in range(1, 101):

    # Podmínka zjišťuje, zda je číslo dělitelné 5 beze zbytku
    # Operátor % (modulo) vrací zbytek po dělení
    if cislo % 5 == 0:
        # Pokud je zbytek 0, jedná se o každé páté číslo
        # Vypíšeme číslo a hvězdičku
        print(cislo, "*")
    else:
        # Pokud číslo není násobkem 5, vypíšeme pouze číslo
        print(cislo)
