fav_films=['intersteller','matrix','the conjouring']
fav_films.append('the nun')
def check_ticket(age,has_ticket):
	if age>=18 and has_ticket==True:
		print('enjoy the ',fav_films,'films')
	else: 
		print("acess denied , you can't enter")
		
check_ticket(13,False)
