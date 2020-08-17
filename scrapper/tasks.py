import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
import os

def task_1():
	
	if os.path.exists('movie_list.json') :
			with open('movie_list.json','r') as file:
				new=json.load(file)
				# pprint(new)
				return new

				
	else:

		url=' https://www.imdb.com/india/top-rated-indian-movies/'
		a=requests.get(url)
		htmlContent=a.content
		soup=BeautifulSoup(htmlContent,'html.parser')
		td=soup.find('tbody',class_="lister-list")
		tr = td.find_all('tr')
		li=[]
		h=[]
		# dic={}
		cou=1
		for i in tr:
			td = i.find_all('td')
			count = 0
			pos=1			
			if count==0:
				movies_name = (td[1].a.get_text())
				year =(td[1].span.text)
				ch=(year[1:5])
				pr=(int(ch))

				lk='https://www.imdb.com/'
				link=(lk+td[1]. a['href'])

				rat=(td[2].strong['title'])
				cha=(rat[0:3])
				fl=(float(cha))

				
				dic={'link':link,'movies':movies_name,'years':pr,'ratings':fl,'position':cou}
				cou+=1
				li.append(dic)

		
		op=open('movie_list.json','w+')
		ds=json.dump(li,op)
		op.close()
		ap=open('tasks.json','r+')
		js=json.load(ap)
	
				
			
task_1()

