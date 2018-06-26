x=open("C:\\Users\\POOJAGUJRAL\\Desktop\\PYTHON\\Copy of datafile.csv","r")
z=x.readlines()
#print(z)
x.seek(0)
u=len(z)
#print(u)
p=list
q=dict()
y=0
for i in range(1,u-1):
    p=z[i].split(",")
    q[p[0]]=p[3]
    y+=int(p[3])    
name=input("enter the name")          
#print(q)
print("average = ",y/35)
for i in q:
    if(i==name):
        print(q[i])
