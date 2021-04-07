n,m = map(int, input().split())
X = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int,input().split()))

Hap = 0
for i in X:
    if i in A:
        Hap += 1
    if i in B:
        Hap += -1    
        
print(Hap) 
