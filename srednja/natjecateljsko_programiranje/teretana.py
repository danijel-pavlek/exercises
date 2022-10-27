

# vraća True jedino ako postoji barem jedan uteg (ako ih nismo sve iskoristili)
def ima_li_utega(utezi_kolicine):
    for utezi_kolicine_i in utezi_kolicine:
        if utezi_kolicine_i > 0:
            return True
    return False


# vraća True jedino ako u tom danu svi polaznici imaju potrebnu težinu utega
def je_li_dan_zadovoljen(tezine_za_jedan_dan):
    for tezine_za_jedan_dan_i in tezine_za_jedan_dan:
        if tezine_za_jedan_dan_i > 0:
            return False
    return True


# vraća True ako mogu svi trenirati u tom danu
def mogu_li_svi_trenirati(tezine_za_jedan_dan, utezi_vrijednosti, utezi_kolicine, ):
    if je_li_dan_zadovoljen(tezine_za_jedan_dan):
        # ako smo utezima pokrili sve zahtjeve, u tom danu svi polaznici mogu trenirati
        return True
    if not ima_li_utega(utezi_kolicine):
        # ako nema više utega, a dan nije zadovoljen, taj dan ne mogu svi polaznici
        # trenirati
        return False
    for i, uteg_tezina in enumerate(utezi_vrijednosti):
        if utezi_kolicine[i] > 0:
            for j in range(len(tezine_za_jedan_dan)):
                if tezine_za_jedan_dan[j] > 0:
                    # prva varijanta - ispitujemo kad ne stavimo uteg kod itog polaznika
                    result_a = mogu_li_svi_trenirati(tezine_za_jedan_dan, utezi_vrijednosti, utezi_kolicine)
                    # ako je rješenje pronađeno
                    if result_a:
                        # u tom danu svi polaznici mogu trenirati
                        return True

                    # liste utezi_kolicine_copy i tezine_za_jedan_dan_copy stvaramo kopirajući sadržaj iz
                    # originalnih zato što ne želimo da se promjena u itom koraku programa (rekurzije)
                    # odrazi u (i-1)-om
                    utezi_kolicine_copy = [kolicina_i for kolicina_i in utezi_kolicine]
                    utezi_kolicine_copy[i] -= 1
                    tezine_za_jedan_dan_copy = [tezina_i for tezina_i in tezine_za_jedan_dan]
                    tezine_za_jedan_dan_copy[j] -= tezine_za_jedan_dan[j]

                    # druga varijanta - ispitujemo kad stavimo uteg kod itog polaznika
                    result_b = mogu_li_svi_trenirati(tezine_za_jedan_dan_copy, utezi_vrijednosti, utezi_kolicine_copy)
                    # ako je rješenje pronađeno
                    if result_b:
                        # u tom danu svi polaznici mogu trenirati
                        return True
    return False



