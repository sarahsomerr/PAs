# PROGRAMMING ASSIGNMENT 1


import random
from tabulate import tabulate
import time

data = []


def dim_1(m):    
    x = 0
    counter = 0
    for n in range(m):
        direction = random.choice([-1,1])
        x += direction
        if x == 0:
            return 1
            
    return 0
  

move_values = [20,200,2000,20000,200000,2000000]

for moves in move_values:
    final_count1 = 0
    for i in range(100):
            final_count1 += dim_1(moves)
    data.append([moves,final_count1])
    
print("Percentages of Time Particle Returned to the Origin: ")

def dim_2(m):   
    x = 0
    y = 0
    counter = 0
    for n in range(m):
        direction_x = random.choice([-1,1])
        direction_y = random.choice([-1,1])
        x += direction_x
        y += direction_y
        if (x == 0) and (y == 0):
            return 1
            
    return 0

move_values = [20,200,2000,20000,200000,2000000]
for moves in move_values:
    final_count2 = 0
    for i in range(100):
            final_count2 += dim_2(moves)
    data.append([moves,final_count2])


start_time = time.time()

def dim_3(m):       
    x = 0
    y = 0
    z = 0
    counter = 0
    for n in range(m):
        direction_x = random.choice([-1,1])
        direction_y = random.choice([-1,1])
        direction_z = random.choice([-1,1])
        x += direction_x
        y += direction_y
        z += direction_z
        if (x == 0) and (y == 0) and (z == 0):
            return 1
            
    return 0
  
move_values = [20,200,2000,20000,200000,2000000]

for moves in move_values:
    final_count = 0
    for i in range(100):
            final_count += dim_3(moves)
    data.append([moves,final_count])

end_time = time.time()

elapsed_time3 = end_time - start_time   

def main():
    headers = ["moves", "Dimension"]
    table = tabulate(data, headers, tablefmt="grid")
    
    print(table)
    print()
    print("Run Time (in seconds): ")
    print(f' D3: {elapsed_time3} seconds')
    return main

