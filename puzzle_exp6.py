from heapq import heappush, heappop
def solve(start, goal):
    def h(s): return sum(a != b and a for a, b in zip(s, goal))
    def moves(s):
        i = s.index(0)
        x, y = divmod(i, 3)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                ni = nx * 3 + ny
                t = list(s); t[i], t[ni] = t[ni], t[i]
                yield tuple(t)
    open_set, seen = [(h(start), 0, start, [])], set()
    while open_set:
        f, g, s, p = heappop(open_set)
        if s in seen: continue
        if s == goal: return p + [s]
        seen.add(s)
        for ns in moves(s):
            heappush(open_set, (g+1+h(ns), g+1, ns, p+[s]))

def show(path):
    for s in path:
        for i in range(0, 9, 3): print(s[i:i+3])
        print()

start = (1, 2, 3, 4, 0, 5, 6, 7, 8)
goal  = (1, 2, 3, 4, 5, 6, 7, 8, 0)
show(solve(start,goal))