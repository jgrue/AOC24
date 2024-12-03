
# python training 
# code of advent 2024 - day 3

# Importing the re module
import re

file = open("input_day3.txt", "r")
#file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")

sum = 0

def compute(input):
    
    print("Computing: ", input)
    sum = 0
    
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"
    matches = re.findall(pattern, input)
    #print(matches)

    for match in matches: 
        res = int(match[0])*int(match[1])
        #print(res)
        sum += res

    return sum

for line in lines:      
    
    #print(f"Processing: ", line) 
    
    print(line)

    #extract all "do" groups
    pattern = r"do\(\)(.*?)(?=(don\'t\(\)|do\(\)|\n))"
    #pattern = r"do\(\)(.*?)(?=(don\'t\(\)|\n))"
    matches = re.findall(pattern, line)
    
    for m in matches: 
         sum += compute(m[0])

    
    # leading 
    pattern = r"(.*?)(?=(don\'t\(\)|do\(\)))"
    leading = re.findall(pattern, line)
    
    sum += compute(leading[0][0])
  
    

print(f"Sum={sum}")