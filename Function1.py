def function1():
    print('hello')
    print('welcome')
    a=[1,2,3,3]
    print(a)
    b=(1,2,3)
    print(b)
    c={1,2,2,3}
    print(c);

def add(a,b):
    return a+b;
#default argument
def function( n1, n2 = 20 ):    
    print("number 1 is: ", n1)    
    print("number 2 is: ", n2) ;
def required(n1,n2):
    print("n1: ",n1)
    print("n2: ",n2);

     


function1()
print(add(2,2))
function(1);
#keyword argument 
function(n2=100,n1=0)
required(3,3)
required(5) #raise an error


