import json

f= open("C:\\Users\\POOJAGUJRAL\\Desktop\\PYTHON\\json sample file down for assign 3", "r")

g=f.readlines()[0]

whole_data=json.loads(g)
print(whole_data)

counts={} #create dict
sum=0
x=whole_data['data'] #to access data of object

for i in range(0, len(x)):
    state=x[i][0]
    total=x[i][3]
    #sum+=int(total)
    counts[state]=total

state= input('enter state: ')
print('The value is : ', total, 'The average is: ', sum/len(x))

