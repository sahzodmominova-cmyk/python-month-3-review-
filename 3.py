matn=input("matn kiriting: ")
belgi=0
orasi=0
sozlar=1
for i in matn:
    belgi+=1
    if i==" ":
        orasi+=1
        belgi-=1
        sozlar+=1
print(f"belgilar soni{belgi}")
print(f"ochiq qolgan joylar{orasi}")
print(f"sozlar soni{sozlar}")

