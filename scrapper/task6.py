from task4 import movies_data
from task4 import task_1
from pprint import pprint as pp
def my_fun_6(movies_dat):
	p=[]
	m=[]
	for i in (movies_dat):
		a=(i['language'])
		for j in a:
			m.append(j)
			if j not in p:
				p.append(j)
	bol=[]
	last_count=0
	for tr in p:

		veer=m.count(tr)
		print(tr,':::',veer)
		last_count+=veer
	print('their count is :::',last_count)
my_fun_6(movies_data(task_1()))