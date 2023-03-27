from collections import defaultdict

adj_map = defaultdict()
with open('inputs/day12.txt', 'r') as file:
    for path in file.readlines():
        sp = path.split(' <-> ')
        start, dest = int(sp[0]), [int(n) for n in sp[1].split(', ')]
        adj_map[start] = dest

visited = set()
stack   = [0]

# dfs
while stack:
    curr: int = stack.pop()
    visited.add(curr)
    for neighbor in adj_map[curr]:
        if neighbor not in visited:
            stack.append(neighbor)

result = len(visited)
print(f"Day 12 Part 1: There are {result} programs reachable from program #0.\n")