# Example input list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get list length
L = len(numbers)

# i goes from 0 to the middle
for i in range(int(L/2)):
    # Swap each number with the number in 
    # the mirror position for example first 
    # and last
    n = numbers[i]
    numbers[i] = numbers[L-i-1]
    numbers[L-i-1] = n

# At this point the list should be reversed
print(numbers)



def myfunc(a):
    rev_str = []
    for x in a:
        rev_str.insert(0, x)
    return rev_str
print(myfunc([1,2,3,4,5,6,7,8,9,10]))
