# Ref: https://www.hellointerview.com/learn/code/intervals/overview
# Title: Find the minimum number of intervals to remove to eliminate any overlap
# Original Input: [[4,6],[11,17],[2,18],[7,10]]

events = [[4,6],[11,17],[2,18],[7,10]]

events.sort(key = lambda key: key[1])
# [[4,6], [7,10], [11,17], [2,18]]

def find_overlaps(meetings):
    overalaps = 0
    for i in range(1, len(meetings)):
        if meetings[i-1][1] > meetings[i][0]:
            overalaps+=1

    return overalaps

print("No. of overlapping: ", find_overlaps(events))
