# Napisati funkciju koja će primiti šahovsku ploču i odrediti koliko pijuna je napadnuto lovcem.
# Na ploči je jedan lovac i proizvoljno mnogo pijuna, a ostala polja su prazna. Šahovska ploča je
# modelirana listom listi. Pijuni na ploči označeni su slovom "P", lovac slovom "B", a prazna polja
# nulom, "0".


CHESS_BOARD = [
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["P", "0", "0", "0", "0", "0", "0", "P"],
    ["P", "P", "0", "0", "0", "0", "0", "P"],
    ["P", "0", "0", "0", "0", "0", "0", "P"],
    ["P", "B", "0", "0", "0", "0", "0", "P"],
    ["P", "0", "0", "0", "P", "0", "0", "P"],
    ["P", "0", "0", "0", "0", "0", "0", "P"],
    ["P", "0", "P", "P", "0", "P", "P", "P"],
]


def countAttackedPawns(board):
    bishop_x = 0
    bishop_y = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "B":
                bishop_y = i
                bishop_x = j

    upper_left = 0
    lower_left = 0
    upper_right = 0
    lower_right = 0
    for delta in range(1, 8):
        if bishop_y - delta >= 0 and bishop_x - delta >= 0:
            if board[bishop_y - delta][bishop_x - delta] == "P":
                upper_left = 1
    for delta in range(1, 8):
        if bishop_y - delta >= 0 and bishop_x + delta < 8:
            if board[bishop_y - delta][bishop_x + delta] == "P":
                upper_right = 1
    for delta in range(1, 8):
        if bishop_y + delta < 8 and bishop_x + delta < 8:
            if board[bishop_y + delta][bishop_x + delta] == "P":
                lower_right = 1
    for delta in range(1, 8):
        if bishop_y + delta < 8 and bishop_x - delta >= 0:
            if board[bishop_y + delta][bishop_x - delta] == "P":
                lower_left = 1

    return upper_left + lower_left + upper_right + lower_right


print(countAttackedPawns(CHESS_BOARD))

# X.gimnazija, 3.r
