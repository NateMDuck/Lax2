import streamlit as st


import os
import random
import time

list_statistics = []

list_moves =[' shift', ' double shift', ' triple shift',
            ' roll dodge', ' question mark dodge',
            ' face dodge', ' split dodge', ' bull dodge']

list_shots = [' high', ' side', ' low']

list_goal = [' upper ninety', ' lower ninety', ' nutmeg']

list_side = [' right', ' left']

num_rounds = 5

for i in range(num_rounds):

    move = random.choice(list_side)

    if move != "nutmeg":
        move = move + " " + random.choice(list_moves)

    list_statistics.append(move)

    os.system(f'say{move}')

    time.sleep(1.0)


    shot = random.choice(list_side) + " " + random.choice(list_shots)
    shot = shot + " " + random.choice(list_goal) + " " + random.choice(list_side)

    list_statistics.append(shot)

    os.system(f'say{shot}')


    time.sleep(1.0)



chunk_size = 2

# Example 1 : Using list slicing
def chunkify(list_statistics, chunk_size):
    return [list_statistics[i:i+chunk_size] for i in range(0, len(list_statistics), chunk_size)]

result = chunkify(list_statistics, chunk_size)
print(result)




