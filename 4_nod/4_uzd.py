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

while True:
    brivie_lidzekli = check_float_input(brivie_lidzekli_txt)
    pasizmaksa = check_float_input(pasizmaksa_txt)
    cena = check_float_input(cena_txt)
    atlaide = check_float_input(atlaide_txt)

    if cena > pasizmaksa and cena - atlaide > pasizmaksa:
        procenti = (pasizmaksa / (cena - atlaide)) * 100
        kopeja_summa += (cena - atlaide) - pasizmaksa
        print(f"Peļņa! {round(procenti, 2)}%")

    elif cena < pasizmaksa or cena - atlaide < pasizmaksa:
        print("Zaudējumi!")
        kopeja_summa += (cena - atlaide) - pasizmaksa

    else:
        print("Neizdevīgi pārdot!")

    x = input('Vai būs vēl? (y/n): ')
    if x == 'y':
        continue
    elif x == 'n':
        break
