def is_prime(n):
    """
    Funkce zjistí, zda je číslo n prvočíslo.

    Parametr:
    n (int) – celé číslo, které testujeme

    Návratová hodnota:
    True  – pokud je n prvočíslo
    False – pokud není prvočíslo
    """

    # 1. Prvočísla jsou definována pouze pro čísla větší než 1
    #    Čísla 0, 1 a záporná čísla NEJSOU prvočísla
    if n <= 1:
        return False

    # 2. Číslo 2 je nejmenší prvočíslo
    if n == 2:
        return True

    # 3. Sudá čísla větší než 2 nejsou prvočísla
    #    (protože jsou dělitelná číslem 2)
    if n % 2 == 0:
        return False

    # 4. Testujeme dělitele od 3 do odmocniny z n
    #    Používáme krok 2, protože sudá čísla už nemá smysl testovat
    i = 3
    while i * i <= n:
        # Pokud je n dělitelné i, není prvočíslo
        if n % i == 0:
            return False
        i += 2

    # 5. Pokud jsme nenašli žádného dělitele,
    #    číslo je prvočíslo
    return True
