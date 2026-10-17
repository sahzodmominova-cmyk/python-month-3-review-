matn=input("matn kiriting: ")
qaysi=input("qaysi harib sonini bilmoqchisiz: ")

harif=0
for i in matn:
    if i==qaysi:
        harif+=1
print(f"siz qidiryakan harif {qaysi} matin ichida {harif} shuncha")
