temp = float(input('Ievadiet savu temeratūru: '))

if temp > 37:
    print(f"Jūsu t ir {temp}. Iespējams drudzis")
elif temp >= 35:
    print(f"Jūsu t ir {temp}. Viss kārtībā")
else:
    print(f"Jūsu t ir {temp}. Nav par aukstu?")