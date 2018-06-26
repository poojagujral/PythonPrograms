a = open("C:\\Users\\POOJAGUJRAL\\Desktop\\PYTHON\\dataset for assignment 2.csv",'r')

b = a.readlines()
a.close()

d={}
#print(b)
for i in b:
    #print(i)
    d[i.split(',')[0]] = i.split(',')[3]
    print(i.split(','))

u = (input('Enter the State name--> '))
'''for i in c:
        d[i[0]]=i[3]'''

print(d[u])
z = input()
