if __name__ == '__main__':
    N = int(input())
    t=[]
    for i in range (0,N):
        list=[]
        list=input().split()
        if list[0]=="insert":
            t.insert(int(list[1]),int(list[2]))
        elif list[0]=="print":
            print(t)
        elif list[0]=="remove":
            t.remove(int(list[1]))
        elif list[0]=="append":
            t.append(int(list[1]))
        elif list[0]=="sort":
            t.sort()
        elif list[0]=="pop":
            t.pop()
        elif list[0]=="reverse":
            t.reverse()

