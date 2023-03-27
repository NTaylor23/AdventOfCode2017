with open('inputs/day13.txt', 'r') as file:
    layers = file.readlines()
    firewall = {int(layer.split(': ')[0]): int(layer.split(': ')[1]) for layer in layers}

"""
    Notice that you only need to check the delays that would allow you to pass through each layer individually.
    For each layer, calculate the earliest delay that would allow you to pass through that layer without 
    getting caught.
    Find the smallest delay value that satisfies the conditions for all layers. 
    This can be done using the Chinese Remainder Theorem (CRT).
"""

earliest_delays = {n: 0 for n in firewall.keys()}
for layer, depth in firewall.items():
    delay = 0
    while True:
        if depth > 0 and (layer + delay) % ((depth - 1) * 2) != 0:
            break
        delay += 1
    earliest_delays[layer] = delay

####### MUST BE OPTIMIZED, THIS IS WAY TOO SLOW #######

def caught(firewall: dict, delay: int) -> bool:
    for layer, depth in firewall.items():
        if depth > 0 and (layer + delay) % ((depth - 1) << 1) == 0:
            return True
    return False

delay = 0
while True:
    if not caught(firewall, delay):
        break
    delay += 1

