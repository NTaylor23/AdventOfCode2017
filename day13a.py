with open('inputs/day13.txt', 'r') as file:
    layers = file.readlines()
    firewall = {int(layer.split(': ')[0]): int(layer.split(': ')[1]) for layer in layers}

severity = 0 

for layer, depth in firewall.items():
    if depth > 1 and layer % ((depth - 1) << 1) == 0:
        # It's not necessary to calculate the actual position of the scanner in the current layer!
        # Just double the `depth` of the layer and check if that's evenly divisible by the packet's current position.
        severity += depth * layer

result = severity
print(f"Day 13 Part 1: The severity of my whole trip is {result}.\n")