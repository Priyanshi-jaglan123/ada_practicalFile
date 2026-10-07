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


# Example graph
graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

mst, cost = prim_mst(graph)

print("Prim MST:")

for u, v, weight in mst:
    print(u, "--", v, "=", weight)

print("Total Cost:", cost)