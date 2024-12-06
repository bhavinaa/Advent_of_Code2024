# you have to read the data line by line
# you have to read it line by line and then you have to read the input ch

import re
# package to help with pattern matching

rows = ""
with open("C:\\python 2024\\advent_of_code\\inputs\\day3.txt", "r") as file:
    rows = "".join(file)



def parse_text(rows):
    total_sum = 0 
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern,rows)
    
    for line in matches:
        #print(line)
        line = list(line)
        x,y = map(int, line)
        total_sum += x * y 
        

    return total_sum




v = parse_text(rows)

print("the result: " + str(v))
