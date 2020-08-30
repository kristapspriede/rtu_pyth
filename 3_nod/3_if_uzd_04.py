sk = int(input("Cik skaitļus ievadīsi? "))
sk_1 = float(input("Ievadiet 1. skaitli: "))
kopa = sk_1
teksts = str(sk_1)

for i in range(sk - 1):

    darbiba = bool(int(input("Izvēlies darbibu + vai - ievadot 1 vai 0: ")))
    skaitlis = float(input("Ievadiet nākamo skaitli: "))

    if darbiba:
        kopa += skaitlis
        teksts += " + " + str(skaitlis)
    else:
        kopa -= skaitlis
        teksts += " - " + str(skaitlis)
    print(f"{teksts} = {kopa}")

