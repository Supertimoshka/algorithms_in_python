import math

def Dijkstra(graph, node):
    weightMarks = []
    pathMarks = []
    notVisitedNodes = []

    for i in range(0, len(graph)):
        weightMarks.append(math.inf)
        pathMarks.append(node)
        notVisitedNodes.append(i)
    weightMarks[node] = 0
    
    visitedNodes = []
    while len(notVisitedNodes) != 0:
        minIndex = 0
        minNode = notVisitedNodes[minIndex]
        minWeight = weightMarks[minNode]
        
        for i in range(1, len(notVisitedNodes)):
            if minWeight > weightMarks[notVisitedNodes[i]]:
                minIndex = i
                minNode = notVisitedNodes[minIndex]
                minWeight = weightMarks[minNode]

        visitedNodes.append(notVisitedNodes.pop(minIndex))

        for i in range(0, len(graph)):
            if graph[minNode][i] >= 0 and weightMarks[minNode] + graph[minNode][i] < weightMarks[i]:
                weightMarks[i] = weightMarks[minNode] + graph[minNode][i]
                pathMarks[i] = minNode

    return {"pathMarks": pathMarks, "weightMarks": weightMarks}

def restorePaths(pathMarks):
    paths = []
    for i in range(0, len(pathMarks)):
        path = []
        index = i
        value = pathMarks[index]
        
        while index != value:
            # path.append(index)
            path.insert(0, index)
            index = value
            value = pathMarks[index]
        
        # path.append(value)
        # path.reverse()
        path.insert(0, value)
        paths.append(path)
    
    return paths

node = 3
graph = [
    [-1, 10, 30, 50, 10],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 10],
    [-1, 40, 20, -1, -1],
    [10, -1, 10, 30, -1]
]

# def createGraph(N, M, K): Долелать !
    # for i in range()

marks = Dijkstra(graph, node)
print("Path marks:\t", marks["pathMarks"])
print("Weight marks:\t", marks["weightMarks"])

paths = restorePaths(marks["pathMarks"])
print("Paths:\t\t", paths)