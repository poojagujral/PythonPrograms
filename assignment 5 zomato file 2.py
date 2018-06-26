import json
file=open("C:\\Users\\POOJAGUJRAL\\Desktop\\PYTHON\\Zomato data\\file2.json", "r")
a=file.readlines()
b=json.loads(a[0])
file.seek(0)
m={}
for j in range (len(a)):
    for i in (b[j]['restaurants']):
        ar=i['restaurant']['user_rating']['aggregate_rating']
        v=i['restaurant']['user_rating']['votes']
        n=i['restaurant']['name']
        c=float(ar)*int(v)
        m[c]=n
print (m[max(m.keys())])
newlist=[]
for i in m.keys():
    newlist.append(i)
newlist.sort()
n2=[]
n2=newlist[::-1] #to reverse the list in descending order
for i in n2[:5:]:
    print(m[i])
