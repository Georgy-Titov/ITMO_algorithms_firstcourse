def dfs(start, goal, graph, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == goal:
        return path
    if start not in graph:
        return False
    shortest = None
    for vertex in graph[start]:
        if vertex not in path:
            new_path = dfs(vertex, goal, graph, path)
            if new_path:
                if shortest is None or len(new_path) < len(shortest):
                    shortest = new_path

    return shortest


a = {"A": ["B", "C"],
     "B": ["D"],
     "C": ["E"],
     "D": ["C"],
     "E": ["G"],
     "F": ["C", "E"],
     "G": ["E", "F", "H"],
     "H": ["K"],
     "K": ["G", "H"]}

s = "K"
g = "H"
shortest_path = dfs(s, g, a)
if shortest_path:
    print(f"Path from {s} to {g}:")
    print(*shortest_path, sep=" ---> ")
else:
    print("No path!")
