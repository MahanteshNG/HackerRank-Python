s=[]
for studentsnumber in range(int(input())):
    s.append([input(),float(input())])
minimum=s[0][1]
for each in s:
    if minimum>=each[1]:
        minimum=each[1]
s[:]=[each for each in s if each[1]!=minimum]
sl=[]
minimum=s[0][1]
for each in s:
    if minimum>each[1]:
        minimum=each[1]
for each in s:
    if each[1]==minimum:
        sl.append(each[0])
sl.sort()
for i in range(len(sl)):
    if i+1==len(sl):
        print(sl[i])
    else:
        print(sl[i],end='\n')
