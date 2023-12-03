input = "Game 11: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"


y = open( r"D:\AI\fruitshoppingdjango\adventofcode\adventofcode\2023\2\input.txt", "r")
inp = y.readlines()
y.close()

print(inp[:4])
x = input.split() # gives something like ['Game', '1:', '4', 'blue,', '4', 'red,', '16', 'green;', '14', 'green,', '5', 'red;', '1', 'blue,', '3', 'red,', '5', 'green']


# print(x)
# print(x[1][:-1])


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

print(func(x))

cont = 0
for i in range(len(inp)):
    x = inp[i].split()
    #print(x)
    cont += func(x)

print(cont)