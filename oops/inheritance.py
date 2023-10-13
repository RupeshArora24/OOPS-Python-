class Father:
    def Land(self):
        print("i have 20 lakh carore of land and i am father")

class Son(Father):
    def me_and_fathers_land(self):
        print("i have 20 crores crorse of land and i a am son ")        

#papa= Father()
#papa.Land()
#papa.me_and_fathers_land()
#child object        

class GreatGrandFather:
    txt="ham dada kae bhi dada hai tumhare"
class GrandFather(GreatGrandFather):
    txt1="dadaji bol dadaji"
    def method(self):
     print("ham to dada hai tumharee par hammare dada yae bolte hai ki = ",self.txt)
  
class Father(GrandFather):
    def method1(self):
        print("mae bapp hu tumhara and my ansistors says = ",self.txt1,self.txt)
#Fa = Father()
#Fa.method()
#Fa.method1()

class emp1:
   def frontend(self):
    print("done with my frontend work")
class emp2:
    def backend(self):
     print("hey team lead done with my backend work")
class teamlead(emp1,emp2):
    print("i will verify your work of both")       
obj111=teamlead()
obj111.frontend()
obj111.backend()    
