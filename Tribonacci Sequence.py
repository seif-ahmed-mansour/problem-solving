def tribonacci(signature, n):
    if n==0:
        return []
    elif n<=len(signature):
        return signature[:n]
    else:
        sequence=signature[:]
        for i in range(3,n):
            next_element=sequence[i-1]+sequence[i-2]+sequence[i-3]
            sequence.append(next_element)
        return sequence
