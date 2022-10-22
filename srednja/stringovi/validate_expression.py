# Napišite program koji će ispisati je li zadan matematički izraz u kojem su zagrade
# ispravno korištene.


def evaluate_expression():
    # učitavamo izraz
    expression = input()

    # ova varijabla broji koliko ima otvorenih zagrada
    # na početku ima 0 otvorenih (dakle, lijevih) zagrada
    left_brackets = 0

    # za svaki znak u izrazu kojeg je zadao korisnik
    for character in expression:
        # ako je znak desna zagrada
        if character == ")":
            # ako nema lijevih (otvorenih) zagrada, a susreli smo desnu,
            # npr. a+)b-(c*d+e)/f, znači da je izraz neispravan
            if left_brackets < 1:
                # tada vraćamo False
                return False
            # inače je sve ok i smanjujemo broj otvorenih zagrada
            else:
                left_brackets -= 1
        # ako je znak otvorena (lijeva) zagrada
        elif character == "(":
            # uvećamo broj otvorenih zagrada
            left_brackets += 1

    # ako imamo zagrade koje nisu zatvorene
    if left_brackets > 0:
        # vratimo False
        return False
    else:
        # inače je izraz ispravan
        return True


print(evaluate_expression())

# X.gimnazija, 3.r
