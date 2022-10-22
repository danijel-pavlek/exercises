# Napišite program koji će u zadanom izrazu izbrisati sva pojavljivanja stringa abc sve dok ga ima
# u stringu. Dakle, ispis ne smije u sebi sadržavati podniz abc.


# aabcbckabc      abc
# s.replace("abc", "")
# "k" ->

# unosimo prvi string iz kojeg trebamo brisati substringove
data = input(" ")
to_replace = input(" ")

# brojač koji označuje koliko smo puta izvršili operaciju replace
number_of_replaces_needed = 0
# dok u stringu data ima substringa kojeg želimo obrisati
while to_replace in data:
    # 'obrišemo' substring - zapravo kreiramo novi string i pridjelimo ga varijabli data
    data = data.replace(to_replace, "")
    # inkrementiramo brojač
    number_of_replaces_needed += 1

# ispišemo rezultat
print(number_of_replaces_needed)

# X.gimnazija, 3.r
