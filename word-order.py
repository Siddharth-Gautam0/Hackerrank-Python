list1 = []
N = input()
for i in range(int(N)):
    list1.append(input())

from collections import Counter

X = Counter(list1)
print(len(X))
y = list(X.values())
for i in y:
    print(i, end = " ")
