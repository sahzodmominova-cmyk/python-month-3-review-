ballar = {
    "Ali": 85,
    "Vali": 92,
    "Sardor": 78,
    "Malika": 95
}

eng_baland_ball = 0
eng_baland_isim = ""

for i in ballar:
    if ballar[i] > eng_baland_ball:
        eng_baland_ball = ballar[i]
        eng_baland_isim = i

print(f"eng katta ball: {eng_baland_ball}, uning egasi: {eng_baland_isim}")