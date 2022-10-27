

# funkcija za izračunavanje sume stupaca
def izracunaj_sumu_stupaca(max_n, max_m):
    # stvorimo listu u kojoj će biti liste elemenata, dakle, imamo listu redaka, a svaki redak
    # je broj
    lista_listi = []
    # i ide od 0 do max_n (0, 1, 2, ..., max_n-1)
    for i in range(max_n):
        # u listu stavljamo novu, praznu listu
        # (to će biti jedan redak brojeva)
        lista_listi.append([])
        # j ide od 0 do max_m (0, 1, 2, ..., max_m-1)
        for j in range(max_m):
            # korisnik učitava broj koji se sprema u varijablu koju smo nazvali number_to_append
            # moglo je i biti samo: number_to_append = int(input())
            number_to_append = int(input("Unesite broj na poziciji " + str(i) + ", " + str(j) + ": "))
            # lista_listi[-1] dohvaća posljednju umetnutu listu, tj. zadnji redak koji zasad postoji u
            # listi lista, append(number_to_append) stavlja u taj redak broj kojeg je korisnik učitao
            lista_listi[-1].append(number_to_append)
    # stvara listu od max_m nula po imenu sume_stupaca
    # dakle, sume_stupaca će biti: [0, 0, 0, ..., 0] -> unutra ima max_m nuli
    # umjesto _ može ići bilo što, npr, i, j, k, number, ...
    # _ se može staviti u list comprehension kad tu varijablu ne koristimo u izrazu lijevo od for (u našem
    # primjeru taj izraz je 0)
    sume_stupaca = [0 for _ in range(max_m)]
    # i ide od 0 do max_m (0, 1, 2, ..., max_m-1)
    # ovim indeksom ćemo pristupati stupcu
    for i in range(max_m):
        # j ide od 0 do max_n (0, 1, 2, ..., max_n-1)
        # ovim indeksom ćemo pristupati retku
        for j in range(max_n):
            # u sume_stupaca na i-to mjesto pribraja element na mjestu (j, i)
            sume_stupaca[i] += lista_listi[j][i]
    # vratimo listu sumi iz funkcije
    return sume_stupaca


# korisnik učitava broj redaka
max_n = int(input("Unesite maksimalni broj redaka: "))
# korisnik učitava broj stupaca
max_m = int(input("Unesite maksimalni broj stupaca: "))

# poziva se funkcija izracunaj_sumu_stupaca kojoj zadamo argumente max_n i max_m i potom
# ta funkcija vrati rezultat - sumu pojedinih stupaca
lista_sumi_stupaca = izracunaj_sumu_stupaca(max_n, max_m)

# ispišemo rezultat kojeg je funkcija vratila
print(lista_sumi_stupaca)
