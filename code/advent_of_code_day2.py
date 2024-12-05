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
    for i in range(0, len(lst) - 1):
        v1 = int(lst[i])
        v2 = int(lst[i + 1])

        if i == v3:
            continue
        if  (0 < v2 - v1 <= 3):
            continue
        else:
            return 0
    return 1

def get_dec(lst):
  
    for i in range(0, len(lst) - 1):
        v1 = int(lst[i])
        v2 = int(lst[i + 1])
        
        if  0 < v1 - v2 <= 3:
            continue
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


    

        
    
