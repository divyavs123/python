class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
str1=input("Enter the string:")
print(py_solution().is_valid_parenthese(str1))
str2=input("Enter the string:")
print(py_solution().is_valid_parenthese(str2))

