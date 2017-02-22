nephews = ["Huey","Dewey","Louie"]
nephews
nephews[0]
nephews[2]
len(nephews)
nephews[3] #error

for i in range(3):
	nephews[i] = nephews[i] +  ' Duck'
nephews
mix_it_up = [1,[2,3],'alpha']
mix_it_up
nephews.append('April Duck')
nephews
nephews.extend(['May Duck','June Duck'])
nephews
ducks = nephews + ['Donald Duck','Daisy Duck']
ducks
ducks.insert(0,'Scrooge McDuck')
ducks
del ducks[0]
ducks
ducks.remove('Donald Duck')
ducks
ducks.sort()
ducks
squares = [0,1,4,9,16,25,36,49]
squares
squares[0:2]
squares[:3]
squares[:]
squares[-1]
squares[-3:-1]
squares[0::2]
for value in squares:
	print("Element",value)

for index, value in enumerate(squares):
	print("Element",index,"-> ",value)
