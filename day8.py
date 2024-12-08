# python training 
# code of advent 2024 - day 8

# Importing the re module
import re

file = open("input_day8.txt", "r")
#file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")

sum = 0

antennas = {}

maxCols = len(lines[0])-1
maxRows = len(lines)

for row in range(maxRows):
    for col in range(maxCols):
    
        if(lines[row][col] !="."):

            value = lines[row][col]
            if(value not in antennas):
                antennas[value] = []

            positions = antennas[value]
            positions.append((row,col))  

#print(antennas)  

def computeNode(a,b):

    aR = a[0]
    aC = a[1]
    bR = b[0]
    bC = b[1]

    newC = aC - (bC - aC)
    newR = aR - (bR - aR)

    return (newR, newC)



def computeNodes(positions, nodes):

    if(len(positions)<=1):
        return
    
    posCopy = positions.copy()
    a = posCopy.pop(0)
    
    for x in range(len(posCopy)):
        b = posCopy[x]

        nodes.append(computeNode(a,b))
        nodes.append(computeNode(b,a))

    computeNodes(posCopy, nodes)

    return

def isInside(pos):
    
    posR = pos[0]
    posC = pos[1]
    
    if(posR < 0 or posC < 0 ):
        #print(f"outside.",end="")
        return False
    if(posR > maxRows-1 or posC > maxCols):
        #print(f"outside.",end="")
        return False
    
    return True


def isFreePos(pos):
    
    posR = pos[0]
    posC = pos[1]

    target = lines[posR][posC] 
    if(target == "."):
        return True    
    #else:
        #print(f"occupied ({target}).",end="")
    
        
    
    return False

nodes = []
for key in antennas:
    
    antenna = antennas[key]
       
    computeNodes(antenna, nodes)
    
    #print(antenna)
    

print(nodes)

# remove duplicates    
nodes = list(set(nodes))
#print(nodes)

for node in nodes:               
    
    #print(f"Evaluating {node}:",end="")
    #if(isInside(node) and isFreePos(node)):
    if(isInside(node)):
        sum += 1 
        #print(f"valid (Sum={sum})",end="")

    #print(f"\n")

print(f"Sum={sum}")
