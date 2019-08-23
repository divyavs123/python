def rev1(str1):
    li=str1.split(" ")
    li.reverse()
    print(li)
    return str1[::-1]

str1=raw_input("enter the string")
print(rev1(str1))
