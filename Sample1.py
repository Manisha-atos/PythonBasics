'''l1=[1,2,3,4]
for x in range(len(l1)):
    l1[x]=l1[x]*2
    print(x+"="+l1[x]);
print(l1)'''

for i in range(1,4):
    print("i=%d" %i)
    for j in range(1,4):
        if(j==2):
            break;
        print("j=%d"%j);


        
