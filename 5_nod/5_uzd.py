txt = "hidroelektrostacija"
# 1
print(txt[0])
# 2
print(txt[-1])
# 3
print(txt[::2])
# 4
print(txt[1:4])
# 5
vowel_counts = {}
for vowel in "aeiou":
    count = txt.count(vowel)
    vowel_counts[vowel] = count
counts = vowel_counts.values()
print(sum(counts))
# 6
print(txt.upper())
# 7
print(txt.lower())
# 8
print(txt.isalpha())
# 9
print(txt.replace("o", "0"))
# 10
if txt.isalpha():
    print(txt.isalpha())
else:
    print(txt.isalnum())
# 11
print(txt.find("k"))

# 2. uzd
# 1
txt_2 = "Suns skrien pakaļ kaķim, kaķis skrien pāri pļavai, bet ezītis noskatās uz skrienošajiem mājdzīvniekiem."
# 2
print(len(txt_2))
# 3
if txt_2.isdigit():
    print("Teksts satur tikai skaitļus")
else:
    print("Teksts satur gan skaitļus, gan burtus")
# 4
print(txt_2.isprintable())
# 5
