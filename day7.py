# python training 
# code of advent 2024 - day 7

# Importing the re module
import re

file = open("input_day7.txt", "r")
#file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")

sum = 0

def checkEquasion(result, operands):

    ops = operands.copy()
    first = ops.pop(0)

    if(computeTerm(result, first, ops)):
        return True

    return False

def computeTerm(targetResult, currentResult, operands):

    if(len(operands) == 0):
        if(targetResult == currentResult):
            return True
        else:
            return False
        
    ops = operands.copy()    
    nextValue = ops.pop(0)
    
    # addition
    newResult = currentResult + nextValue
    if(computeTerm(targetResult, newResult, ops )):
        return True
    
    # subtraction
    #newResult = currentResult - nextValue
    #if(computeTerm(targetResult, newResult, ops )):
    #    return True
    
    # multiply
    newResult = currentResult * nextValue
    if(computeTerm(targetResult, newResult, ops )):
        return True
    
    # division
    #newResult = currentResult / nextValue
    #if(computeTerm(targetResult, newResult, ops )):
    #    return True

    return False


operations = []
for line in lines:
    splits = line.split(":")

    result = int(splits[0])
    numbers = splits[1].split()

    operands = []
    for op in range(len(numbers)):
        operands.append(int(numbers[op]))

    #print(f"Result: {result}")
    #print(f"Operands: {operands}")

    if(checkEquasion(result,operands)):
        sum += result        

print(f"Sum={sum}")