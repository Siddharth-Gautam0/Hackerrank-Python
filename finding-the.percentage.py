#Finding the percentage

if __name__ == '__main__':
    x = 0
    y = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks[query_name]:
        x+=i
        y = y+1
    x = x/y 
    print("%.2f" % x)
