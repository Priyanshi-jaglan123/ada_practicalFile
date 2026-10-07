def bellman_ford(vertices, edges, source):

    distance = [float('inf')] * vertices
    distance[source] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):

        for u, v, weight in edges:

            if distance[u] != float('inf'):
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Check for negative cycle
    for u, v, weight in edges:

        if distance[u] != float('inf'):
            if distance[u] + weight < distance[v]:
                return None

    return distance


# Example graph
edges = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 4),
    (3, 1, -2)
]

vertices = 4
source = 0

distance = bellman_ford(vertices, edges, source)

if distance is None:
    print("Negative weight cycle exists.")
else:
    print("Shortest distances from vertex", source)

    for i in range(vertices):
        print("To", i, "=", distance[i])