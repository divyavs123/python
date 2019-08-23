def search(lis,a):
    print(lis)
    if a in lis:
        return True
    else:
        return False
    
lis=[]
n=int(input("enter the number of  values"))
while len(lis)!=n:
    
    a = int(input("Enter the values"))
    if a!= -1 :
        lis.append(a)
    else:
        break
b=input("Enter the element to be searched")
print(search(lis,int(b)))
