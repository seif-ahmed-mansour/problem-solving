def Watermelon(weight):
    weight=int(weight)
    for i in range(2,weight//2+1,2):
        if (weight//2)%2==0:
            return "true"
        else:
            return "false"
print(Watermelon(8))