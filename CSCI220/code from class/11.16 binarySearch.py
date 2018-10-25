##11.14 contains linear search
#binary search, split list in half and compare those two halves and keep diviving
#   in half until find it or do not find it. data must be sorted to do this
##can guess in seven guesses because 2**7>100 and 2**6!=100
## the bigger the num more efficient a binary search is
## if num is between 1 and mil , guess takes at most 20 times
## linear search 1 mil items
#   worst case: 1 mil (item not in list or at bottom) big oh of n
#   best case: 1 big oh of 1
##1 mill items:
##binary search
#   best case:1 (num exactly in the middle) big oh of 1
#    worse case:20 big oh logn (base of 2)
##log1000 = what num can you raise 2**x and get something bigger than a 1000
##  base of 2
##log3000-> 12
#log100000->17
#log4->3

##[ant apple bird cat dog frog giraffe hourse kangaroo]
##0    1       2    3  4    5    6       7      8
##searchVal  low        high       mid    foundPos        high=len(values)-1
##"cat"       0          8          4 <
##            0          3          1 >
##            2          3          2 >
##            3          3          3 =       3

##"horse"     0          8          4 >
##            5          8          6 >
##            7          8          7 =       7

##"frog"      0          8          4 >
##            5          8          6 <
##            5          5          5 =       5

##"aorta"     0          8          4 <
##            0          3          1 <
##            0          0          0 >                  low adjust when using >
##            1          0                   -1
# when low is greater than high then you know it is not in the list

low=0
high=len(values)-1
mid=(low+high)//2
while low<=high and values[mid]!=searchVal:
    if searchVal< values[mid]:
        high=mid-1
    else:
        low=mid+1
    if low<=high:
        found=mid
    else:
        found=-1
