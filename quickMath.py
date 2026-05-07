import random

min_operand = 3
max_operand = 12

operators = ["+", "-", "/", "*"]


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)

    return expr


while True:
    expression = generate_problem()
    answer = eval(expression)
    response = input("solve: " + expression + "\n")
    if float(response) == answer:
        print("you done it")
    else:
        print("you failed, the answer was " + answer)