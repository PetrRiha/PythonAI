# Program pro zjištění počtu slov ve větě
# Autor: (můžeš doplnit své jméno)
# Popis: Program načte větu od uživatele a vypíše počet slov

# 1. Načtení věty od uživatele
# Funkce input() vrací textový řetězec (string), který uživatel zadá
veta = input("Zadej větu: ")

# 2. Rozdělení věty na jednotlivá slova
# Metoda split() rozdělí text podle mezer
# Výsledkem je seznam (list) slov
slova = veta.split()

# 3. Zjištění počtu slov
# Funkce len() vrací počet prvků v seznamu
pocet_slov = len(slova)

# 4. Výpis výsledku
print("Počet slov ve větě je:", pocet_slov)
