print ("Enter a number")
user_input = input()
number = int(user_input)
mult = 0
while mult <= 9:
    result = mult * number
    print(mult, "x", number, "=", result)
    mult += 1
