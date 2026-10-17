def tekshir(son):
    if son>0 and son%2==0:
        return "musfat juft"
    elif son<0 and son%2==0:
        return "manfiy juft"
    elif son>0:
        return "son juft emas"
    elif son<0:
        return "son manfiy juf emas"
    else:
        return "o sonini bolib bolmaydi"
son=int(input("son kiriting: "))
print(tekshir(son))