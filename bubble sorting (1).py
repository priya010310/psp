List=[]
n=int(input("Enter the number of elements"))

for i in range(n):
    a=int(input("Enter the element"))
    List.append(a)

for i in range(n-1):
    for j in range(n-i-1):
        if (List[j]>List[j+1]):
            l=List[j]
            List[j]=List[j+1]
            List[j+1]=l
        
print(List)