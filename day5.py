
# python training 
# code of advent 2024 - day 4

# Importing the re module
import re

#file = open("input_day5.txt", "r")
file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")

sum = 0

ruleSection = True
rule_lines = []
update_lines = []

for line in lines: 
       
    if(line == "\n"):
        ruleSection = False
        continue

    if(ruleSection):
        rule_lines.append(line)
    else:
        update_lines.append(line)

#print(rule_lines)
#print(update_lines)

rules = []
for line in rule_lines: 
    
    pattern = r"(\d+)\|(\d+)"
    matches = re.findall(pattern, line)

    for match in matches:
        rules.append((match[0],match[1]))



def getMiddleNumber(array):

    pos = len(array) // 2
        
    return array[pos]

def getDependencies(num):

    dependencies = []

    for rule in rules:
        if(rule[1] == num):
            dependencies.append(rule[0])

    return dependencies

def isLeftSideRule(num):

    for rule in rules:
        if(rule[0] == num):
            return True

    return False

def checkOrder(input):

    checkList = input.copy()
    
    while(len(checkList)>0):
        next = checkList.pop(0)

        deps = getDependencies(next)
        
        for element in deps:
            if element in checkList:
                return False
    
    return True

def sort(input):

    checkList = input.copy()
    
    checkPos = 0
    while(checkPos < len(checkList)):
    
        resort = False
        checkItem = checkList[checkPos]
        deps = getDependencies(checkItem)
        
        for comparePos in range(len(checkList)-1, checkPos, -1):

            compareItem = checkList[comparePos]
            
            if(compareItem in deps):
                checkList.insert(comparePos+1, checkItem)
                del checkList[checkPos]
                resort = True
                break

        if(resort == False):
            checkPos += 1

    return checkList


for line in update_lines: 
    
    update = []

    pattern = r"(\d+)\,"
    matches = re.findall(pattern, line)

    for match in matches:
        update.append(match)

    pattern = r"(\d+)[\n](?!\,)"
    matches = re.findall(pattern, line)

    for match in matches:
        update.append(match)

    if (checkOrder(update) == False):
        
        newUpdate = sort(update)
        print("New sorted list: ", newUpdate)

        middle = getMiddleNumber(newUpdate)
        sum += int(middle)

print(f"Sum={sum}")