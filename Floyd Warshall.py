def floyd_warshall(graph):
	n = len(graph)
	distances = graph.copy()
	for k in range(n):
		for i in range(n):
			for j in range(n):
				distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
	return distances

inf = float("inf")
graph = [
	[3, 5, inf, 2],
	[3, 4, 3, inf],
	[1, inf, 5, inf],
	[7, 4, inf, 3]
]

shortest_path = floyd_warshall(graph)
for row in shortest_path:
	print(row)