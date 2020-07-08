import math
def is_leap(y):
    leap = False
    if 1900<=y<=math.pow(10,5):
        if y%4==0:
            if y%100!=0:
                leap = True
            elif y%400==0: 
                leap = True
    return leap

