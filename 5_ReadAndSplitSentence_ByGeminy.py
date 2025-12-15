# Funkce pro zjištění počtu slov ve větě
def spocitej_slova(veta):
    """
    Načte textový řetězec (větu) a vrátí počet slov v ní.
    Slova jsou rozdělena pomocí metody split().
    """
    
    # 1. Použití metody split() k rozdělení věty na seznam slov.
    # Bez argumentu split() standardně rozděluje řetězec podle bílých znaků 
    # (mezery, tabulátory, nové řádky) a inteligentně ignoruje vícenásobné mezery.
    # Výsledek je seznam (list), kde každý prvek je jedno slovo.
    seznam_slov = veta.split()
    
    # Příklad:
    # Pokud je veta = "Toto je testovací věta", pak 
    # seznam_slov bude ['Toto', 'je', 'testovací', 'věta']

    # 2. Zjištění délky seznamu.
    # Funkce len() vrací počet prvků v seznamu (tj. počet slov).
    pocet_slov = len(seznam_slov)
    
    # 3. Vrácení výsledku.
    return pocet_slov

# Hlavní část programu
def main():
    # 1. Výzva pro uživatele k zadání věty.
    # Funkce input() načte text zadaný uživatelem jako řetězec.
    print("Prosím, zadejte větu pro spočítání slov:")
    vstupni_veta = input()
    
    # Kontrola, zda uživatel vůbec něco zadal.
    # Pokud je vstup prázdný, nebudeme volat funkci a jen ohlásíme 0.
    if not vstupni_veta.strip():
        print("\nZadaná věta je prázdná nebo obsahuje jen mezery.")
        pocet = 0
    else:
        # 2. Volání funkce pro spočítání slov.
        pocet = spocitej_slova(vstupni_veta)
    
    # 3. Vypsání výsledku.
    print("\n--- Výsledek ---")
    print(f"Zadaná věta: '{vstupni_veta}'")
    print(f"Počet slov ve větě je: {pocet}")

# Spuštění hlavní funkce, pokud je skript spuštěn přímo
if __name__ == "__main__":
    main()
