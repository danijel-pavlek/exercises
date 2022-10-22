code = input()

# 31542
# decoded = ["" for i in range(5)]
decoded = []
for i in range(5):
    decoded.append("")

for i in range(len(code)):
    digit = int(code[i])
    decoded[digit-1] = str(i+1)

print("".join(decoded))
