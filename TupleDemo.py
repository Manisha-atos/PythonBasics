# Python program to show how to create a tuple    
# Creating an empty tuple    
empty_tuple = ()    
print("Empty tuple: ", empty_tuple)    
    
# Creating tuple having integers    
int_tuple = (4, 6, 8, 10, 12, 14)    
print("Tuple with integers: ", int_tuple)    
    
# Creating a tuple having objects of different data types    
mixed_tuple = (4, "Python", 9.3)    
print("Tuple with different data types: ", mixed_tuple)    
    
# Creating a nested tuple    
nested_tuple = ("Python", {4: 5, 6: 2, 8:2}, (5, 3, 5, 6))    
print("A nested tuple: ", nested_tuple)    

# Python program to create a tuple without using parentheses    
# Creating a tuple    
tuple_ = 4, 5.7, "Tuples", ["Python", "Tuples"]  
print("Elements between indices 1 and 3: ", tuple_[1:3])    
# Using negative indexing in slicing    
print("Elements between indices 0 and -4: ", tuple_[:-4])     
#del tuple_[3] 
# Displaying the tuple created    
print(tuple_)    
# Checking the data type of object tuple_    
print(type(tuple_) )    
# Trying to modify tuple_ 
t1=(1,2,2,5,3,3,3,3)   
print(t1*3)
print(t1.count(3))
print(t1.index(5))
try:    
    tuple_[1] = 4.2    
except:    
    print(TypeError )    