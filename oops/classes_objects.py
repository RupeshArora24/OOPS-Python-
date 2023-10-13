# empty class 
class empty_class:
       def __init__(self,age,name,address): 
        age=10
        print(age)
        print("I am ",name,"and my age is ",age,"and i live in",address)
#obj=empty_class(21,"Rupesh Arora","Nagpur")


class practice:
    #without default constructor.
    pass
#obj=practice()    

class practice1():
    # with constructor
    def __init__(self):
        pass
#obj1=practice1()

class practice2():
    def __init__(self):
        self.name="Rupesh Arora"
        print(self.name)
#obj3=practice2()        


class practice3():
    age=21
    def __init__(self):
        name="Rupesh Arora"
        print("I am ",name,"and my age is ",self.age)
#obj4=practice3() 

class practice4():
    # creating 2 default constructors
    def __init__(self):
        name="Rupesh Arora"
        print(name)

    def __init__(self):
        name="Rupesh Arora 123 "
        print(name)   

#obj5=practice4()

class practice5():
    # creating 2 default constructors
    def __init__(self):
        name="Rupesh Arora i am from default constructor."
        print(name)

    def show(self):
        name="Rupesh Arora i am from show method "
        print(name)   

#obj6=practice5()


class practice6():
    # using parametrized constructors
    def __init__(self,name,year):
     
        print(name," was born in ",year)

obj7=practice6("Rupesh Arora",2002)