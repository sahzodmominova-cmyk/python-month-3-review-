raqamlar=list(map(int, input("raqam kiriting: ").split()))

muspat=list(filter(lambda son: son>0,raqamlar))
manfiy=list(filter(lambda son: son<0,raqamlar))
nol=list(filter(lambda son: son==0,raqamlar))
print(f"musfat sonlar{muspat}")
print(f"manfiy sonlar{manfiy}")
print(f"0 lar{nol}")