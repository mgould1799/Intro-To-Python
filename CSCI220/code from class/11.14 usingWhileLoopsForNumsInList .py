##while loop allows you to leave once you find what you are looking for


##linear search algorithm 
#stop i>=len(values) or values[i] == search val
def find(values, searchVal):
    i=0
    while i < len(values) and values[i]!=searchVal:
        i+=1
    if i == len(values):
        i=-1
    return i 

##seachVal i      searchVal  i
## s       0           g     0
##         1                 1
##         2                 2
#          3                 3
#          4                 4
#                            5
#                            6
# when the loop finds the item i == position of the item
# when i == len(values) -> values not there
##List = m k d a s t b 

#for loop solution would not stop when item searched for is found- always going
##    through n times regardless if found or not found
## while loop stops once item is found or no more data to search
## best case for while loop: O(1) big oh of one-> searchVal in first postion of list
## worst case for while loop: O(n) big oh of n(complexitity)-> when item not in
#       in list or item in last element of list 
