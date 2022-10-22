# Korisnik zadaje izraz oblika: 1+3+3+1+2+1. Dakle, dozvoljena su četiri znaka: 1, 2, 3 i +.
# Treba ispisati izraz nakon sortiranja brojeva, npr. za gornji niz program bi ispisao: 1+1+1+2+3+3


# učitavamo izraz 1+1+3+1+2+3
expression = input("Upišite izraz: ")

# brojimo koliko ima znakova "1" u učitanom nizu
n_digit1 = expression.count("1")
# brojimo koliko ima znakova "2" u učitanom nizu
n_digit2 = expression.count("2")
# brojimo koliko ima znakova "3" u učitanom nizu
n_digit3 = expression.count("3")

# u ovaj niz ćemo spremati znakove
final_expression_data = []
# idemo od 0 do broj_jedinica-1
for i in range(n_digit1):
    # stavimo u niz jedinicu
    final_expression_data.append("1")

# isto napravimo za dvojke
for i in range(n_digit2):
    final_expression_data.append("2")

# i za trojke
for i in range(n_digit3):
    final_expression_data.append("3")

# ["1", "1", "2"]
# 1+1+2

# stavimo u konačni niz prvu brojku
final_expression = final_expression_data[0]

# idemo kroz niz i stavljamo druge znamenke
# počevši od one na indeksu 1
for number_str in final_expression_data[1:]:
    # ne smijemo zaboraviti "+"
    final_expression += "+" # final_expression = final_expression + "+"
    # nakon toga ide broj
    final_expression += number_str

# ispišemo rezultat
print(final_expression)

# X.gimnazija, 3.r
