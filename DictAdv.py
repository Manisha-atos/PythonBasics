Employee = {"Name": "Johnny", "Age": 32, "salary":26000,"Company":"^TCS"}        
print(type(Employee))   
k=Employee.keys()
print(k)
v=Employee.values()
print(v)
print(Employee.get("Age"))
Employee.pop("Age")
print(Employee)