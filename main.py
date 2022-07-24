expression = input("Expression: ")
x, y, z = expression.split(" ")

if y == "+":
    answer = (float(x) + float(z))
    print(answer)
elif y == "-":
    answer = (float(x) - float(z))
    print(answer)
elif y == "*":
    answer = (float(x) * float(z))
    print(answer)
elif y == "/":
    answer = (float(x) / float(z))
    print(answer)

