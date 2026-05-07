# Ref: https://www.hellointerview.com/learn/code/intervals/overview
# Method: Sort by end time and merge
# Original Input: [[2,4], [9,12], [6,9], [13,15]]

events = [[1,5],[3,6],[8,10],[15,18]]
events = [[1,4],[3,5],[6,9]]

events.sort(key = lambda key: key[1])

def merge_intervals(meetings):
    merged = []
    for i in range(len(meetings)):
        if not merged or meetings[i][0] > merged[-1][1]:
            merged.append(meetings[i])
        else:
            merged[-1][1] = max(meetings[i][1], merged[-1][1])

    return merged

print("Merged Intervals: ", merge_intervals(events))
