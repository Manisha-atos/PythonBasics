a=[11,32,3,4]
b=[1,"apple",3.3]
print(a)
print(b)
print(type(a))
print(type(b))
emp = [ "John", 102, "USA"] 
print(" Name : %s, ID: %d, Country: %s" %(emp[0], emp[1], emp[2]))     
a=[1,2,3,4,5]
#list slising
print(a[1:4])  
#list in backward order  
print(a[-1])    
print(a[-3:])    
print(a[:-1])    
print(a[-3:-1])  
#updating list 
a[3]=101
print(a) 

a[1:3]=[10,20]
print(a)