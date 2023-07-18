Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)    
print(type(Days))    
print("looping through the set elements ... ")    
for i in Days:    
    print(i)    

# Empty curly braces will create dictionary  
set3 = {}  
print(type(set3))  
  
# Empty set using set() function  
set4 = set()  
print(type(set4))  

set5 = {1,2,4,4,5,8,9,9,10}  
print("Return set with unique elements:",set5)  
print(len(set5))
set5.discard(14)
print(set5)