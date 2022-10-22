keyword = input(" ")
code = input(" ")

code_numbers = [int(number_str) for number_str in code]
# code_numbers = []
# for i in range(len(code)):
#     code_numbers.append(int(code[i]))

decoded = ""
for code_number in code_numbers:
    if code_number - 1 < len(keyword) and code_number > 0:
        decoded += keyword[code_number - 1]

print(decoded)
