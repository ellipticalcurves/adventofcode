from collections import deque


x = open( r"D:\AI\fruitshoppingdjango\adventofcode\adventofcode\2023\3\input.txt", "r")
inp = x.readlines()
x.close()

for i in range(len(inp)-1):
    inp[i] = inp[i][:-1]

print(inp)
dig = [str(i) for i in range(10)]
digits = set(dig)
print(digits)

ROWS = len(inp)
COLS = len(inp[0])
visit = set()
print(ROWS, COLS)

def bfs(i,j):
    weirdsym = ""
    curr = [inp[i][j]]
    q = deque()
    q.append((i,j))
    neighbs = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
    while q:
        i, j = q.pop()
        for x, y  in neighbs:
            dx, dy = i+x, j+y 
            if (dx < ROWS and dy < COLS and 
            dx>=0 and dy>=0 and 
            (dx,dy) not in visit and
              inp[dx][dy] in digits):
                q.append((dx,dy))
                visit.add((dx,dy))
                curr.append(inp[dx][dy])
                print(inp[i][j], inp[dx][dy])
            if (dx < ROWS and dy < COLS and 
            dx>=0 and dy>=0 and 
            (dx,dy) not in visit and inp[dx][dy] not in digits and inp[dx][dy]!="."):
                weirdsym = inp[dx][dy]
    #print(curr)
    res = ""
    for i in range(len(curr)):
        res = res + curr[i]
    #print(res)
    return int(res), weirdsym

result = 0
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j] in digits and (i,j) not in visit:
            visit.add((i,j))
            res, weirdsym = bfs(i,j)
            #print(weirdsym)
            if weirdsym:
                #print(res)
                result = result + res
            #else:
                #print(res)

print(result)
