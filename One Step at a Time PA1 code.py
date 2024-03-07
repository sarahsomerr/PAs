# PA 1      ONE STEP AT A TIME

import random 
import time

moves = [20,200,2000,20000,200000,2000000]

    
def dimension_one(moves):
    x = 0
    counter = 0
    for n in range(moves):
        direction = random.choice(["left","right"])
        if direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
        if x == 0:
            counter += 1
            break
        return counter
        
    for moves in move_values:
        final_count = 0
        for i in range(100):
            final_count += dimension_one(moves)