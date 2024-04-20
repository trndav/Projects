""" • ovisno o točkama A, B i C, program treba prepoznati o kojoj se vrsti pravokutnika radi (pravokutnik ili kvadar) te za svoje izvršavanje 
treba dinamički odrediti koje će se klase ili funkcije pozvati
• proširite program da moze podržavati unos točaka A, B, C, D i X od kojih svaka ima po 3 dimenzije. Neka program provjerava mogu li 
točke A, B, C i D biti vrhovi jednog kvadra. Neka provjeri nalazi li se točka X unutar kvadra ABCD. Neka izračuna prostornu dijagonalu.
• napravite da program radi s arbitrarnim brojem dimenzija sve iz prethodnog zadatka """

# Ovaj program izračunava samo za 2D objekte (kvadar).
# Format datoteke je predviđen za jedan objekt; jedan red za jednu koordinatu.

import math

# Otvaranje datoteke u istom direktoriju
with open('input3d.txt', 'r') as file:
    lines = file.readlines()

# Dodaj podatke iz datoteke u listu
lst = []
for line in lines:
    line = line.strip()
    lst.append(line)

# Dodijeli vrijednosti iz liste točkama A, B, C, X ['0, 0', '5, 0', '0, 5', '2, 2']
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

# Odgovor da li je X unutar kvadra
if x_u_kvadru(A, B, C, D, X):
    print("Tocka X je unutar kvadra.")
else:
    print("Tocka X je izvan kvadra.")


