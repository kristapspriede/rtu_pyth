"""

Klients pieejot pie kases norāda, vai ir pieejama klienta karte.

Klients ievadīs 4 preces.

Klientu karte, katrai precei dod 11% atlaidi, bet pirmajai precei 12% atlaidi

Klients ievada preces nosaukumu un cenu

Programma izvada pilnā teikumā preces nosaukumu un cenu, ja ir pieejama klientu karte izvada cenu ar atlaidi

Visas cenas ir jāsaskaita un beigās jāizvada

Kopējā atlaižu summa arī ir jāsaskaita un jāizvada

"""

irKarte = bool(int(input("Vai Jums ir Klienta karte? (1 / 0): ")))
summa = 0

for i in range(4):
    nosaukums = input("Ievadiet preces nosaukumu: ").lower()
    cena = float(input("Ievadiet preces cenu: "))

    if irKarte:
        if i == 0:
            print(f"Prece: {nosaukums.title()}, cena - {cena}€, cena ar atlaidi - {round(cena * 0.88, 2)}€")
            summa += round(cena * 0.88, 2)
        else:
            print(f"Prece: {nosaukums.title()}, cena - {cena}€, cena ar atlaidi - {round(cena * 0.89, 2)}€")
            summa += round(cena * 0.89, 2)
    else:
        print(f"Prece: {nosaukums.title()}, cena - {cena}€")
        summa += round(cena)

print(f"Kopējā summa - {summa}€")
