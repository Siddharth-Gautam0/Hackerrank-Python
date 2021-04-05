import textwrap

def wrap(string, max_width):
    i = 0
    while i<len(string):
        i += max_width
        string = string[:i]+"\n"+string[i:]
        i+=1
        
    return string
