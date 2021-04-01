# Pablo Perez
# PSID: 1770045
user_input = input()
user_list = user_input.split()

num_list = []

for value in user_list:
    if int(value) >= 0:
        num_list.append(int(value))

num_list.sort()
for value in num_list:
    print(value, "", end='')