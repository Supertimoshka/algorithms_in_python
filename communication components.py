graph = {1: [2], 2: [1], 3: [4, 6], 4: [3, 5, 6], 5: [4], 6: [3, 4, 7], 7: [6], 8: [9, 10], 9: [8, 10], 10: [8, 9], 11: []}

def bfs(graph, note):
    visited = []
    queue = [note]
    while len(queue) != 0:
        first = queue.pop(0)
        if visited.count(first) == 0:
            visited.append(first)
            for i in range(0, len(graph[first])):
                if visited.count(graph[first][i]) == 0:
                    queue.append(graph[first][i])
    return visited

def findComponents(graph):
    notVisited = list(graph.keys())
    visited = []
    components = []
    while len(notVisited) != 0:
        component = bfs(graph, notVisited[0])
        components.append(component)
        for i in range(0, len(component)):
            visited.append(component[i])
            notVisited.pop(notVisited.index(component[i]))
    return components

print(findComponents(graph))