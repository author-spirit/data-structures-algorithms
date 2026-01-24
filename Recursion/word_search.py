"""
Ref: https://leetcode.com/problems/word-search/
"""

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]

word="CAZ"

is_found = False
visited = set()
row=len(board)
col=len(board[0])

def track(i,j,ch):
    if ch >= len(word):
        return True

    if i < 0 or i >= row or j < 0 or j >= col or f"{i}{j}" in visited:
        return False

    if board[i][j] == word[ch]:
        ch+=1

    visited.add(f"{i}{j}")

    is_found = track(i,j-1,ch) or track(i-1,j,ch) or track(i,j+1,ch) or track(i+1,j,ch)
    return is_found

def search():
    c=0
    for i in range(row):
        for j in range(col):
            if board[i][j] == word[c]:
                return track(i,j,c)

#print('visited',visited,search())
visited.add('00')
visited.add('01')
print(track(0,2,0))
