# 05 May 2022
# Aakash Sir


def dfs(node, parent, vis, dis, low, graph, ap, timer):
    vis[node] = True
    dis[node] = timer
    low[node] = timer
    child = 0
    timer += 1

    for nbr in graph[node]:
        if nbr == parent:
            continue
        elif vis[nbr] == False:
            dfs(nbr, node, vis, dis, low, graph, ap, timer)
            low[node] = min(low[node], low[nbr])
            if low[nbr] >= dis[node] and parent != -1:
                ap.add(node)
            child += 1
        else:
            low[node] = min(low[node], dis[nbr])
    if child >= 2 and parent == -1:
        ap.add(node)

def buildGraph(edges, vertices):
    graph = dict()

    for i in range(vertices):
        graph[i] = list()

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def findArticulationPoints(edges, vertices):
    visited = [False] * vertices
    discoveryTime = [0] * vertices
    lowestTime = [0] * vertices
    articulationPoints = set()

    graph = buildGraph(edges, vertices)
    timer = 0
    for node in range(vertices):
        if visited[node] == False:
            dfs(node, -1, visited, discoveryTime, lowestTime, graph, articulationPoints, timer)
    
    return articulationPoints

if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [1, 2], [1, 3], [3, 4], [3, 6], [4, 5], [5, 6]]
    vertices = 7

    ans = findArticulationPoints(edges, vertices)
    print(ans)