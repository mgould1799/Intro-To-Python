##Name:Meagan Gould
##Problem:This program will find the RMS and Harmonic Mean for a set of numbers
##Certification of Authenticity: I certify that this lab is entirely my own work.
## I did discuss this lab with Prof. Stalvey and Shefalli

import math
def mean():
    print("This program will help you find out the average, root mean square (rms) average, and harmonic average")

    ##totals used for math and setting them to zero
    totalMean = 0
    rmsAverage1=0
    harmAverage=0

    ##Input: Number of terms and set of terms by user
    numOfTerms = eval(input("Enter the total number of terms in the set: "))
    for i in range (numOfTerms):

        ##find out terms in set
        numTotalMean=eval(input("Enter #" + str(i+1) + ": "))

        ##total mean
        totalMean = totalMean + numTotalMean

        ##mean squared
        rmsAverage1= rmsAverage1 +numTotalMean**2

        ##division of total mean
        harmAverage=harmAverage +(1/numTotalMean)

    ## average mean
    averageMean = totalMean/numOfTerms

    ##rms mean
    rmsAverage2= math.sqrt(rmsAverage1/numOfTerms)

    ##harmonic mean
    harmAverage2= numOfTerms/harmAverage

    ##output: average, rms, and harmonic all on to monitor
    print("RMS Mean: ", rmsAverage2)
    print("Harmonic mean: ", harmAverage2)
