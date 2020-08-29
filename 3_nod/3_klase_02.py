# Firma apsolījusi Ziemassvētku bonusu 15% apjomā no mēneša algas par KATRU nostrādāto gadu virs 2 gadiem.

# Uzdevums. Noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu.

# Izvadiet bonusu.

# Piemērs 5 gadu stāžs, 1000 Eiro alga, bonuss būs 450 Eiro.
bonuss = 0.15

alga = float(input("Kāda ir Jūsu mēneša alga? "))
gadi = float(input("Ivadiet pilnu nostrādāto gadu skaitu: "))

algas_bonuss = alga * bonuss

if gadi > 2:
    print(f"Jums ir {gadi} gadu stāžs. {alga}€ alga, bonuss būs {round(algas_bonuss * (gadi - 2), 2)}€")
else:
    print(f"Jūsu alga ir {alga}€")
