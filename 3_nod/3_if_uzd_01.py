aitas = 255
strausi = 15

vilnas_cena = 20.5
olas_cena = 30

vilnas_cena_kopa = aitas * vilnas_cena
olu_cena_kopa = strausi * olas_cena * 15

starpiba = vilnas_cena_kopa - olu_cena_kopa

print(vilnas_cena_kopa)
print(olu_cena_kopa)

if starpiba >= 0:
    print("Jā, ir iespējams iegādāties visas olas")
else:
    print("Nē, nav iespējams iegādāties visas olas")
