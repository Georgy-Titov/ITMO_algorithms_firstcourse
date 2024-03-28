from collections import deque


def bfs(start_point, search_point, graph):
    search_queue = deque()
    search_queue += graph[start_point]
    visited = []
    while search_queue:
        vertex = search_queue.popleft()
        if vertex not in visited:
            if vertex == search_point:
                print("Found!")
                return True
            else:
                search_queue += graph[vertex]
                visited.append(vertex)
    print("Not found!")
    return False


graph = {"A": ["B", "C"],
         "B": ["D"],
         "C": ["E"],
         "D": ["C"],
         "E": ["G"],
         "F": ["C", "E"],
         "G": ["E", "F", "H"],
         "H": ["K"],
         "K": ["G", "H"]}

bfs("G", "A", graph)
