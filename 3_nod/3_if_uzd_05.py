# 1. uzd
skaitlis = int(input("Ievadiet veselu skaitli: "))
factorial = 1

for i in range(1, skaitlis + 1):
    factorial = factorial * i
print(f"Skaitļa {skaitlis} faktoriālis ir  {factorial}.")

# 2. uzd

sk = int(input("Ievadiet skaitli: "))
txt = ""

for i in range(1, sk + 1):
    txt += str(i)
    print(txt)

# 3. uzd
no = int(input("No: "))
lidz = int(input("Lidz: "))
lidz += 1
dalitajs = int(input("Dalitajs: "))
for i in range(no, lidz):
    if i % dalitajs == 0:
        print(i)

# 4. uzd

a = 0
b = 1
print(a, b)
for i in range(1, 101):
    a += b
    print(a, end=" ")
    a, b = b, a
