## read the file (all lines are of different lengths

# determine if the line is increasing or decreasing
# count if the line is safe or not



"""
errors i made:
the order of the modulus matters, it affects what divides what
in this case modulus as the condition wont work as you want an absolute diff

eg 10 % 3 == 1 (which would pass with the mod condition) but it is wrong
"""


rows = []
with open("C:\\python 2024\\advent_of_code\\inputs\\day2.txt", "r") as file:
    for line in file:

        columns = line.strip().split()
        rows.append(columns)

rows2 = rows


def check_gradient(lst):
    if len(lst) >= 2:
        v1 = int(lst[0])
        v2 = int(lst[1])
        if v1 > v2:
            return "decr"
        if v2 > v1:
            return "incr"
        if v1 == v2:
            return "unsafe"
    return "safe"


def get_inc(lst):
    badc = 0
    v3 = None
    for i in range(0, len(lst) - 1):
        v1 = int(lst[i])
        v2 = int(lst[i + 1])

        if i == v3:
            continue
        
        if  (0 < v2 - v1 <= 3):
            continue
        if v1 >= v2:
            if badc < 1:
                v3 = i + 1
                if (0 < int(lst[v3]) - v1 <=3):
                    badc = 1
                    continue
            return 0
        else:
            return 0
    return 1

def get_dec(lst):
    badc = 0 
    v3 = None
    for i in range(0, len(lst) - 1):
        v1 = int(lst[i])
        v2 = int(lst[i + 1])
        
        if  0 < v1 - v2 <= 3:
            continue
        if v2 >= v1:
            if badc < 1:
                v3 = i + 1
                if (0 < v1 - int(lst[v3])  <=3):
                    badc = 1
                    continue
                else:
                    return 0
        else:
             return 0
    return 1


def check_reports(lsts, value):
    for i in lsts:
        #print(i)
        v = check_gradient(i)
        if v == "decr":
            value += get_dec(i)
        if v == "incr":
            value += get_inc(i)

    return value


count_safe = check_reports(rows, 0)
print("count safe: " + str(count_safe))
            


## part 2

count_safe2 = 0

# the initial way of checking would not work
# test case, the error might be found in position no 2.
# you do part 1
# if it is safe, yay good for u
# if it is not safe, remove everyone 1 (One at a time) then check if it is safe


"""
i was failing some test cases, it was the very specific to when what happens if you fail with the first
two elements
"""

def check_error_reports(rows,count_safe2):
    temp = 0
    for i in rows:
        grad =  check_gradient(i)
        temp_c = 0
        s = 0 
        if grad == "decr":
            temp_c = get_dec(i)
            if temp_c == 0:
                s = check_all(i)
                count_safe2 += s
                continue
            count_safe2 += temp_c
            continue

        if grad == "incr":
            temp_c = get_inc(i)
            if temp_c == 0:
                s = check_all(i)
                count_safe2 += s
                continue

            count_safe2 += temp_c
            continue


        s = check_all(i)
        count_safe2 += s
        
    return count_safe2

def check_all(row):
    length = len(row)
    curr_safe = False
    
    for i in range(0,length):
        if not(curr_safe):
            value = 0
            make_copy = row[0:i] + row[i+1:length]
            v = check_gradient(make_copy)
            if v == "decr":
                value += get_dec(make_copy)
            if v == "incr":
                value += get_inc(make_copy)

            if value == 1:
                curr_safe = True
                return 1
            continue
    return 0
            
  
                    

count_safe2 = check_error_reports(rows2, 0)
print("count safe2:  " + str(count_safe2))


    

        
    
