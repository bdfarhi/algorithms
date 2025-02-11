from collections import deque, defaultdict


def BFS(s):
    queue = deque([s])
    visited = set()
    visited.add(s)
    while queue:
        node = queue.popleft()
        for neighbors in node.neighbors:
            if neighbors not in visited:
                queue.append(neighbors)
                visited.add(neighbors)

def DFS(s):
    visited= set()
    recursive_DFS(s,visited)

def recursive_DFS(s,visited):
    visited.add(s)
    for neighbors in s.neighbors:
        if neighbors not in visited:
            recursive_DFS(neighbors,visited)

def BFS_Bipartiteness(s):
    visited = set()
    queue = deque([s])
    color = defaultdict(int)
    color[s] = 0
    while queue:
        node = queue.popleft()
        for neighbors in node.neighbors:
            if neighbors not in visited:
                queue.append(neighbors)
                visited.add(neighbors)
                color[neighbors] = 1 - color[node]
            elif color[neighbors] == color[node]:
                return "G is not bipartite"
    return "G is bipartite"

def Topologial_Sort(graph):
    d = defaultdict(int)
    for node in graph:
        d[node] = 0
    for v in graph:
        for u in graph[v]:
            d[u] = d[u] + 1
    queue = deque()
    i = 0
    for node in d:
        if d[node] == 0:
            queue.append(node)
    while queue:
        v = queue.popleft()
        i = i + 1
        for u in graph[v]:
            d[u] = d[u] - 1
            if d[u] == 0:
                queue.append(u)
    if i < len(graph):
        return "Not a DAG"
    return "Is a DAG"


