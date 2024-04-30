""" Napravite program koji će za ulaz primiti 2D koordinate točaka A, B, C i X. Neka se koordinate učitavaju iz datoteke. Program treba:
1. provjeriti mogu li te tri točke biti vrhovi pravokutnika. Ukoliko ne mogu, program mora kontrolirano prestati s radom te obavijestiti 
korisnika o pogrešci, 
2. provjeriti nalazi li se točka X unutar pravokutnika ABC te obavijestiti korisnika o rezultatu,
3. izračunati dijagonalu lika. 

• ovisno o točkama A, B i C, program treba prepoznati o kojoj se vrsti pravokutnika radi (pravokutnik ili kvadar) te za svoje izvršavanje 
treba dinamički odrediti koje će se klase ili funkcije pozvati
• proširite program da moze podržavati unos točaka A, B, C, D i X od kojih svaka ima po 3 dimenzije. Neka program provjerava mogu li 
točke A, B, C i D biti vrhovi jednog kvadra. Neka provjeri nalazi li se točka X unutar kvadra ABCD. Neka izračuna prostornu dijagonalu.
• napravite da program radi s arbitrarnim brojem dimenzija sve iz prethodnog zadatka"""

# Format datoteke je predviđen za jedan objekt; jedan red za jednu koordinatu.
# Ako je u datoteci koja se učitava 2 elementa u redu, tada se radi o 2D objektu (pravokutnik). 
# Ako je 3 elementa u redu, onda se radi o 3D objektu (kvadar).

import math

# Otvaranje datoteke u istom direktoriju (test: input2d.txt ili input3d.txt)
with open('input3d.txt', 'r') as file:
    lines = file.readlines()

# Dodaj podatke iz datoteke u listu
lst = []
for line in lines:
    line = line.strip()
    elementi = line.split(',')
    broj_koordinata = len(elementi)
    lst.append(line)
print("Broj dimenzija je:",broj_koordinata)

# Ako je 2D objekt
if broj_koordinata == 2: 
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

# Ako je 2D objekt
if broj_koordinata == 2: 
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

# Ako je 2D objekt
if broj_koordinata == 2: 
    # Provjera da li je X u pravokutniku i da li točke formiraju pravokutnik
    if x_u_pravokutniku(A, B, C, X):
        if saved_double_print:
            print("Tocka X je u pravokutniku.")
        else:
            print("X nije u pravokutniku jer zadane tocke ne mogu formirati pravokutnik.")
    else:
        print(f"Tocka X {X} nije u pravokutniku.")

# Ako je 3D objekt
if broj_koordinata == 3: 
    # Dodijeli vrijednosti iz liste točkama A, B, C, X
    lst = [x.replace(' ', '') for x in lst]
    A = [float(item) for item in lst[0].split(',')]
    B = [float(item) for item in lst[1].split(',')]
    C = [float(item) for item in lst[2].split(',')]
    D = [float(item) for item in lst[3].split(',')]
    X = [float(item) for item in lst[4].split(',')]
    print(f"Tocke A: {A}, B: {B}, C: {C}, D: {D} i X: {X}")

def kvadar(A, B, C, D):
    # Euklidska udaljenost stranica
    AB = math.sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2 + (B[2] - A[2])**2)
    BC = math.sqrt((C[0] - B[0])**2 + (C[1] - B[1])**2 + (C[2] - B[2])**2)
    CD = math.sqrt((D[0] - C[0])**2 + (D[1] - C[1])**2 + (D[2] - C[2])**2)
    DA = math.sqrt((D[0] - A[0])**2 + (D[1] - A[1])**2 + (D[2] - A[2])**2)
    AC = math.sqrt((C[0] - A[0])**2 + (C[1] - A[1])**2 + (C[2] - A[2])**2)
    BD = math.sqrt((D[0] - B[0])**2 + (D[1] - B[1])**2 + (D[2] - B[2])**2)

    # Provjera istih dužina stranica
    tol = 1e-6  # Tolerancija za usporedbu decimala
    if not (math.isclose(AB, BC, abs_tol=tol) and
            math.isclose(AB, CD, abs_tol=tol) and
            math.isclose(AB, DA, abs_tol=tol) and
            math.isclose(AC, BD, abs_tol=tol)):
        return False
  
    # Izračun dijagonale
    dijagonala = math.sqrt(AB**2 + AC**2 + BD**2)
    print("Prostorna dijagonala je:", dijagonala)
    return True

# Ako je 3D objekt
if broj_koordinata == 3: 
    tocke = [(A), (B), (C), (D)]

    if kvadar(A, B, C, D):
        print("Zadane tocke formiraju kvadar.")
    else:
        print("Zadane tocke ne mogu formirati kvadar.")

# Provjera da li je X unutar kvadra
def x_u_kvadru(A, B, C, D, X):
    # Izračun udaljenosti od x, y i z koordinata
    min_x = min(A[0], B[0], C[0], D[0])
    max_x = max(A[0], B[0], C[0], D[0])
    min_y = min(A[1], B[1], C[1], D[1])
    max_y = max(A[1], B[1], C[1], D[1])
    min_z = min(A[2], B[2], C[2], D[2])
    max_z = max(A[2], B[2], C[2], D[2])

    # Provjera da li je X unutar max i min zadanih vrijednosti kvadra
    if min_x <= X[0] <= max_x and min_y <= X[1] <= max_y and min_z <= X[2] <= max_z:
        return True
    else:
        return False

# Ako je 3D objekt
if broj_koordinata == 3: 
    # Odgovor da li je X unutar kvadra
    if x_u_kvadru(A, B, C, D, X):
        print("Tocka X je unutar kvadra.")
    else:
        print("Tocka X je izvan kvadra.")