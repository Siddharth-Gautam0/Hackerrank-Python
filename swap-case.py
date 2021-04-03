#sWAP cASE

def swap_case(s):
    out = ""
    for i in s:
        if i.islower():
            out+= i.upper()
        elif i.isupper():
            out+= i.lower()
        else:
            out+= i        
    return out

if __name__ == '__main__':
