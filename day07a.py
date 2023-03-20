from collections import defaultdict

adj_list = defaultdict()

with open('inputs/day07.txt', 'r') as file:
    for obj in file.readlines():
        sp = obj.split('->')
        name = sp[0].split()[0]
        
        if len(sp) > 1:
            if name not in adj_list:
                adj_list[name] = []
            for edge in [edge_name.strip() for edge_name in sp[1].split(',')]:
                if edge not in adj_list:
                    adj_list[edge] = []
                adj_list[name].append(edge)                
        else:
            adj_list[name] = []

def dfs(neighbors: list) -> int:
    """Search each program's edges such that all connected vertices are visited and counted. 

    Args:
        neighbors (list): Some program's immediately connected vertices, used as a Stack.

    Returns:
        int: Sum total of all vertices connected to the calling vertex.
    """
    count_seen = 0
    while neighbors:
        curr = neighbors.pop()
        count_seen += 1
        for program in adj_list[curr]:
            neighbors.append(program)
    return count_seen

max_neighbor_count = -1

for k in adj_list.keys():
    if len(adj_list[k]) > 0:
        neighbor_count = dfs(adj_list[k].copy()) # Pass-By-Value 
        if neighbor_count > max_neighbor_count:
            max_neighbor_count = neighbor_count
            max_edge = k

result = max_edge
print(f'Day 7 Part 1: The name of the bottom program is {result}.\n')    