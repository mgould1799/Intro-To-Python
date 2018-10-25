##relational operator not equal to !=
##5 !=5 false
##5 !=7 true

## 3 logical operators: and, or, not
##<boolean exp> and <boolean expression>
##5!=7 and 3>2
## true    true  -> true

##<be> or <be>
##7<2 or 5>=5
## false true --> true

##not <be>
## not 7<3
##      false --> true 

##truth tables for: and, not, or (like 207)

## false and _____ => false
## python returns a false if the first response is false immdediatly
## i<len(values) and values[i]== searchVal
##list contains 5 elements (01234) the second value at 5 will cause an index
##      out of rage

## true or ___ => true
## any portion of true can terminate and be true

##if not true, it is false
##if not false, it is true

##what goes first: not, and, or (like pemdas)

##5>3 or 7<5 and not 3>5
##   3      2         1
##       false         true
##              false
## true or
##      true 

##what goes first: not, and , or (like pemdas)

## (5>3 or 7<5) and not 3>5
##     true         true
##              true

## false or true and not false
##      3        2      1
##                      true
##              true
##    true
##          True


##num1=0
##for i in range(10):
##      num1+=.1
##num1=1.0 (it's a float)

##num2 = .1*10
##num1 == num2
## false. why? ##the decimal converstion of num1= .9999999
## for in equalities test for closeness
##take difference of 2 nums. if the difference is suffeciently small enough set it equal
##if num 1 == num2:
##          print('they are equal')
##else:
##          print('not equal')
##not equal

## abs(num1-num2) < epsilon means they are equal
##epsilon=.0001 (also depends on data that you are talking about)

##if abs(num1-num2)<.000001:
##      print('equal')
##else:
##      print('not equal')
##equal

## boolean function that accepts two floats that test for equality
def floatEqual(num1,num2):
    return abs(num1-num2)<.0001

def isAbc(letters):
##    if letters == "abc":
##        rtnVal= True
##    else:
##        rtnVal= False
##    return rtnVal 

    return letters == "abc"
##def total(num1, num2):
##      return num1+num2

def greatHundred(num):
    return num>100

def main():
    print(".1 and .2 equal: ", floatEqual(.1,.2))
    print(".2 and .1 equal: ", floatEqual(.2,.1))
    print(".999999 and .1 equal: ", floatEqual(.999999,.1))
    print(".1 and .0999999: :", floatEqual(.1,.099999))

    print("'abc': ", isAbc("abc"))
    print("'hi': ", isAbc("hi"))

    print("100>100 is: ", greatHundred(100))
    print("70>100 is: ", greatHundred(70))
    print("120>100 is: ", greatHundred(120))
main()
