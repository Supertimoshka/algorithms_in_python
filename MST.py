# MST - Minimum Spanning Tree (минимальное остовное дерево)

import random
import math

# Повторить логику работы алгоритма Прима
def Prim(nodesCount, graph):
    spanningTree = []
    component = [random.randint(0, nodesCount - 1)]

    while len(component) != nodesCount:
        minWeight = math.inf

        for i in range(0, len(component)):
            for j in range(0, len(graph)):
                if graph[j]["from"] == component[i] and component.count(graph[j]["to"]) == 0 and graph[j]["weight"] < minWeight:
                    edge = graph[j]
                    minWeight = edge["weight"]
                    
        spanningTree.append(edge)
        component.append(edge["to"])

    return spanningTree


def sortGraph(graph):
    
    for i in range(0, len(graph) - 1):
        for j in range(0, len(graph) - i - 1):
            if graph[j]["weight"] > graph[j + 1]["weight"]:
                swap = graph[j]
                graph[j] = graph[j + 1]
                graph[j + 1] = swap


def Kruskal(nodesCount, graph):
    
    sortGraph(graph)

    components = []
    for i in range(0, nodesCount):
        components.append([i])        

    spanningTree = []
    for i in range(0, len(graph)):
        for j in range(0, len(components)):
            if components[j].count(graph[i]["from"]) != 0:
                indexFrom = j
            if components[j].count(graph[i]["to"]) != 0:
                indexTo = j
        if indexFrom < indexTo:
            components[indexFrom].extend(components.pop(indexTo))
            spanningTree.append(graph[i])
        if indexFrom > indexTo:
            components[indexTo].extend(components.pop(indexFrom))
            spanningTree.append(graph[i])

    return spanningTree
        
    
def printMST(MST):
    for i in range(0, len(MST)):
        print(MST[i]["from"], "-", MST[i]["to"], "\tw =", MST[i]["weight"])

# Избавиться от дублирования рёбер графа и перестроить логику алгоритмов
nodesCount = 6
graph = [
    {"from": 0, "to": 1, "weight": 10},
    {"from": 0, "to": 2, "weight": 5},
    {"from": 1, "to": 0, "weight": 10},
    {"from": 1, "to": 2, "weight": 4},
    {"from": 1, "to": 4, "weight": -2},
    {"from": 2, "to": 0, "weight": 5},
    {"from": 2, "to": 1, "weight": 4},
    {"from": 2, "to": 3, "weight": 7},
    {"from": 2, "to": 5, "weight": 3},
    {"from": 3, "to": 2, "weight": 7},
    {"from": 3, "to": 4, "weight": 7},
    {"from": 3, "to": 5, "weight": 5},
    {"from": 4, "to": 1, "weight": -2},
    {"from": 4, "to": 3, "weight": 7},
    {"from": 4, "to": 5, "weight": 2},
    {"from": 5, "to": 2, "weight": 3},
    {"from": 5, "to": 3, "weight": 5},
    {"from": 5, "to": 4, "weight": 2}
]

MSTPrim = Prim(nodesCount, graph)
printMST(MSTPrim)

MSTKruskal = Kruskal(nodesCount, graph)
printMST(MSTKruskal)