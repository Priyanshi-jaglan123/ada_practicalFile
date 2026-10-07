# Program 7: Shortest Path
# Using Dijkstra's and Bellman-Ford Algorithms


# ---------- Dijkstra's Algorithm ----------
def dijkstra(graph, source):

    n = len(graph)

    distance = [float('inf')] * n
    visited = [False] * n

    distance[source] = 0

    for _ in range(n):

        minimum = float('inf')
        u = -1

        for i in range(n):

            if not visited[i] and distance[i] < minimum:
                minimum = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):

            if graph[u][v] != 0:

                new_distance = distance[u] + graph[u][v]

                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance


# ---------- Bellman-Ford Algorithm ----------
def bellman_ford(vertices, edges, source):

    distance = [float('inf')] * vertices
    distance[source] = 0

    # Relax edges V-1 times
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


# ---------- Main Program ----------

print("Shortest Path Algorithms")


# Dijkstra's Algorithm
graph = [
    [0, 4, 1, 0],
    [4, 0, 2, 5],
    [1, 2, 0, 8],
    [0, 5, 8, 0]
]

source = 0

distance = dijkstra(graph, source)

print("\nDijkstra's Algorithm")
print("Source Vertex =", source)

for i in range(len(distance)):
    print("To", i, "=", distance[i])


# Bellman-Ford Algorithm
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

print("\nBellman-Ford Algorithm")

if distance is None:
    print("Negative weight cycle exists.")
else:
    print("Source Vertex =", source)

    for i in range(vertices):
        print("To", i, "=", distance[i])