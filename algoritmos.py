import math
from collections import deque

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return math.sqrt((x_2-x_1)**2+(y_2-y_1)**2)
    
def depth_search(graph, start):
    stack = deque()
    visited = []
    path = []
    stack.append(start)
    visited.append(start)
    while(len(stack)>0):
        current = stack.pop()
        path.append(current)
        for vertex in graph[current]:
            if vertex[0] not in visited:
                visited.append(vertex[0])
                stack.append(vertex[0])
    
    return path

def breadth_search(graph, start):
    queue = deque()
    visited = []
    path = []
    queue.append(start)
    visited.append(start)
    while(len(queue)>0):
        current = queue.popleft()
        path.append(current)
        for vertex in graph[current]:
            if vertex[0] not in visited:
                visited.append(vertex[0])
                queue.append(vertex[0])
    
    return path

    
