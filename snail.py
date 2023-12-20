def snail(array):
    result = []
    while array:
        result += array.pop(0)
        if array and array[0]:
            for row in array:
                result.append(row.pop(-1))
        if array:
            result += array.pop()[::-1]
        if array and array[0]:
            for row in reversed(array):
                result.append(row.pop(0))
    return result
