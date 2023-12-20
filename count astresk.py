def count_asterisks(s):
    count = 0
    between_pipes = False
    for c in s:
        if c == '|':
            between_pipes = not between_pipes
        elif c == '*' and not between_pipes:
            count += 1
    return count