"""
Kruskal's Algorithm:
    Greedy Algorithm, uses UnionSet to find MST

Requirements:
    Visited Array, Priority Queue (MinHeap), MST Result & Sum
"""
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


edges = [
    [1, 4, 1], [1, 2, 2], [2, 3, 3], [2, 4, 3],
    [1, 5, 4], [3, 4, 5], [2, 6, 7], [3, 6, 8], [4, 5, 9]
]
n = 7

edges = [(w, u, v) for u, v, w in edges]
edges.sort(key=lambda x: x[0])

uf = UnionFind(n)
mst_weight = 0

for w, u, v in edges:
    if uf.union(u, v):
        mst_weight += w

print(mst_weight)
