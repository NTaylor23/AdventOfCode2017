from collections import defaultdict, deque

class Program:
    def __init__(self, weight: int, neighbors: list) -> None:
        self.weight = weight
        self.neighbors = []

adj_list, visited = defaultdict(), set()

with open('inputs/day07.txt', 'r') as file:
    for obj in file.readlines():
        sp = obj.split('->')
        name, weight = sp[0].split()
        adj_list[name] = Program(int(weight[1:-1]), [])
        if len(sp) > 1:
            for neighbor in [neighbor.strip() for neighbor in sp[1].split(',')]:
                adj_list[name].neighbors.append(neighbor)

def dfs(connected_vertices: list) -> int:
    sum = 0
    while connected_vertices:
        curr = connected_vertices.pop()
        visited.add(curr)
        sum += adj_list[curr].weight
        for neighbor in adj_list[curr].neighbors:
            if neighbor not in visited:
                connected_vertices.append(neighbor)
    return sum
        
max_weight = 0
for name in adj_list.keys():
    if len(adj_list[name].neighbors) > 0:
        adj_list[name].weight += dfs(adj_list[name].neighbors.copy())
    if adj_list[name].weight > max_weight:
        root_node = name
        max_weight = adj_list[name].weight

weights = {}
for adjacent_node in adj_list[root_node].neighbors:
    weights.setdefault(adj_list[adjacent_node].weight, []).append(adjacent_node)

for k, v in weights.items():
    if len(v) == 1:
        problem_node = v[0]
        queue = deque([problem_node])
        while queue:
            curr = queue.popleft()
            if len(adj_list[curr].neighbors) > 0:
                print(f'{curr} -> {adj_list[curr].weight}: ')
                print(' '.join([str((n, adj_list[n].weight)) for n in adj_list[curr].neighbors]))
                #print(set([adj_list[n].weight for n in adj_list[curr].neighbors]))
                print()
                for neighbor in adj_list[curr].neighbors:
                    queue.append(neighbor)

