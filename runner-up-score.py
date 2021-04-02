#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=list(arr);
    a.sort(reverse=True);
    Max= max(a);
    for i in a:
        if(i<Max):
            print(i)
            break
