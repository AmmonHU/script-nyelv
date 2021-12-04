def is_numeric(text):
    return text.isnumeric()


def is_supported_operator(text):
    return text in ['+', '-', '*', '/']


def calculate(operand1, l_operator, operand2):
    result = 0

    if l_operator == '+':
        result = operand1 + operand2
    elif l_operator == '-':
        result = operand1 - operand2
    elif l_operator == '*':
        result = operand1 * operand2
    elif l_operator == '/':
        result = operand1 / operand2

    return result
