##selection statements

##ex) say'hello'
## if your eyes are brown:
##    raise left hand
## else:
##    raise your right hand
##  say goodbye

##print("hi")
##if eyeColor="brown":   if true it will return True if false will return False
##    raise("left")
##else:
##    raise("right")
##print("bye")

## if boolean expression :
##    statements to run if exp is true
## else:
##    statment if exp it false

##relational operators:
##    == :equlatiy
##    != : inequality
##    >:greater than
##    <:less than
##    >= :great than or equal to
##    <= :less than or equal to

##age=eval(input("Age? "))
##if age >=18:
##      
##    print("can vote")
##      if age 21>=21:
##          print("can drink")
##
##else:
##  print("cant vote")
##  if age >=14:
##        print("can vote")
##    else:
##        print("not for awhile")
##print("done")
## age 15- output:done- false
## age 18- output:can vote, done-true
##age 21-outputL can vote, can drink, done-true
##hit false and it quits evaluating
## can have if without else cannot have else without if

##logical operators
##and
##or
##not

def findMin(val1,val2):
    if val1<val2:
        minVal=val1
    else:
        minVal=val2
    return minVal
#input: parameter repsenting has mileage of auto
# output: return a sting stating good, fair or bad mileage
def gasAppeal(gasMileage):
    if gasMileage >= 30:
        appeal="good"
    else:
        if gasMileage>=20:
                appeal="fair"
        else:
            appeal="bad"
    return appeal

##input: parameter str password
##output: return boolean if pwd is long than 6 characters--> true

def goodPassword(password):
    first= ord(password[0])
    if len(password) >=6 and first >= ord("A") and first<= ord("Z"):
        isGood= True
    else:
        isGood= False
    return isGood
def main():
    minVal=findMin(3,7)
    print("Min: " +str(minVal))

    minVal=findMin(7,3)
    print("Min: " + str(minVal))

    ##test gas appeal
    ans=gasAppeal(10)
    print("10", ans)

    ans=gasAppeal(25)
    print("25", ans)

    ans=gasAppeal(20)
    print("20", ans)

    ans=gasAppeal(30)
    print("30", ans)

    ans=gasAppeal(35)
    print("35", ans)

    # test good password
    for pwd in ["hi","Friend", "TryThis","goodbye"]:
        
        isGood= goodPassword(pwd)
        if isGood==True:
            print(pwd+" is good")
        else:
            print(pwd+" is no good")
    

    
    
main()
