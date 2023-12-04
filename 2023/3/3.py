from collections import deque


x = open( r"D:\AI\fruitshoppingdjango\adventofcode\adventofcode\2023\3\input.txt", "r")
inp = x.readlines()
x.close()

for i in range(len(inp)-1):
    inp[i] = inp[i][:-1]

#print(inp)

def part1(inp):
    dig = [str(i) for i in range(10)]
    digits = set(dig)
    #print(digits)

    ROWS = len(inp)
    COLS = len(inp[0])
    visit = set()
    #print(ROWS, COLS)

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
                    #print(inp[i][j], inp[dx][dy])
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

    return result
#print(part1(inp))
dig = [str(i) for i in range(10)]
digits = set(dig)
visit = set()
ROWS = len(inp)
COLS = len(inp[0])

def numdfs(i,j):
    ans = [inp[i][j]]
    x = j
    r = j
    vis = [(i,j)]
    while x-1<COLS and x-1>=0 and inp[i][x-1] in digits:
        if x>0:
            ans = [inp[i][x-1]] + ans
            vis.append((i,x-1))
            x-=1

    while r+1<COLS and r+1>=0 and inp[i][r+1] in digits:
        if r+1<COLS:
            ans.append(inp[i][r+1])
            vis.append((i,r+1))
            r+=1
    return ans, vis

#print(numdfs(0,0))

def dfs(i,j):
    vis = set()
    neighbs = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
    curr = []
    vis.add((i,j))
    for x, y in neighbs:
        dx, dy = i+x, j+y
        #print(inp[dx][dy])
        if (dx < ROWS and dy < COLS and 
            dx>=0 and dy>=0 and 
            inp[dx][dy] in digits and (dx,dy) not in vis):

            #check surrounding digits/dfs it?
            vis.add((dx, dy))
            ans, v = numdfs(dx,dy)
            for l in range(len(v)):
                vis.add(v[l])
            curr.append(ans)

    if len(curr)==2:
        return curr
        
    return 0

# cur = dfs(1,3)
# cu = []

# for i in range(len(cur)):
#     x = ""
#     for j in range(len(cur[i])):
#         x= x+cur[i][j]
#     cu.append(int(x))

#print(cu[0]*cu[1])

#print(dfs(8,5))

ress = 0 
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j]=="*":
            cur = dfs(i,j)
            if cur:
                cu = []
                for l in range(len(cur)):
                    x = ""
                    for k in range(len(cur[l])):
                        x = x + cur[l][k]
                    cu.append(int(x))
                #print(cu)
                #print(cu[0]*cu[1])
                ress += cu[0]*cu[1]

print(ress)

