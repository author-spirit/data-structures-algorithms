"""Ref: https://www.leetcode.com/problems/fruit-into-baskets
Title: Fruits Into Baskets

Naive: O(n^3)
Improvement 1: Include dict -> O(n^2) reduced
Improvement 2: When in invalid remove from state using "start" to contract
"""

fruits = [3,3,2,1,2,1,0]

max_length = 0

state = {}
start = 0
for i in range(len(fruits)):
    state[fruits[i]] = state.get(fruits[i], 0) + 1

    while len(state) > 2:
        state[fruits[start]] -=1

        if state[fruits[start]] == 0:
            del state[fruits[start]]

        start +=1

    max_length = max(i - start +1 , max_length)

print(max_length)
