def calc_amplitude(arr:list):
    for i in arr:
        if i=="error":
            arr.remove(i)
            continue
    return max(arr)-min(arr)
print(calc_amplitude([3, -2, -6, -1, "error", 9, 13, 17, 15, 14, 9, 5]))