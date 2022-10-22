# Napišite program koji će za zadani string ispisati string koji je rotiran ulijevo ili udesno
# za toliko mjesta koliko zada korisnik.


# Indeksi:
# ------------------------------------------------------------------------------------------------
# s                  =  [2, 2, 8, 9, 1, 0, 7]
# indeksi:           =   0  1  2  3  4  5  6
# negativni indeksi  =  -7 -6 -5 -4 -3 -2 -1
# indeksi kreću od 0
# Općenito, s[a:b] stvara listu elemenata od indeksa a (uključivo) do indeksa b (element na mjestu
# b NIJE uključen)
# npr.
# s[1:4] bi bilo [2, 8, 9], dakle, uključeni su elementi na indeksima 1, 2 i 3
#
# s[:] uzima sve elemente iz liste
#
# s[:a] uzima sve elemente od početka do indeksa a (opet, element na indeksu a NIJE uključen)
# npr. s[:3] bi bilo [2, 2, 8]
#
# s[a:] uzima elemente od indeksa a sve do kraja, npr.
# s[4:] bi bilo [1, 0, 7]
#
# negativni indeksi označuju elemente od kraja,
# npr.
# s[-4:-1] bi bilo isto što i s[len(s)-4:len(s)-1]
# tj. s[7-4:7-1] = s[3:6] = [9, 1, 0, 7]

# string_to_rotate = abcdefg, n=2
def rotate(string_to_rotate, n):
    if n > 0:
        print(string_to_rotate[-n:] + string_to_rotate[:-n])
    elif n < 0:
        n = abs(n)
        print(string_to_rotate[n:] + string_to_rotate[:n])
    else:
        print(string_to_rotate)

# Python, -2 -> 2
#      onPyth
#     P y t h o n
#     n P y t h o
#     o n P y t h
#     P y t h o n
#     y t h o n P
#     t h o n P y
#     _ _ _ _ _ _

print(rotate(input(), int(input())))

# X.gimnazija, 3.r
