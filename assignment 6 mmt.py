import csv
globallist=[]
with open('C:\\Users\\POOJAGUJRAL\\Desktop\\PYTHON\\mmt data\\makemytrip_com-travel_sample.csv', 'r', encoding="UTF-8") as csvfile:
    read= csv.reader(csvfile, delimiter=',', quotechar='"') #delimiter is splitting element and quotechar does not split
    for row in read:
        globallist.append(row)

d={}
for i in range(len(globallist)):
    try:
        d[globallist[i][22]] = float(globallist[i][16])*float(globallist[i][18])
    except:
        d[globallist[i][22]]=0

a1=[]
a2=[]
a3=[]
for value in d.values():
    a1.append(value)
a1.sort(reverse=True)

a2=a1[:5:]
for i in a2:
    for j in d.keys():
        if d[j]==i:
            a3.append(j)
for i in range (len(a3)):
    print(a3[i]+" "+str(a2[i]))
