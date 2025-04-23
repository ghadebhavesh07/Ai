import heapq
def a_star_search(start, goal, get_neighbors, heuristic, cost_function=lambda a, b: 1):
    open_set = [(heuristic(start, goal), start)]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    open_set_hash = {start}
    while open_set:
        current_f, current = heapq.heappop(open_set)
        open_set_hash.remove(current)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path (start to goal)
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + cost_function(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in open_set_hash:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    open_set_hash.add(neighbor)
    return None
def example_grid_usage():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]  # 0: open, 1: obstacle
    start = (0, 0)
    goal = (4, 4)
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    def get_neighbors(node):
        x, y = node
        neighbors = []
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                neighbors.append((nx, ny))
        return neighbors
    path = a_star_search(start, goal, get_neighbors, heuristic)
    return path