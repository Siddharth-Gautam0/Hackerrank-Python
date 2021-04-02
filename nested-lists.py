#Nested Lists
if __name__ == '__main__':
    dict1 = {}
    sortedsc = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dict1:
            dict1[score].append(name)
        else:
            dict1[score]=[name]    
        if score not in sortedsc:
            sortedsc.append(score)

sortedsc.sort()
dict1[sortedsc[1]].sort()

for i in dict1[sortedsc[1]]:
    print(i)
