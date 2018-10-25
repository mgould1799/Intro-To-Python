#in square search
#selection sort. n**2 complexity
#100 items unsorted = 100**2 comparisons

##1000 unsorted items
## linear: worst case 1000 comparisons
##binary:
#       first have to sort-> bigOh(n**2)=1 mil comparisons
#       then i can search -> bigOh(logn)=10 camparisons
##if info needed quickly, sort before the assignment. also, because of lots of
##      searches needed

##bubble sort push largest to the bottom
##  for all of the items in the list compare 2 items and swap if needed
##  for all items in list:
##      for all items in list:
##          compare 2 items
##          swap if needed
##bubble sort is a partial list?
##nested for loop for this.
## O(n**2) for complexity .

#partial sort
#selection sort
for front from(0.len(values)-1):
    for all the other items:
        find position of smallest item
    swap smallest item with the front
