## Name : Meagan Gould 
##this program helps determine the interest amount paid for a loan,
##how much the montly payment is, and how much is paid with the interest applied in the end
## the input are: amount borrowing, inerest rate,
##and how many months the loan is for
## Certificaton of Authenticity:
## I certify that this lab is entirely my own work.
## I have discussed this lab with Shefalli and Megan.

def findInterestRate():
    print("This code will help you figure out how much you are ", end=" ")
    print("payying in interest rates, monthly payments, and how much ", end=" ")
    print("you are paying back for a loan.")

    ## user input- interest, amount borrow(principal), and months all from user
    ## output - monthly payment, total for loan, and amound paid in interest
    ##          all to monitor

    ##input all info
    principal = eval(input("Enter the amount you are borrowing: "))
    interest = eval(input("Enter the interest rate for the loan: "))
    months = eval(input("Enter how many months the loan is for: "))
       
    ## calculate rate   
    YEARLY_PERCENTAGE = 1200
    rate = interest / YEARLY_PERCENTAGE

    
    ## calc monthly payment
    monthlypayment = (principal * (rate *(1+rate)**months))/(((1+rate)**months)-1)
    
    ## calc total loan amount
    totalloanamount= monthlypayment * months
    
    ## calc total interest paid
    totalinterestpaid = totalloanamount - principal

    ## output all info
    print("Your monthly payment is: ", monthlypayment)
    print("Your total amount paid for the loan is: ", totalloanamount)
    print("Your total interest paid is: ", totalinterestpaid)
     
