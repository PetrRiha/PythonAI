import math # Importujeme modul math pro použití funkce sqrt()

def is_prime(n):
    """
    Funkce zjišťuje, zda je dané celé číslo 'n' prvočíslo.
    Vrací True, pokud je 'n' prvočíslo, jinak False.
    
    Argument:
        n (int): Kladné celé číslo, které má být testováno.
    """
    
    # --- Krok 1: Základní případy ---
    
    # Prvočíslo musí být větší než 1. 
    if n <= 1:
        # 1 a všechna záporná čísla nejsou prvočísla.
        return False
        
    # Číslo 2 je jediné sudé prvočíslo.
    if n == 2:
        return True
        
    # --- Krok 2: Eliminace sudých čísel ---
    
    # Jakékoli sudé číslo větší než 2 (např. 4, 6, 8, ...) nemůže být prvočíslo.
    # Operátor % (modulo) vrací zbytek po dělení.
    # Pokud n % 2 == 0, znamená to, že je n dělitelné 2 beze zbytku.
    if n % 2 == 0:
        return False
        
    # --- Krok 3: Hledání dělitelů (Optimalizace) ---
    
    # Stačí testovat dělitele pouze do odmocniny z n (sqrt(n)). 
    # Důvod: Pokud má číslo n dělitele většího než sqrt(n), musí mít nutně 
    # i menšího dělitele, kterého bychom už našli.
    limit = int(math.sqrt(n)) 
    
    # Začínáme testovat od 3 a zvětšujeme krok o 2 (i += 2).
    # Můžeme přeskočit všechna sudá čísla, protože jsme je už eliminovali v Kroku 2.
    # Zkontrolujeme, zda je n dělitelné i (se zbytkem 0).
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            # Našli jsme dělitele, číslo NENÍ prvočíslo.
            return False
            
    # --- Krok 4: Výsledek ---
    
    # Pokud smyčka proběhla bez nalezení dělitele, číslo je prvočíslo.
    return True

# --- Příklady použití funkce ---

def main():
    print(f"Test 7 (očekáváme True): {is_prime(7)}")
    print(f"Test 12 (očekáváme False): {is_prime(12)}")
    print(f"Test 2 (očekáváme True): {is_prime(2)}")
    print(f"Test 1 (očekáváme False): {is_prime(1)}")
    print(f"Test 131 (očekáváme True): {is_prime(131)}")
    print(f"Test 91 (očekáváme False, 91 = 7 * 13): {is_prime(91)}")

# Spuštění hlavní části programu
if __name__ == "__main__":
    main()