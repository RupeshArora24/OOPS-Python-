#here we are makeing the variables private and protected which in turn is the example d
#of encapsulatin where we are trying to make the variable restricted.
class A: 
    _a=10  #Protected where variable can access both object and function 
    __b=20  # Private - here variable can access only function
    #below we are creating a method
    def Show(self):
       print(self._a+self.__b)
obj=A() #object of class A
obj.Show()   
print("can we print the varibale with the protected restriction ? \n ", A._a)

print("can we print the varibale with the private restriction ? \n ", A.__b)

