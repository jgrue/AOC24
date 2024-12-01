
# python training 
# code of advent 2024 - day 1

# Importing the re module
import re

file = open("input_day1.txt", "r")
#file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")

sum = 0

c1 = []
c2 = []

for line in lines:       
    
    #print(line)

    matches = re.findall(r'\d+', line)
    num1 = matches[0]
    num2 = matches[1]
      
    #print("found numbers: [" + num1 + "], [" + num2 + "]\n")

    c1.append(int(num1))
    c2.append(int(num2))

#c1.sort()
#c2.sort()

for index in range(len(c1)):
    abs_delta = abs(c2[index] - c1[index])
    #print(f"numbers: [{c2[index]}], [{c1[index]}] - delta: {abs_delta}\n")
    #sum += abs_delta

def compute_result(search):
    result = 0 

    hits = c2.count(search)
    print(f"input={search} - hits={hits}")


    return search*hits

for num in c1:
    res = compute_result(num)
    sum += res



#print(c1)
#print(c2)



print('Similarity=', sum)