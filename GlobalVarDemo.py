x = 101    
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x 
    #  
    x=100
    print(x)  
    # modifying a global variable  
   
    print(x) 
    
  
mainFunction()  
print(x) 