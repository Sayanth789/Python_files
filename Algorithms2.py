# Implementation of BFS
# _____________________________________________________________________________________________________

import heapq
from collections import deque

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])  # row is the len(grid) and col is the len(grid[0])
    queue = deque([(start,[])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path + [(x , y)] # Found the goal
        
        for dx , dy in [(-1,0), (1, 0), (0, -1), (0, 1)]: # Up, Down, Left, Right
            nx , ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append((nx, ny), path + [(x, y)])
                visited.add(nx, ny)

    return None # No path found           

# Implementation of DFS
def dfs(grid, start, end, path=[], visited=set()):
    x, y = start
    if start == end:
        return path + [start]  # Found the goal
    
    visited.add(start)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0,1)]:
        nx, ny = x + dx , y + dy
        if  0 <= nx < len(grid) and  0  <= ny < len(grid[0]) and grid[nx][ny] != 1 and ( nx, ny) not in visited:
            result = dfs(grid, (nx, ny), end, path + [start], visited)
            if result:
                return result
    return None # NO path found        
            
# Dijkstra's algorithm
def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start, [])]   # (cost , position , path)
    visited = set()

    while pq:
        cost, (x, y) , path = heapq.heappop(pq)

        if (x, y) == end:
            return path + [(x, y)] # Found the goal
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx , ny = x + dx , y + dy 
            if 0 <= nx < rows and   0 <= ny < cols and grid[nx][ny] != 1:
                heapq.heappush(pq, (cost + 1, (nx , ny), path + [(x, y)]))
    return None  # No path found


# A star Algorithm
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # manhattan distance
    
def astar(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    pq = [(0 + heuristic(start, end), 0 , start, [])]  # (f-score . g-score ,position, path)
    visited = set()

    while pq:
        _, cost, (x, y), path = heapq.heappop(pq)

        if (x, y) == end:
            return path + [(x, y)]
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx , dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx , y + dy
            if  0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != 1:
                g = cost + 1
                f = g + heuristic((nx, ny), end)
                heapq.heappush(pq, (f, g, (nx, ny), path + [(x, y)])) 

    return None # No path found            
# test case 
