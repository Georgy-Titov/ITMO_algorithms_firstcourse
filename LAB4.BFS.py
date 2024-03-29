from collections import deque


def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: start}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node

    if goal not in visited.keys():
        print(f"No path from {start} to {goal}!")
    else:
        print(f"Path from {g} to {s}:\n{g}", end='')
        while goal != start:
            goal = visited[goal]
            print(f" <--- {goal}", end='')

    return 0


a = {"A": ["B", "C"],
     "B": ["D"],
     "C": ["E"],
     "D": ["C"],
     "E": ["G"],
     "F": ["C", "E"],
     "G": ["E", "F", "H"],
     "H": ["K"],
     "K": ["G", "H"]}


s = "A"
g = "F"
result = bfs(s, g, a)
