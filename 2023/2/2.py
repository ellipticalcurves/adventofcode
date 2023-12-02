input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

x = input.split()

print(x)
print(x[1][:-1])
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
print(curr)