def calc(expression):
    tokens = tokenize(expression)
    return evaluate(tokens)
def tokenize(expression):
    tokens = []
    current = ''
    for char in expression:
        if char.isdigit() or char == '.':
            current += char
        elif char in '*/+-()':
            if current:
                tokens.append(current)
                current = ''
            tokens.append(char)
    if current:
        tokens.append(current)
    return tokens

def evaluate(tokens):
    def helper():
        nonlocal index
        result = term()
        while index < len(tokens) and tokens[index] in '+-':
            operator = tokens[index]
            index += 1
            operand = term()
            if operator == '+':
                result += operand
            else:
                result -= operand
        return result
    def term():
        nonlocal index
        result = factor()
        while index < len(tokens) and tokens[index] in '*/':
            operator = tokens[index]
            index += 1
            operand = factor()
            if operator == '*':
                result *= operand
            else:
                result /= operand
        return result
    def factor():
        nonlocal index
        token = tokens[index]
        index += 1
        if token == '(':
            result = helper()
            index += 1  
            return result
        elif token == '-':
            return -factor() if tokens[index - 1] == '-' else float(tokens[index])
        else:
            return float(token)
    index = 0
    return helper()