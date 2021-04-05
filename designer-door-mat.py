n,m = map(int, input().split())
s1 = ".|."
s2 = "WELCOME"
for i in range(n//2):
    print((s1*((2*i)+1)).center(m,'-'))
print((s2).center(m,'-'))
i = n//2 -1
while i> -1:
    print((s1*((2*i)+1)).center(m,'-'))
    i+=-1
