# Korisnik unosi brojeve. Treba ispisati koliko je brojeva veće od svih svojih susjeda u unesenom nizu.


# učitamo količinu brojeva
n = int(input("Upišite količinu brojeva: "))

# niz u kojeg ćemo pohraniti brojeve
numbers = []
# pravimo n iteracija
# ako se i ne koristi, možemo napisati: for _ in range(n):
for i in range(n):
    # učitamo i-ti broj
    numbers.append(int(input(" ")))



# iteriramo kroz indekse elemenata osim prvog i zadnjeg,
# tj. kroz indekse 1, 2, ..., duljina niza - 2
numbers_with_smaller_neighbours = 0
for i in range(1, len(numbers)-1):
    # ako su oba susjeda manja od trenutnog broja,
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        # uvećaj brojač za 1
        numbers_with_smaller_neighbours += 1

# provjera za element na indeksu 0:
if numbers[0] > numbers[1]:
    numbers_with_smaller_neighbours += 1

# provjera za posljednji element:
if numbers[-1] > numbers[-2]:
    numbers_with_smaller_neighbours += 1

# ispis
print(numbers_with_smaller_neighbours)

# X.gimnazija, 3.r
