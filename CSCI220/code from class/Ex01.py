def prob1():
    print("a.")
    print(3 + 2 // 5 + -2 * 4 + 2 ** 2 ** 3)
    print("\nb.")
    print(2 * (1 + - (3//4) // 2) * (2 - 6 %3))
    print("\nc.")
    print(33/4//3)
    print("\nd.")
    print(float(33//4//3))
    print("\ne.")
    print(33//4//float(3))
    print("\nf.")
    print(int(9.0/2))
    print("\ng.")
    print(9.0//2)
    print("\nh.")
    print("\"" + str(9.5) +"\"")
    print("\ni.")
    print(eval("5"))
    print("\nj.")
    print(list(range(3, 12, 2)))

##prob2
##a)
## i    val  
##       7
## 4    11
## 6    17
## 8    25
## 10   35

##b)
## i   j    val
##          0
## 9   2    2
##     3    5
##     4    9
##     5    14
##     6    20
##     7    27
##     8    35
## 6   2    37
##     3    40
##     4    44
##     5    49
## 3   2    51

     
def prob3():
    total = 0
    numTerms = eval(input("Num terms: "))
    for i in range(numTerms):
        num = i + 1
        denom = num * 2 + 1
        print(str(num) + "/" + str(denom)) #error checking
        total += num/denom #total = total + num/denom

def prob4():
    print("1.")
    for i in [1, 4, 9, 16]:
        print(i)

    print("\n2.")
    for i in range(5):
        print(i)

    print("\n3.")
    total = 0
    for i in range(3):
        total = total + i
    print(total)

    print("\n4.")
    product = 1
    for i in range(3):
        product = product * i
        print(product)

    print("\n5.")
    product = 1
    for i in range(3):
        product = product * (i+1)
    print(product)



#probl5
# A rectangle that is twice as long as it is tall, labeled with Practice with
#   a circle in the middle.

#prob6
# objects: win, pt, cir
# classes: GraphWin, Point, Circle
# methods: draw() and the constructors for Point, GraphWin and Circle
          
