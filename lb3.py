from collections import deque, defaultdict


def Dfs(graph, start):
    passing = set()
    stack = [start]

    while stack:
        current = stack.pop()
        if current not in passing:
            print(current)
            passing.add(current)
            neighbors = sorted(graph[current], reverse=True)
            stack.extend(neighbors)


def Bfs(graph, start):
    passing = set([start])
    queue = deque([start])

    while queue:
        current = queue.popleft()
        print(current)
        neighbors = sorted(graph[current])
        for neighbor in neighbors:
            if neighbor not in passing:
                passing.add(neighbor)
                queue.append(neighbor)


def build_graph():
    graph_type, start_vertex, search_type = input().split()
    graph = defaultdict(list)

    while True:
        try:
            line = input().strip()
            if not line:
                break
            u, v = line.split()
            graph[u].append(v)
            if graph_type == 'u':
                graph[v].append(u)
        except EOFError:
            break

    return graph, start_vertex, search_type


def main():
    graph, start_vertex, search_type = build_graph()
    if search_type == 'b':
        Bfs(graph, start_vertex)
    elif search_type == 'd':
        Dfs(graph, start_vertex)


if __name__ == "__main__":
    main()
