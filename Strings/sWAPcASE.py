def swap_case(s):
    ss=''
    for a in s:
        if a.islower():
            a=a.upper()
            ss=ss+a
        elif a.isupper():
            a=a.lower()
            ss=ss+a
        else:
            ss=ss+a
    return ss



if __name__ == '__main__':
