num=int(input("Enter the no. to find divisor::"))
div=[]
for i in range(1,num):
        if(num%i==0):
                div.append(i)
print(div)                
