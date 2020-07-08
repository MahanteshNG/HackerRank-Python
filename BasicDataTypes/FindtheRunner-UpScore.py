if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    maximum=max(arr)
    arr.remove(maximum)
    maximum=max(arr)
    print(maximum)
