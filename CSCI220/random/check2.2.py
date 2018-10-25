def calcValues1(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]+10
def calcValues2(nums):
    values=[]
    for num in nums:
        values.append(num*2)
    print(values)

def main():
    numbers=[7,3,5]

    print(numbers)
    calcValues1(numbers)
    print(numbers)

    totals=calcValues2(numbers)
    print(numbers)
    print(total)
