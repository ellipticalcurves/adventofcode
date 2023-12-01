import re

x = open( r"D:\AI\fruitshoppingdjango\adventofcode\adventofcode\2023\1\input.txt", "r")
inp = x.readlines()
#print(inp)
x.close()

#print(len(inp))
num = [str(i) for i in range(10)]
#print(num)
nums = set(num)
#print(nums)

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
numbers1 = {
           "zero": "0",
            "one": "1",
           "two": "2",
           "three": "3",
           "four": "4",
           "five": "5",
           "six": "6",
           "seven": "7",
           "eight": "8",
           "nine": "9"
           }

def preprocess(input):
    for key, value in numbers.items():
        input = re.sub(key, value, input)
    return res

# def preprocess(input):
#     res = []
#     for key, value in numbers.items():
#         x = re.finditer(key, input)
#         for i in x:
#             res.append(i.start())
#     return res

print(preprocess("adf eightwo adfadf"))

def capture_first_last_digits(input_string):
    # Match the first and last digit
    first_digit_match = re.search(r'\d', input_string)
    last_digit_match = re.search(r'\d(?=[^\d]*\d*$)', input_string)

    # Check if matches are found
    first_digit = first_digit_match.group() if first_digit_match else None
    last_digit = last_digit_match.group() if last_digit_match else None

    return first_digit, last_digit


#print(capture_first_last_digits("8two1"))

newinp = []
# for i in range(len(inp)):
#     newinp.append(replace_in_order(inp[i], numbers))
# print(len(newinp))

# newinp = ["two1nine",
# "eightwothree",
# "abcone2threexyz",
# "xtwone3four",
# "4nineeightseven2",
# "zoneight234",
# "7pqrstsixteen"]

# newinp = [replace_in_order(newinp[i], numbers) for i in range(len(newinp))]
# print(newinp)
# res = 0
# for i in range(len(newinp)):
#     x = findfirstnum(newinp[i])
#     y = findlastnum(newinp[i])
#     ans = str(x) + str(y)
#     print(ans)
#     res+=int(ans)
# print(res)


