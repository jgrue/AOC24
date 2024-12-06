
# python training 
# code of advent 2024 - day 6

# Importing the re module
import re

file = open("input_day6.txt", "r")
#file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")

sum = 0

minR = 0
minC = 0
maxR = len(lines)-1
maxC = len(lines[0].strip())-1

dirR = -1
dirC = 0

posR = 0
for row in range(len(lines)): 
    
    pos = lines[row].find("^")
    if(pos > 0):
        posR = row
        break

posC = pos

print(f"Starting point r={posR} c={posC}")   
print(f"bounds {minR}/{minC}/{maxR}/{maxC}")




def isInside(r, c):
    if(r < minR or r > maxR or c < minC or c > maxC):
        return False
    else:
        return True   

def replace_at_position(original_string, new_substring, position):
     # Ensure the position is within the range of the original string 
     if position < 0 or position >= len(original_string): 
        raise ValueError("Position out of range") 
     
     # Create the new string 
     new_string = original_string[:position] + new_substring + original_string[position + len(new_substring):] 
     return new_string

def checkLoop(lines, dirR, dirC, posR, posC):

    isLoop = False
    path = []

    while(isInside(posR,posC)):
        pos = (posR,posC,dirR,dirC)
        if(pos in path):
            isLoop = True
            break
        else:
            path.append(pos)
                
        lines[posR] = replace_at_position(lines[posR],"X",posC)
    

    #for line in lines:
    #    print(line.strip())

    #print("")

        nextPosR = posR + dirR
        nextPosC = posC + dirC

        if(not(isInside(nextPosR,nextPosC))):
            break

        if(lines[nextPosR][nextPosC] == "#" or lines[nextPosR][nextPosC] == "O"):
            if(dirR == -1 and dirC == 0):
                dirR = 0
                dirC = 1
            elif(dirR == 0 and dirC == 1):
                dirR = 1
                dirC = 0
            elif(dirR == 1 and dirC == 0):
                dirR = 0
                dirC = -1
            elif(dirR == 0 and dirC == -1):
                dirR = -1
                dirC = 0

            nextPosR = posR + dirR        
            nextPosC = posC + dirC

            if(not(isInside(nextPosR,nextPosC))):
                break   

        posR = nextPosR
        posC = nextPosC
    
    return isLoop


count = 0
overall = len(lines) * len(lines[row])

for row in range(len(lines)):
    for col in range(len(lines[row])):

        count += 1

        print(f"{count}/{overall}")

        checkArray = []
        for line in lines:
            checkArray.append(line)

        if(checkArray[row][col] == "."):

            checkArray[row] = replace_at_position(checkArray[row],"O",col)

           
            isLoop = checkLoop(checkArray, dirR, dirC, posR, posC)            

            #for checkline in checkArray:
            #    print(checkline.strip())
            #print("")

            if(isLoop):
                sum += 1

for line in lines:
    print(line.strip())

print(f"Sum={sum}")