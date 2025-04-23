from queue import PriorityQueue

graph = {
    'A' : [('B', 1), ('C', 4)],
    'B' : [('D', 3)],
    'C' : [('D', 1)],
    'D' : [('E', 2)],
    'E' : []
}

heuristics = {
    'A' : 7,
    'B' : 6,
    'C' : 2,
    'D' : 1,
    'E' : 0,
}

def A_star(start , goal):
    pq = PriorityQueue()
    pq.put((0 + heuristics[start], 0, start, [start]))

    while not pq.empty():
        f, g, node, path = pq.get()

        if node == goal:
            return path, g

        for neighbour, cost in graph[node]:
            total_g = g + cost
            f = total_g + heuristics[neighbour]
            pq.put((f, total_g, neighbour, path + [neighbour]))

    return None, float('inf')

path, cost = A_star('A', 'E')
print("Path:",path)
print("cost:",cost)