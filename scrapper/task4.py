from tasks import task_1
from bs4 import BeautifulSoup
from pprint import pprint as pp
import requests
import os,json	

def movies_data(movies):

	if os.path.exists('tasks_four.json') :
			with open('tasks_four.json','r') as file:
				new=(json.load(file))
				# pp(new)
				return new
	else:
		main_link=[]
		count=1
		count_1=1
		li=[]
		for data in (movies):
			names=(data['movies'])
			url=(data['link'])
			main_link.append(url)
			req=requests.get(url)
			htmlContent=req.content
			soup=BeautifulSoup(htmlContent,'html.parser')
			links=soup.find_all('div',class_='credit_summary_item')
			co=soup.find_all('div',class_='txt-block')
			run=soup.find_all('div',class_='subtext')
			image=soup.find_all('div','poster')
			bio=soup.find_all('div',class_='summary_text')
			gen=soup.find_all('div',class_='subtext')
			copy=[]
			for linked_data in links:
				diric=linked_data.find_all('h4',class_='inline')
				for j in diric:
					if 'Director:' in j.get_text():
						diri=([linked_data.a.get_text()])
			for Country_name in co: 
				con=Country_name.find_all('h4',class_='inline')
				for m in con:
					if 'Country:' in m.get_text():
					 	countr=(Country_name.a.get_text())
					if 'Language:' in m.get_text():
						lang=([Country_name.a.get_text()])
			sam=(soup.find_all("time"))
			runtime=sam[0].get_text()
			copy.append(runtime)			
			ist_one=(runtime[25])
			ist=(int(ist_one))
			second_one=(runtime[28:])
			going_to_done=(second_one.replace('min',''))
			done_2=ist*60
			for im in image:
				poster=(im.img['src'])
			for bi in bio:
				biography=(bi.get_text())
				kar=(biography.strip())	

			for genr in gen:
					kop=genr.find_all('a')
					sab_kuch=[]

					for  p in kop:
						sab_kuch.append(p.get_text())	
					last_one=(sab_kuch)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																				
					hiu=genr.find_all('a',title='See more release dates')
					for k in hiu:
						last_2=(k.get_text())
					if last_2 in last_one:
						last_one.remove(last_2)
					done=last_one
					
			if 'min' not in runtime:
				done_1=done_2
			else:
				nice=(int(going_to_done))
				done_1=(ist*60+nice)
			count_1+=1
			dict_last_1={'position':count,'movie-name':data['movies'],'Director':diri,'country':countr,'language':lang,'runtime':done_1,'poster_image_url':poster,'biography':kar,'Genre':done}
			count+=1
			li.append(dict_last_1)
		pp(li)



		ope=open('tasks_four.json','a')
		opening=json.dump(li,ope,indent=4)
		ope.close()
		ap=open('tasks_four.json','r+')
		js=json.load(ap)
movies_data(task_1())

