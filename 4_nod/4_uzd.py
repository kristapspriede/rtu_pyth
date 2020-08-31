def check_float_input(text):
    while True:
        try:
            data = float(input(text))
        except ValueError:
            print("Atvainojiet, mēģiniet vēlreiz.")
            continue
        else:
            return data


pasizmaksa_txt = "Ievadiet pašizmaksu: "
cena_txt = "Ievadiet cenu: "
atlaide_txt = "Ievadiet atlaidi: "
brivie_lidzekli_txt = "Jums pieejamie brīvie līdzekļi: "
kopeja_summa = 0
brivie_lidzekli = check_float_input(brivie_lidzekli_txt)

while True:
    preces_nosaukums = input("Ievadiet preces nosaukumu: ").lower()
    pasizmaksa = check_float_input(pasizmaksa_txt)
    cena = check_float_input(cena_txt)
    atlaide = check_float_input(atlaide_txt)
    preces_summa = round((cena - atlaide) - pasizmaksa, 2)

    if cena > pasizmaksa and cena - atlaide > pasizmaksa:
        procenti = (pasizmaksa / (cena - atlaide)) * 100
        kopeja_summa += preces_summa
        print(f"Peļņa! {round(procenti, 2)}% \n")
        print(f"Nosaukums: {preces_nosaukums.title()}, \n"
              f"Peļņa par preci: {preces_summa}€, \n"
              f"kopējā summa: {kopeja_summa}€, \n"
              f"pieejamie brivie līdzekļi: {brivie_lidzekli + preces_summa}€")
        brivie_lidzekli += preces_summa
    elif cena < pasizmaksa or cena - atlaide < pasizmaksa:
        print("Zaudējumi!\n")
        kopeja_summa += preces_summa
        print(f"Nosaukums: {preces_nosaukums.title()}, \n"
              f"Zaudējumi par preci: {preces_summa}€, \n"
              f"kopējā summa: {kopeja_summa}€, \n"
              f"pieejamie brivie līdzekļi: {brivie_lidzekli + preces_summa}€")
        brivie_lidzekli += preces_summa
    else:
        print("Neizdevīgi pārdot!")

    if brivie_lidzekli <= 0:
        print("Jūsu zaudējumi pārsniedz pieejamos brīvos līdzekļus!")
        break
    else:
        x = input('Vai būs vēl? (y/n): ')
        if x == 'y':
            continue
        elif x == 'n':
            break

