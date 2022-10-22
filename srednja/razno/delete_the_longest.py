# Korisnik unosi string formiran od riječi koje su međusobno odvojene jednim razmakom.
# Ispišite string koji nastaje brisanjem najveće riječi u zadanom stringu.
# BONUS: rješite zadatak tako da se omogući da bude proizvoljno mnogo razmaka između susjednih riječi.


string = input("Upišite izraz:")

# ovime ćemo iz stringa dobiti niz riječi
words = string.split(" ")

# [abc, defghu, ...]
# najdužom riječi proglasimo onu na indeksu 0
longest_word = words[0]
# može i na sljedeći način:  for word in words:
# words[1:] je kreiranje novog niza sa istim elementima
# kao i u polju words, samo što ovdje kreće od indeksa 1

for word in words[1:]:
    # jedino ako naiđemo na riječ dulju od trenutne najdulje,
    # tada spremimo nju i njezinu duljinu
    if len(word) > len(longest_word):
        longest_word = word

# 'replaceamo' longest word + " " sa "", svrha " " je da se makne jedan ekstra razmak koji bi
# ostao da ga nismo "dodali" na longest word
string_with_removed_longest_word = string.replace(longest_word + " ", "")

# ispišemo rezultat
print(string_with_removed_longest_word)


# X.gimnazija, 3.r
