## DAY 1 - Puzzle 1 

f = open("C:\\python 2024\\advent_of_code\\inputs\\day1.txt", "r")


column1 = []
column2 = []
ans_column = []
answer = 0
answer2 = 0

with open("C:\\python 2024\\advent_of_code\\inputs\\day1.txt", "r") as file:
    for line in file:

        columns = line.strip().split()
        if len(columns) >= 2:
            column1.append(columns[0])
            column2.append(columns[1])


# quick sort in ascending

def quickSort(lst, low, high):
    # only sort when it is a valid index
    # with quicksort each iteration, one item is places in the correct place
    # recursively do the rest to each side
    if low < high:
        pi = partition(lst, low, high)
        quickSort(lst, low, pi - 1)
        quickSort(lst, pi + 1, high)

def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i = i + 1
            (lst[i], lst[j]) = (lst[j], lst[i])
    (lst[i+1], lst[high]) = (lst[high], lst[i + 1])

    return i + 1

# compare list  and add

# done inplace
quickSort(column1, 0, len(column1) - 1)
quickSort(column2, 0, len(column2) - 1)

for i in range(0, len(column1)):
    v = int(column1[i]) - int(column2[i])
    if v >= 0:
        answer = answer + v
    else:
        answer = answer - v
   
        


print("answer: " + str(answer))

## Day 2 Puzzle 2


# for each lst 1, check if it is in lst 2 + count the number of items in the lst
# multiply each item in lst 1 by the count it is present in lst 2

# you can store lst2 in a hashmap first
count_map_c2 = {}


for item in column2:
    print(item)
    if item in count_map_c2:
        count_map_c2[item] += 1
    else:
        count_map_c2[item] = 1

for i in range(0,len(column1)):
    if column1[i] in count_map_c2:
        answer2 = answer2 + int(column1[i]) * count_map_c2[column1[i]]


print("answer2: " + str(answer2))









