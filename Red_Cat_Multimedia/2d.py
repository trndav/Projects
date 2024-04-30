""" Napravite program koji će za ulaz primiti 2D koordinate točaka A, B, C i X. Neka se koordinate učitavaju iz datoteke. Program treba:
1. provjeriti mogu li te tri točke biti vrhovi pravokutnika. Ukoliko ne mogu, program mora kontrolirano prestati s radom te obavijestiti 
korisnika o pogrešci, 
2. provjeriti nalazi li se točka X unutar pravokutnika ABC te obavijestiti korisnika o rezultatu,
3. izračunati dijagonalu lika. 
"""

# Ovaj program izračunava samo za 2D objekte (pravokutnik).
# Format datoteke je predviđen za jedan objekt; jedan red za jednu koordinatu.

import math

# Otvaranje datoteke u istom direktoriju
with open('input2d.txt', 'r') as file:
    lines = file.readlines()

# Dodaj podatke iz datoteke u listu
lst = []
for line in lines:
    line = line.strip()
    elementi = line.split(',')
    broj_koordinata = len(elementi)
    lst.append(line)
print("Broj dimenzija je:",broj_koordinata)

if broj_koordinata == 2:
    pass

# Dodijeli vrijednosti iz liste točkama A, B, C, X ['0, 0', '5, 0', '0, 5', '2, 2']
lst = [x.replace(' ', '') for x in lst]
A = [int(item) for item in lst[0].split(',')]
B = [int(item) for item in lst[1].split(',')]
C = [int(item) for item in lst[2].split(',')]
X = [int(item) for item in lst[3].split(',')]
print("Tocke A, B, C i X:", A, B, C, X)

def udaljenost(tocka1, tocka2):
    return math.sqrt((tocka2[0] - tocka1[0])**2 + (tocka2[1] - tocka1[1])**2)

def pravokutnik(tocka):    
    distance = [udaljenost(tocka[i], tocka[j]) for i in range(3) for j in range(i+1, 3)]   
    print("Dijagonalna udaljenost je:",distance[2])
    return len(set(distance)) == 2

# tocke = [(0, 0), (5, 0), (0, 5)]
tocke = [(A), (B), (C)]
saved_double_print = pravokutnik(tocke) # Dodana funkcija u varijablu kako bi izbjeglo dupli print dijagonale
if saved_double_print:
    print("Zadane tocke formiraju pravokutnik.")
else:
    print("Zadane tocke ne mogu formirati pravokutnik.")

# Provjera točke X
def x_u_pravokutniku(A, B, C, X):
    # Izračun četvrte točke pravokutnika
    D = (C[0] + (B[0] - A[0]), C[1] + (B[1] - A[1]))
    
    # Izračun stranica
    min_x = min(A[0], B[0], C[0], D[0])
    max_x = max(A[0], B[0], C[0], D[0])
    min_y = min(A[1], B[1], C[1], D[1])
    max_y = max(A[1], B[1], C[1], D[1])

    # Provjera da li je X unutar granica pravokutnika
    return min_x <= X[0] <= max_x and min_y <= X[1] <= max_y

# Provjera da li je X u pravokutniku i da li točke formiraju pravokutnik
if x_u_pravokutniku(A, B, C, X):
    if saved_double_print:
        print("Tocka X je u pravokutniku.")
    else:
        print("X nije u pravokutniku jer zadane tocke ne mogu formirati pravokutnik.")
else:
    print(f"Tocka X {X} nije u pravokutniku.")
