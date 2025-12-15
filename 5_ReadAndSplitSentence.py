# Program načte větu od uživatele a zjistí,
# kolik slov se v ní nachází.

# Načtení věty z konzole.
# input() vrací celý řetězec (string), včetně mezer.
veta = input("Zadej větu: ")

# Metoda split() rozdělí text na seznam slov.
# Pokud nezadáme žádný parametr, rozdělí text
# podle libovolného počtu mezer (mezera, tabulátor, nový řádek).
slova = veta.split()

# Funkce len() vrátí počet položek v seznamu,
# což v tomto případě odpovídá počtu slov.
pocet_slov = len(slova)

# Vypíšeme výsledek do konzole.
print(f"Počet slov ve větě je: {pocet_slov}")
