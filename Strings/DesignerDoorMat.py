N,M=map(int,input().split(" "))
s=".|."
for i in range(1,N-1,2):
    print((s*i).center(M,"-") )
print("WELCOME".center(M,"-"))
for i in range(N-2,0,-2):
    print((s*i).center(M,"-"))
