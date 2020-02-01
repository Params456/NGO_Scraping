import requests,pprint,json,os
from bs4 import BeautifulSoup

if os.path.exists("Ngo.json"):
	with open("Ngo.json","r") as thaman:
		aa=json.load(thaman)
		name=json.loads(aa)
	pprint.pprint(name)
	dict2=name

else:
	a=requests.get("https://www.giveindia.org/certified-indian-ngos")
	soup=BeautifulSoup(a.text,"html.parser")
	table=soup.find("table",class_="jsx-697282504 certified-ngo-table")
	tr=table.findAll("tr",class_="jsx-697282504")
	name=[]
	states=[]
	for i in range(1,len(tr)):
		total=[]
		state=tr[i].findAll("td",class_="jsx-697282504")
		total=[j.text for j in state]
		name.append(total[0])
		states.append(total[2])	
	pprint.pprint(name)
	pprint.pprint(states)
	states2=set(states)
	dict2={r:[name[j] for j in range(len(name)) if r==states[j]] for r in states2}
	pprint.pprint(dict2)
	
	with open("Ngo.json","w+") as thaman:
		name=json.dumps(dict2)
		name=json.dump(name,thaman)

Input=input("Enter the state: ")
for l in dict2:  
	if Input==l:
		pprint.pprint(dict2[l])





	# dict1={}
	# for r in states2:
	# 	list1=[]
	# 	for k in range(len(states)):
	# 		if r==states[k]:
	# 			list1.append(name[k])
	# 	dict1[r]=list1
	# pprint.pprint(dict1)	
	# Input=input("Enter the state: ")
	# for l in dict1:
	# 	if Input==l:
	# 		pprint.pprint(dict1[l])