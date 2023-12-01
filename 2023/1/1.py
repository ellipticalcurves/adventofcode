import re

x = open( r"D:\AI\fruitshoppingdjango\adventofcode\adventofcode\2023\1\input.txt", "r")
inp = x.readlines()

x.close()

num = [str(i) for i in range(10)]

nums = set(num)


def findfirstnum(input):
    for i in range(len(input)):
        if input[i] in nums:
            return input[i]

def findlastnum(input):
    for i in range(len(input)-1,-1,-1):
        if input[i] in nums:
            return input[i]

numbers = {
           "zero": "z0ro",
            "one": "o1e",
           "two": "t2o",
           "three": "t3ree",
           "four": "fo4r",
           "five": "f5ve",
           "six": "s6x",
           "seven": "se7en",
           "eight": "e8ght",
           "nine": "n9ne"
           }

def preprocess(input):
    for key, value in numbers.items():
        input = re.sub(key, value, input)
    return input

print(preprocess("adf eightwo adfadf"))



newinp = []
for i in range(len(inp)):
    newinp.append(preprocess(inp[i]))


res = 0
for i in range(len(newinp)):
    x = findfirstnum(newinp[i])
    y = findlastnum(newinp[i])
    ans = str(x) + str(y)
    print(ans)
    res+=int(ans)
print(res)


