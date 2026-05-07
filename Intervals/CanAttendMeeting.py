# Ref: https://www.hellointerview.com/learn/code/intervals/overview
# Method: Using Sort by start
# Original Input: [[2,4], [9,12], [6,9], [13,15]]
# Overall complexity: Time (O(n * logn)) : n intervals & sorting algo. Space: O(n) - aux space.

events = [[2,4], [9,12], [6,10], [13,15]]

events.sort(key = lambda key: key[0])

def can_attend(meetings):
    for i in range(1, len(meetings)):
        if meetings[i-1][1] > meetings[i][0]:
            return False

    return True

print("Can Attend Meeting?", "Yep" if can_attend(events) else "Nope")
