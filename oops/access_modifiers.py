class practice_1:
    a=10 #public
    _b=20 #protected
    __c=None #private
    print("we are accessing all the 3 variables in same class",a,_b,__c)
    def Add(self):
        self.__c=self._b + self.a
        print("(here we are accesing all the 3 variables in same method within the class)Addition : ",self.__c)
#obj=practice_1()
#obj.Add()
#print("Here we are accessing all the 3 variables outside of the class",obj.a,obj._b,obj.__c)

class practice_2:
    # which acccess modifiers can get accessed in different classes.
    def Show(self):
      print("i got acccessed in different class ",practice_1.a)
      print("i got acccessed in different class ",practice_1._b)
      print("i got acccessed in different class",practice_1.__c)

obj_practice_2 = practice_2()      
obj_practice_2.Show()