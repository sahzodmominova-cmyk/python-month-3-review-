sonlar=list(map(int, input("sonlarni kiriting bosh joy bilan").split()))
juft=0
toq=0
for i in sonlar:
    if i%2==0:
        juft+=1
    else: 
        toq+=1
print(f"juft sonlar{juft}")
print(f"toq sonlar{toq}")