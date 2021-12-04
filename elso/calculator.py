import secret_logic


def ask():
    print("Calculator app\nPlease give me the first operand: ")
    text = input()
    while not text.isnumeric():
        print("Bad input! Try again!")
        text = input()
    operand1 = int(text)

    print("The operator: ")
    text = input()
    while not secret_logic.is_supported_operator(text):
        print("Bad input! Try again!")
        text = input()
    l_operator = text

    print("Second operand: ")
    text = input()
    if l_operator == '/':
        while not (secret_logic.is_numeric(text) & (text != '0')):
            print("Bad input! Try again!")
            text = input()
    else:
        while not secret_logic.is_numeric(text):
            print("Bad input! Try again!")
            text = input()

    operand2 = int(text)

    return operand1, l_operator, operand2


op1, operator, op2 = ask()
