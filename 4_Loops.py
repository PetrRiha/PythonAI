
# Program vypíše všechna čísla od 1 do 100.
# Každé páté číslo označí hvězdičkou (*).

# Funkce range(1, 101) vytvoří posloupnost čísel od 1 do 100.
# Horní hranice (101) se do rozsahu nezahrnuje.
for cislo in range(1, 101):

    # Operátor % (modulo) vrací zbytek po dělení.
    # Pokud je číslo dělitelné 5 beze zbytku,
    # výraz cislo % 5 == 0 bude True.
    if cislo % 5 == 0:
        # Každé páté číslo vypíšeme s hvězdičkou.
        print(f"{cislo} *")
    else:
        # Ostatní čísla vypíšeme normálně.
        print(cislo)

