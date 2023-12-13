#1 class defintion


class car: # pasclecase
   #1.1 property = variable
   brand="TATA"
   model="2024" # variable

   #1.2 constructor



   #1.3 method = functions
   def getMyBrand(self): # camlecase 
       # self is internal class object 
       print(f"Brand is {self.brand}")
       print(f"model year is {self.brand}")
       pass

   pass    
#2 create class object
# classobject = classname()
#co is exteranal class object
co = car()        

# call the method with classobjectcls
co.getMyBrand()