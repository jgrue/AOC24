
# python training 
# code of advent 2024 - day 4

# Importing the re module
import re

file = open("input_day4.txt", "r")
#file = open("temp.txt", "r")
lines_input = file.readlines()

print(" \n")

sum = 0

def search(startX,startY,vectorX,vectorY,maxX,maxY,searchString):

    nextLetter = searchString[0]
      
    nextX = startX + vectorX
    nextY = startY + vectorY

    if(nextX < 0 or nextY < 0 or nextX > maxX or nextY > maxY):
        return False  
       
    checkLetter = lines[nextX][nextY]

    if(checkLetter != nextLetter):
        return False

    newString = searchString[1:]

    if(len(newString)>0):    
        return search(nextX, nextY, vectorX, vectorY, maxX, maxY,newString)
    
    return True


def searchX(startR,startC,maxGridX,maxGridY):

    minX = startR - 1
    maxX = startR + 1
    minY = startC - 1
    maxY = startC + 1
      
    if(minX < 0 or minY < 0 or maxX > maxGridX or maxY > maxGridY):
        return False  

    leftUpper = lines[startR-1][startC-1]   
    rightUpper = lines[startR-1][startC+1]   
    leftLower = lines[startR+1][startC-1]   
    rightLower = lines[startR+1][startC+1]   

    if(leftUpper == "M" and rightLower == "S" and rightUpper == "S" and leftLower == "M"):
        return True
       
    if(leftUpper == "S" and rightLower == "M" and rightUpper == "M" and leftLower == "S"):
        return True
    
    if(leftUpper == "S" and rightLower == "M" and rightUpper == "S" and leftLower == "M"):
        return True
    
    if(leftUpper == "M" and rightLower == "S" and rightUpper == "M" and leftLower == "S"):
        return True
    
    return False

lines = []
for line in lines_input:
    line = line.strip()
    lines.append(line)


for r in range(len(lines)):      
    print(f"Line {r}")

    for c in range(len(lines[r])):
        
        if(lines[r][c] == "A"):     

            if(searchX(r,c,len(lines[0])-1,len(lines)-1)):
                sum += 1

    print(f"Line {r} Sum={sum}")


print(f"Sum={sum}")