with open("3-oy/11-dars/matn.txt","r", encoding="UTF=8") as f:
    data=f.read()
    caount=0
    for i in data:
        if i==" " or i=="\n":
            caount+=1
print(f"sozlar soni{caount+1}")