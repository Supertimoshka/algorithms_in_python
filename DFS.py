graph = {6:[3, 5], 5: [3, 4, 6], 4: [3, 5], 3: [1, 2, 4, 5, 6], 2: [1, 3], 1:[2, 3]}

def dfs(graph, note):
    visited = []
    stack = [note]
    while len(stack) != 0:
        first = stack.pop(len(stack)-1)
        if visited.count(first) == 0:
                visited.append(first)
        notes = graph[first]
        for i in range(0, len(notes)):
            if visited.count(notes[i]) == 0:
                stack.append(notes[i])
    print(visited)

dfs(graph, 2)
        