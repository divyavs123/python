list=[]
n=int(input("Enter the elements:\n"))
for i in range(0,n):
        element=int(input())
        list.append(element)
print(list)
for i in list:
  newlist=[]
  if(i%2==0):
          newlist.append(i)
print(newlist)
