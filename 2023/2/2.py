input = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"


y = open( r"D:\AI\fruitshoppingdjango\adventofcode\adventofcode\2023\2\input.txt", "r")
inp = y.readlines()
y.close()

print(inp[:4])
x = input.split() # gives something like ['Game', '1:', '4', 'blue,', '4', 'red,', '16', 'green;', '14', 'green,', '5', 'red;', '1', 'blue,', '3', 'red,', '5', 'green']

curr = x[1][:-1]


def func2(x):
    dic = {"b":0, "r":0, "g":0}

    for i in range(2, len(x)):
        if i % 2 == 0:
            num = int(x[i])
        elif i%2 == 1:
            if dic[x[i][0]] < num:
                dic[x[i][0]] = num
    prodsum = 1
    for i in dic.values():
        prodsum*=i
    return prodsum


print(func2(x))

cont = 0
for i in range(len(inp)):
    x = inp[i].split()
    #print(x)
    cont += func2(x)

print(cont)

        # if x[i][0]=="b" and num>14:
        #     curr = 0
        #     break
        # elif x[i][0]=="g" and num>13:
        #     curr = 0
        #     break
        # elif x[i][0]=="r"and num>12:
        #     curr = 0
        #     break
print(int(curr))


def func(x):
    curr = x[1][:-1]
    for i in range(1, len(x)):
        if i % 2 == 0:
            num = int(x[i])
        elif i%2 == 1:
            if x[i][0]=="b" and num>14:
                curr = 0
                break
            elif x[i][0]=="g" and num>13:
                curr = 0
                break
            elif x[i][0]=="r"and num>12:
                curr = 0
                break
    return int(curr)

# print(func(x))

# cont = 0
# for i in range(len(inp)):
#     x = inp[i].split()
#     #print(x)
#     cont += func(x)

# print(cont)