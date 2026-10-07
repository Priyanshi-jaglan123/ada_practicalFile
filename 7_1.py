def dijkstra(graph, source):

    n = len(graph)

    distance = [float('inf')] * n
    visited = [False] * n

    distance[source] = 0

    for _ in range(n):

        # Find unvisited vertex with minimum distance
        minimum = float('inf')
        u = -1

        for i in range(n):
            if not visited[i] and distance[i] < minimum:
                minimum = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        # Update neighbouring vertices
        for v in range(n):

            if graph[u][v] != 0:

                new_distance = distance[u] + graph[u][v]

                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance


# Example graph
graph = [
    [0, 4, 1, 0],
    [4, 0, 2, 5],
    [1, 2, 0, 8],
    [0, 5, 8, 0]
]

source = 0

distance = dijkstra(graph, source)

print("Shortest distances from vertex", source)

for i in range(len(distance)):
    print("To", i, "=", distance[i])