raqamlar=list(map(int, input("raqam kiriting: ").split()))

juft=list(filter(lambda son: son%2==0,raqamlar))
kvdrat=list(map(lambda son: son**2,juft))
print(f"juf sonlkar{juft}")
print(f"juft sonlar kvadrati{kvdrat}")
