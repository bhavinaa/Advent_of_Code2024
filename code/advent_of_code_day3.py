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


# FOR THE complicated pattern matching 
#https://docs.python.org/3/howto/regex.html#regex-howto

# question 2
"""
we are using regex as we want to do string matching
the string matches, are vey complicated as
1. input string has a complex and irregular structure
2. need to extract or process specific parts of the string based on the rules

we want to filter out the disables sections (the parts we do not want)
then we want to process the remaning enabled sections

Explanation of Each Part:
don't\(\):

    Matches the literal text don't().
    ': Matches a single quote.
    \\(: Escapes the opening parenthesis ( so it is treated literally.
    \\): Escapes the closing parenthesis ) so it is treated literally.


    (?s:.*?):

    (?s:...):
    Enables dot-all mode inside the parentheses, allowing the dot (.)
    to match any character, including newlines.
    Without this, . matches everything except newline characters.
    Example:
    With (?s), . matches a, \n, b in the string a\nb.
    Without (?s), . matches a only.


    Matches any sequence of characters (dot . matches any character,
    * allows repetition).
    The ? after * makes it non-greedy,
    meaning it matches the shortest possible sequence that
    satisfies the rest of the pattern.
    Why Non-Greedy?
    A greedy match (.*) would consume as much as possible,
    potentially going past the next do() or to the end of the string.
    The non-greedy version (.*?) stops at the first occurrence of do() or
    the end of the string.


    ?:do\(\)|$):

    (?:...):
    Creates a non-capturing group, meaning it
    groups the expressions inside without creating a
    capturing group (doesn't store a match for use later).
    Useful for grouping parts of the regex without needing
    the overhead of capturing matches.
    do\(\):
    Matches the literal text do(), like don't() earlier.
    |:
    Acts as an OR operator, meaning "match either do() or..."
    $:
    Matches the end of the string.


    Why Use re.compile?
    Efficiency: Compiling a regex pattern into a Pattern object
    is more efficient when you need to use the pattern
    multiple times. It avoids recompiling the regex each time
    you use it.
    Readability: It makes the code clearer by separating the
    definition of the regex from the operations you perform with it.

    The Two re.compile Calls:
    1. disabled_pattern = re.compile(r"don't\(\)(?s:.*?)(?:do\(\)|$)")
    Purpose:
    This pattern identifies sections of the memory that should be ignored (disabled)
    because they are between don't() and do() (or until the end of the string).
    It is used to remove these sections from the input.
    2. mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    Purpose:
    This pattern matches and captures enabled multiplication
    instructions (mul(a, b)) from the remaining input.
    It is used to extract numbers a and b for multiplication.
    Why Are They Separate?
    Different Roles:

    disabled_pattern is for filtering out unwanted content.
    mul_pattern is for finding the valid instructions.
    Since these patterns serve different purposes, they are compiled separately.
    Reusability:

    Each pattern can be reused independently multiple times (e.g.,
    in loops or with different input strings).
    Compiling them once and reusing them is faster than compiling them every time.
    Clarity:

    Separating the patterns improves readability. Each pattern
    represents a distinct concept, making the code easier to understand.


    this is all parts of processing the data twice 


"""


import re

def calculate_sum_optimized(corrupted_memory):
    # Regex to find all blocks disabled by don't()
    #until the next do() or the end of the string
    disabled_pattern = re.compile(r"don't\(\)(?s:.*?)(?:do\(\)|$)")
    # Regex to find mul(a, b) instructions
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    
    # Remove all disabled blocks
    enabled_memory = re.sub(disabled_pattern, "", corrupted_memory)
    
    # Find all enabled mul instructions
    #and calculate the sum
    total = 0
    for match in mul_pattern.finditer(enabled_memory):
        a, b = map(int, match.groups())
        total += a * b
    
    return total

result = calculate_sum_optimized(rows)
print("Sum of enabled multiplications:", result)

