def cumulative_product(numlist):
    product=1
    cp=[]
    for ele in numlist:
        product=product*ele
        cp.append(product)
    return cp

numlist=[]
n=int(input("Enter number of elements to be insert:"))
for i in range(n):
    ele=int(input("Enter element:"))
    numlist.append(ele)
cp=cumulative_product(numlist)
print("Cumulative product of list elements is ",cp)
