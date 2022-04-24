graph = {1: [2, 3, 4], 2: [1, 4, 5], 3: [1, 4], 4: [1, 2, 3, 5, 6, 7], 5: [2, 4], 6: [4, 7], 7: [4, 6]}

def dfs(graph, note, target):
    visited = []
    stack = [note]
    isFinded = False
    while len(stack) != 0:
        lastNote = stack.pop(len(stack) - 1) 
        if visited.count(lastNote) == 0:
            if target == lastNote:
                isFinded = True
                break
            visited.append(lastNote)
            notes = graph[lastNote]
            for i in range(0, len(notes)):
                if visited.count(notes[i]) == 0:
                    stack.append(notes[i])
    if isFinded:
        print("Элемент найден")
    else:
        print("Элемент не найден")

dfs(graph, 3, 7)