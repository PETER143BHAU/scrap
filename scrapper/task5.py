from tasks import task_1
from bs4 import BeautifulSoup
from pprint import pprint as pp
import requests
import os,json	
again_list=[]

def movies_data(movies):
	# if os.path.exists('task_4.json'):
	# 	ope=open('task_4.json','r')
	# 	lo=ope.read()
	# 	print(lo)

		# ope.close()
	# else:
	final_list=[]
	main_link=[]
	count=1
	final=[]
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
		for linked_data in links:
			diric=linked_data.find_all('h4',class_='inline')
			for j in diric:
				if 'Director:' in j.get_text():
					diri=([linked_data.a.get_text()])
		for Country_name in co: 
			con=Country_name.find_all('h4',class_='inline')
			li=[]
			for m in con:
				if 'Country:' in m.get_text():
				 	countr=(Country_name.a.get_text())
				if 'Language:' in m.get_text():
					lang=([Country_name.a.get_text()])
		sam=(soup.find_all("time"))
		runtime=sam[0].get_text()
		ist_one=(runtime[25])
		ist=(int(ist_one))
		second_one=(runtime[28:])
		# print(second_one)
		going_to_done=(second_one.replace('min',''))
		nice=(int(going_to_done))
		done_1=(ist*60+nice)


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
				dict_last={'position':count,'movie-name':data['movies'],'Director':diri,'country':countr,'language':lang,'runtime':done_1,'poster_image_url':poster,'biography':kar,'Genre':done}
				pp(dict_last)
				again_list.append(dict_last)
				count+=1
		pp(again_list)


				
		# opened=open('tasks_five.json','a')
		# po=json.dump(dict_last,opened,indent=3)
		# opened.close()		
movies_data(task_1()[0:10])