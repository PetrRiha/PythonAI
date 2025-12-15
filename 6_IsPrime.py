# Funkce is_prime(n) ověří, zda je číslo n prvočíslo.
# Prvočíslo je přirozené číslo větší než 1,
# které má právě dva dělitele: 1 a samo sebe.

def is_prime(n):
    # Pokud je číslo menší nebo rovno 1,
    # nemůže se jednat o prvočíslo.
    if n <= 1:
        return False

    # Číslo 2 je jediné sudé prvočíslo.
    if n == 2:
        return True

    # Pokud je číslo sudé a větší než 2,
    # nemůže být prvočíslem.
    if n % 2 == 0:
        return False

    # Není nutné testovat všechny dělitele až do n.
    # Stačí kontrolovat do odmocniny z n.
    # Pokud by n mělo dělitel větší než odmocnina,
    # musel by existovat i menší dělitel.
    limit = int(n ** 0.5) + 1

    # Testujeme pouze lichá čísla,
    # protože sudá už byla vyloučena.
    for delitel in range(3, limit, 2):
        # Pokud je n dělitelné beze zbytku,
        # číslo není prvočíslo.
        if n % delitel == 0:
            return False

    # Pokud jsme nenašli žádného dělitele,
    # číslo je prvočíslo.
    return True


# Příklad použití funkce:
cislo = int(input("Zadej celé číslo: "))

if is_prime(cislo):
    print("Číslo je prvočíslo.")
else:
    print("Číslo není prvočíslo.")

