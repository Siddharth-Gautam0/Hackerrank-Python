#Lists
if __name__ == '__main__':
    list1 = []
    N = int(input())
    for i in range(N):
        x = input()
        x = x.split()
        if x[0]== "print":
            print(list1)
        if x[0]=="insert":
            list1.insert(int(x[1]),int(x[2]))    
        if x[0]=="append":
            list1.append(int(x[1]))  
        if x[0]=="pop":
            list1.pop()
        if x[0]=="reverse":
            list1.reverse()
        if x[0]=="sort":
            list1.sort()
        if x[0]=="remove":
            list1.remove(int(x[1]))   
                 
