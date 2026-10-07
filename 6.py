# Program 6: Minimum Spanning Tree
# Using Kruskal's and Prim's Algorithms


# ---------- Kruskal's Algorithm ----------
def kruskal_mst(vertices, edges):

    edges.sort(key=lambda x: x[2])

    parent = list(range(vertices))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    mst = []
    total_cost = 0

    for u, v, weight in edges:

        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            parent[root_v] = root_u

    return mst, total_cost


# ---------- Prim's Algorithm ----------
def prim_mst(graph):

    n = len(graph)

    selected = [False] * n
    selected[0] = True

    mst = []
    total_cost = 0

    for _ in range(n - 1):

        minimum = float('inf')
        x = -1
        y = -1

        for i in range(n):

            if selected[i]:

                for j in range(n):

                    if not selected[j] and graph[i][j] != 0:

                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        mst.append((x, y, minimum))
        total_cost += minimum
        selected[y] = True

    return mst, total_cost


# ---------- Main Program ----------

print("Minimum Spanning Tree")

# Graph for Kruskal
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, cost = kruskal_mst(4, edges)

print("\nKruskal's Algorithm")
for u, v, weight in mst:
    print(u, "--", v, "=", weight)

print("Total Cost =", cost)


# Graph for Prim
graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

mst, cost = prim_mst(graph)

print("\nPrim's Algorithm")
for u, v, weight in mst:
    print(u, "--", v, "=", weight)

print("Total Cost =", cost)