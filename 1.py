print("5ta son kiritish majburiy")

for i in range(5):
    sonlar=list(map(int, input().split()))

yegindi=sum(sonlar)
ortacha=sum(sonlar)/len(sonlar)
engkata=max(sonlar)
enkichik=min(sonlar)

print(yegindi)
print(ortacha)
print(engkata)
print(enkichik)