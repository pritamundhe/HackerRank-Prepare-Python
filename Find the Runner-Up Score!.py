if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    p1=set(arr)
    p2=sorted(p1)
    print(p2[-2])
