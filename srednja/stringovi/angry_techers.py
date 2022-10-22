# 17
# .....U....U......
# xxx.xxxx.xxxxx.xx
# .U..U.U..........
#
# 10
# UU.UUU..UU
# XX.XXX.XXX
# U...UU....

n = int(input(" "))
left_path = input(" ")
wall = input(" ")
right_path = input(" ")

left_path_teachers = []
right_path_teachers = []
left_index = 0
for i in range(n):
    if wall[i] == ".":
        left_path_teachers.append(left_path[left_index:i].count("U"))
        right_path_teachers.append(right_path[left_index:i].count("U"))
        left_index = i + 1
left_path_teachers.append(left_path[left_index:n].count("U"))
right_path_teachers.append(left_path[left_index:n].count("U"))

min_angry_teachers = right_path_teachers[0]
for i in range(1, len(left_path_teachers)-1):
    min_angry_teachers += min(left_path_teachers[i], right_path_teachers[i])
min_angry_teachers += left_path_teachers[-1]

print("Minimal number of angry teachers: " + str(min_angry_teachers))
