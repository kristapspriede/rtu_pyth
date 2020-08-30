sk_list = []
i = 1

while i <= 3:
    sk_list.insert(i - 1, int(input(f"Ievadiet {i}. skaitli: ")))
    i += 1

sk_list.sort()

for j in sk_list:
    print(j)



