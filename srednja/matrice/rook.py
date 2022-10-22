# Napisati funkciju koja će primiti šahovsku ploču i odrediti koliko pijuna je napadnuto topom.
# Na ploči je jedan top i proizvoljno mnogo pijuna, a ostala polja su prazna. Šahovska ploča je
# modelirana listom listi. Pijuni na ploči označeni su slovom "P", top slovom "R", a prazna polja
# nulom, "0".


CHESS_BOARD = [
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["P", "0", "0", "0", "0", "0", "0", "P"],
    ["P", "P", "0", "0", "0", "0", "0", "P"],
    ["P", "0", "0", "0", "0", "0", "0", "P"],
    ["P", "R", "0", "0", "0", "0", "0", "P"],
    ["P", "0", "0", "0", "P", "0", "0", "P"],
    ["P", "0", "0", "0", "0", "0", "0", "P"],
    ["P", "0", "P", "P", "P", "P", "P", "P"],
]


def countAttackedPawns(board):
    rookX = 0
    rookY = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "R":
                rookY = i
                rookX = j
    up = 0
    down = 0
    left = 0
    right = 0
    for i in range(0, rookY):
        if board[i][rookX] == "P":
            up = 1
    for i in range(rookY+1, 8):
        if board[i][rookX] == "P":
            down = 1
    for i in range(0, rookX):
        if board[rookY][i] == "P":
            left = 1
    for i in range(rookX+1, 8):
        if board[rookY][i] == "P":
            right = 1

    return up + down + left + right


print(countAttackedPawns(CHESS_BOARD))

# X.gimnazija, 3.r
