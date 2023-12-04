with open( r"D:\AI\fruitshoppingdjango\adventofcode\adventofcode\2023\4\input.txt", "r") as x:
    inp = x.readlines()

curr = inp[0]

x = curr.split()
#print(x)
left = x[2:12]
right = x[13:]

#print(left)
#print(right)

# z = "41 48 83 86 17"
# left = z.split()
# right = "83 86  6 31 17  9 48 53".split()

def func(left, right):
    y = set(left)
    points = 0 
    for i in range(len(right)):
        if right[i] in y:
            points+=1

    return points

    # part 1 return
    # if points==0:
    #     return 0
    # elif points>0:
    #     return 2**(points-1)
res = 0
hashmap = {i:1 for i in range(len(inp))}

for i in range(len(inp)):
    curr = inp[i]
    x = curr.split()
    left = x[2:12]
    right = x[13:]
    re = func(left, right)
    for j in range(re):
        hashmap[i+j+1] += hashmap[i]
    

    #res += func(left, right)
end = 0
for i in hashmap.values():
    end+= i

print(hashmap)
print(end)
#print(res)