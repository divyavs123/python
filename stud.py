class University:
        def __init__(self):
                stu_id=age=marks=0
        def validate_marks(self):
                if(self.marks>0 and self.marks<=100):
                        return True
                else:
                        return False
        def validate_age(self):
                if(self.age>20):
                        return True
                else:
                        return False

        def check_qualification(self):
                if(self.validate_marks() and self.validate_age()):
                        if(self.marks>65):
                                return True
                        else:
                                return False
                else:
                        return False
        def setter_method(self,sid,a,m):
                self.stu_id=sid
                self.age=a
                self.marks=m
        def getter_method(self):
               
                if u1.check_qualification():
                         print("Given informatin are valid")

                         print("id:",self.stu_id)
                         print("Age:",self.age)
                         print("Marks:",self.marks)
                else:
                        print("Information are invalid")
                

n=int(input("Enter the no. of students:"))
for i in range(0,n):
      u1=University()
      sid=int(input("Enter the sid:"))
      age=int(input("Enter the age:"))
      marks=int(input("Enter the marks:"))
      u1.setter_method(sid,age,marks)
      u1.getter_method()
