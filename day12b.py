from collections import defaultdict

adj_map = defaultdict()
with open('inputs/day12.txt', 'r') as file:
    for path in file.readlines():
        sp = path.split(' <-> ')
        start, dest = int(sp[0]), [int(n) for n in sp[1].split(', ')]
        adj_map[start] = dest

def dfs(visited: set, curr: int, graph: defaultdict):
    visited.add(curr)
    for neighbour in adj_map[curr]:
        if neighbour not in visited:
            dfs(visited, neighbour, graph)

def find_connected_components():
    visited = set()
    count = 0
    for program in adj_map.keys():
        if program not in visited:
            dfs(visited, program, adj_map)
            count += 1
    return count

result = find_connected_components()
print(f"Day 12 Part 2: There are {result} groups of programs.\n")
