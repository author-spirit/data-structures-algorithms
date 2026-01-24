"""
Ref: https://neetcode.io/problems/valid-tree


"""

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

adjList = {p: [] for p in range(n)}
vis = [None] * n
stack = []

for cur,pre in edges:
    adjList[cur].append(pre)

def dfs(ver):
    if vis[ver] or ver in stack:
        return False

    vis[ver] = True
    for n in adjList[ver]:
        if not dfs(n):
            return False

        stack.append(ver)

    return True

# <<main>>

# Perform dfs on each node
# Do not traverse on visited nodes
for node in range(n):
    if not vis[node]:
        dfs(node)

print(stack)
