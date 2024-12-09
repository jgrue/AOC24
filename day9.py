# python training 
# code of advent 2024 - day 9

# Importing the re module
import re

#file = open("input_day9.txt", "r")
file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")


values = []

id = 0
empty = False

for line in lines: 
    for char in line:

        #print(char)
        amount = int(char)
        
        for a in range(amount):
            if(empty == False):
                values.append(id)        
            else:
                values.append(-1)            
        
        if(empty == False):
            empty = True
        else:
            empty = False
            id += 1

sum = 0

def hasGaps(text):
    
    lastChar = False
    foundGap = False

    for pos in range(len(values)-1,-1,-1):
        
        if(values[pos] != -1):
            lastChar = True
            
        if(lastChar == True and values[pos] == -1):
            foundGap = True
            break

    return foundGap

def replace_at_position(original_string, new_substring, position):
     # Ensure the position is within the range of the original string 
     if position < 0 or position >= len(original_string): 
        raise ValueError("Position out of range") 
     
     # Create the new string 
     new_string = original_string[:position] + new_substring + original_string[position + len(new_substring):] 
     return new_string


def find_last_value_position(array):

    for pos in range(len(array)-1,-1,-1):        
        if(array[pos] != -1):
            return pos
    return -1

def find_first_empty_position(array):
    for i in range(len(array) - 1):
        if (array[i] == -1):
            return i 
    return -1

while(hasGaps(values)):

    lastPos = find_last_value_position(values)
    firstFreepos = find_first_empty_position(values)

    values[firstFreepos], values[lastPos] = values[lastPos], values[firstFreepos]
    
    #print(valueLine)
    

print(values)
#print("Result: ", valueLine)

for x in range(len(values)-1):    
    if(values[x] != -1 ):      

        value = values[x]
        sum += x*value

print(f"Sum={sum}")
