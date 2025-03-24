
from collections import deque

def bfs(graph, first):
    GoPlenty = {first}  
    queue = deque([first])    # Using deque instead of list
    while queue:
        current = queue.popleft()  # popleft() is O(1) in deque
        print(current) 
        for neighbor in sorted(graph[current]):  
            if neighbor not in GoPlenty:
                GoPlenty.add(neighbor)  
                queue.append(neighbor)

def dfs(graph, start, GoPlenty):
    stack = [start] 
    while stack:
        current = stack.pop()  
        if current not in GoPlenty:
            print(current)  
            GoPlenty.add(current)  
            stack.extend(sorted(graph[current], reverse=True))

def Graph():
    graph_type, first_vertex, search_type = input().split()
    graph = {}
    edges = []

    while True:
        try:
            line = input().strip()
            if not line:
                break
            edges.append(tuple(line.split()))
        except EOFError:
            break

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        if graph_type == 'u':
            graph[v].append(u) 
    return graph, first_vertex, search_type

def main():
    graph, first_vertex, search_type = Graph()
    if search_type == 'b':
        bfs(graph, first_vertex) 
    elif search_type == 'd':
        dfs(graph, first_vertex, set())  

if __name__ == "__main__":
    main()
