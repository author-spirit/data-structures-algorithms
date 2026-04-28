"""
102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""

from collections import deque

root = [3, 9, 20, None, None, 15, 7]

nodes = []

que = deque([])
nodes = [root[0]]

for i in range(1,len(root)):
    level = []

    if i == 1:
        que.append(root[i])

    while que and len(que) < 2:
        level

que = deque([root[0]])

nodes = []

x = 1
while que:
    count = 0
    for i in range(x, len(root)):
        if count == 2:
            break
