def printVar():
    total = 0
    for i in range(5):
        total=total+(i+1)
        print(total)
    print()
def printVar2():
    total=0
    for i in range(1,4):
        for j in range(i,5):
            total=total+j
            print(total)
    print()

def threes():
    num2=100
    for i in range(num2):
        num = i * 3
        print(num, end= " ")

    print()
