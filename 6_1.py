def kruskal_mst(vertices, edges):

    # Sort edges according to weight
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

        # If roots are different, no cycle is formed
        if root_u != root_v:
            mst.append((u, v, weight))
            total_cost += weight
            parent[root_v] = root_u

    return mst, total_cost


# Example graph
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst, cost = kruskal_mst(4, edges)

print("Kruskal MST:")

for u, v, weight in mst:
    print(u, "--", v, "=", weight)

print("Total Cost:", cost)