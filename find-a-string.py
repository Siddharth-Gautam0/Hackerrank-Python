def count_substring(string, sub_string):
    x = len(sub_string)
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string[i:i+x] == sub_string:
                count+=1
            else:
                pass    
            
    return count
