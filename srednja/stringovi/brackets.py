expression = input(" ")
refactored = ""

# {[?[]?(?[] -> {[]?(?[]
# {[]

position = 0
while len(expression) > 0:
    next_step = True
    if expression[position] in "([{":
        refactored += expression[position]
    elif expression[position] in ")]}":
        refactored += expression[position]
        expression = expression[:position-1] + expression[position+1:]
        next_step = False
    elif expression[position] == "?":
        if expression[position-1] == "(":
            refactored += ")"
        if expression[position-1] == "[":
            refactored += "]"
        if expression[position-1] == "{":
            refactored += "}"

        expression = expression[:position - 1] + expression[position + 1:]
        next_step = False

    if next_step:
        position += 1
    else:
        position -= 1


print(refactored)
