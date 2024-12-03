
# python training 
# code of advent 2024 - day 2

# Importing the re module
import re

file = open("input_day2.txt", "r")
#file = open("temp.txt", "r")
lines = file.readlines()

print(" \n")

def check_safe(numbers):
    
    nums_int = numbers.copy()
    start = nums_int.pop(0)
    previous = start

    direction = 0
    firstCheck = True
    
    for num in nums_int:

        delta = num - previous

        if(firstCheck == True):
            direction = delta
            firstCheck = False

        if((delta < 0 and direction > 0) or (delta > 0 and direction < 0)):
            return False
        
        if(abs(delta) > 3):
            return False
            
        if(delta == 0): 
            return False

        previous = num 
        
    return True  


sum = 0

for line in lines:      
    
    print(f"Processing: ", line)
    
    matches = re.findall(r'\d+', line)

    numbers = []
    for m in matches:
        numbers.append(int(m))
    print("found numbers:", numbers)

    check = check_safe(numbers)   

    if(not(check)):
        for n in range(len(numbers)):
            new_numbers = numbers.copy()
            new_numbers.pop(n)

            check2 = check_safe(new_numbers)
            if(check2):
                check = True
                break
            
    if(check):
        sum += 1

print(f"Sum={sum}")