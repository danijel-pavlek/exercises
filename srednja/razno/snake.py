# korisnik učitava broj n
n = int(input(" "))
# korisnik učitava redak
row = input(" ")
# korisnik učitava broj sekundi
t = int(input(" "))

# result_left će pamtiti stanje ploče, ova naredba sve znakove iz redova što ga je upisao korisnik
# stavlja u listu result_left. Tijekom izvršavanja programa će se ova lista mijenjati, ovisno gdje se zmija
# pomakne, tj. što pojede.
result_left = [s for s in row]
# indeks glave zmije
snake_left_index = -1
# prolazimo kroz red kojeg zadaje korisnik
# želimo pronaći prvi znak 'o'
for i in range(len(row)):
    # ako je znak 'o'
    if row[i] == "o":
        # upamtimo taj indeks
        snake_left_index = i
        # izlazimo iz petlje odmah, tj. ona se više ne izvršava,
        # dakle program će iz break-a skočiti na liniju: snake_right_index = -1
        break
# indeks zmijinog repa
snake_right_index = -1
# slično kao i za glavu, tražimo rep
# i će poprimati vrijednosti 1, 2, 3, ..., len(row)
# gdje je len(row) broj znakova niza row što ga je unio korisnik
# u sljedećih nekoliko linija ćemo zapravo ići od kraja prema početku niza
for i in range(1, len(row)+1):
    # izraz len(row)-i će poprimati vrijednosti len(row)-1, len(row)-2, len(row)-3, ..., 0
    # kad, krećući se od kraja prema početku, stignemo do znaka 'o'
    if row[len(row)-i] == "o":
        # upamtimo taj indeks
        snake_right_index = len(row)-i
        # izlazimo iz petlje
        # program skače na liniju: step = 0
        break

# trenutno vrijeme (tj. broj sekundi koje su prošle)
step = 0
# je li supermoć uključena
superpower_enabled = False
# sve dok je ukupno vrijeme - trenutni broj sekundi veće od nule
while t > 0:
    # ako je zmijina glava već na skroz lijevom mjestu
    if snake_left_index == 0:
        # ako je i rep na skroz lijevom mjestu, tj.
        # ako je zmija duljine 1 i na skroz lijevom mjestu
        if snake_right_index == 0:
            # zmija nestaje
            result_left[snake_right_index] = "."
            # izlazimo iz while petlje
            break
        else:
            # na mjestu repa stavljamo točku (prazno mjesto)
            result_left[snake_right_index] = "."
            # rep se pomiče za jedan ulijevo
            snake_right_index -= 1
    else:
        # ako je sljedeće lijevo polje prazno ili supermoć
        if result_left[snake_left_index - 1] == "." or result_left[snake_left_index - 1] == "!":
            # ako je supermoć
            if result_left[snake_left_index - 1] == "!":
                # postavi supermoć na True
                superpower_enabled = True
            # glava se pomiče na jedno mjesto ulijevo
            result_left[snake_left_index - 1] = "o"
            # dakle, indeks glave je sad za jedan manji jer se zmija pomiče ulijevo
            snake_left_index -= 1
            # rep se pomaknuo, zato na trenutno njegovo mjesto ide prazno polje, dakle točkica
            result_left[snake_right_index] = "."
            # indeks repa se pomakne ulijevo, isto kao što je bio slučaj za glavu
            snake_right_index -= 1
        # ako je na sljedećem mjestu (dakle, lijevo kamo se glava treba pomaknuti)
        elif result_left[snake_left_index - 1] == "+":
            # na to mjesto postavi zmijinu glavu, tj. znak 'o'
            result_left[snake_left_index - 1] = "o"
            # pomakni glavu jedno mjesto ulijevo
            snake_left_index -= 1
        # ako je na sljedećem mjestu (dakle, lijevo kamo se glava treba pomaknuti) otrov
        elif result_left[snake_left_index - 1] == "x":
            # ako je supermoć uključena, isti je efekt kao da je normalna hrana
            if superpower_enabled:
                # dakle, na sljedeće mjesto postavimo zmijinu glavu
                result_left[snake_left_index - 1] = "o"
                # i smanjimo indeks glave za jedan
                snake_left_index -= 1
            else:
                # ovo je situacija kad je duljina zmije 1 (glava i rep na istom indeksu), a zmija
                # dođe na otrov
                if snake_right_index - snake_left_index == 0:
                    # zmija nestaje
                    result_left[snake_right_index] = "."
                    # izlazimo iz while petlje
                    break
                # situacija kad je zmija došla na otrov, a ima duljinu veću od 1
                else:
                    # na lijevo mjesto stavimo zmijinu glavu
                    result_left[snake_left_index - 1] = "o"
                    # trebamo umanjiti indeks glave zmije
                    snake_left_index -= 1
                    # pomaknemo rep, tj. na trenutno mjesto repa ide točka, kao i obično
                    result_left[snake_right_index] = "."
                    # ova naredba ide zato što je u pitanju otrov
                    result_left[snake_right_index - 1] = "."
                    # -2, dakle, zato što je otrovna hrana, inače bi bilo -1
                    snake_right_index -= 2
        # situacija kad je sljedeće mjesto za glavu zmije zid
        elif result_left[snake_left_index - 1] == "#":
            # i će imati vrijednosti 0, 1, 2, ..., len(result)-1
            # tj. idemo kroz sve pozicije u listi koja sprema rezultat
            # i sve znakove zmijinog tijela, tj, 'o' pretvaramo u '.'
            for i in range(len(result_left)):
                # ako je na trenutnom mjestu 'o'
                if result_left[i] == "o":
                    # na to mjesto u listi stavimo točku
                    result_left[i] = "."
            # izlazimo iz while petlje
            break
    # uvećavamo trenutno vrijeme za 1
    t -= 1

# listu pretvaramo u string, npr. [".", ".", "o", "x"] -> "..ox"
result_left = "".join(result_left)
# ispišemo rezultat
print(result_left)

# ulaz: x.+o!xxx+
#  t=1: x.oo!xxx+
#  t=2: xoo.!xxx+
#  t=3: o...!xxx+
#  t=4: ....!xxx+
