import csv
d = {}
i=0
c=0
with open('C:\\Users\\POOJAGUJRAL\\Desktop\\PYTHON\\mmt data\\makemytrip_com-travel_sample.csv','r',encoding='utf-8') as csvfile:
	read = csv.reader(csvfile,delimiter=',',quotechar='"')
	for row in list(read):
		try:
			c+=1
			city = row[1]
			
			name = row[22]
			mmt = row[16] #mmt_review_ score
			trip = row[18]#mmt_tripadvisor_count
			
			rating = int(trip)*float(mmt)
			if city not in d:
				d[city] = {}
			d[city][rating] = name
		except:
			continue

for i in list(d):
	top =[]
	keys = list(d[i].keys())
	keys = sorted(keys,reverse=True)
	print('-----------------------------------------\nFor',i,':\n','\nTotal Hotels: ',len(keys),'\nBest Hotel:',d[i][keys[0]])

	try:
		for j in range(5):
			top.append(d[i][keys[j]])
		print('\nTop 5 Hotels in order of their ranks:\n',top)
	except:
		print('\nTop',len(top),'Hotels order of their ranks:\n',top)
		continue
#print("\nTotal Hotels: ",c)
z = input()