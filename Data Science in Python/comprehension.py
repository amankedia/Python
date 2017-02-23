squares = []
for i in range(10):
	squares.append(i**2)
squares
squares = [i**2 for i in range(10)]
squares
squares = [i**2 for i in range(10) if i % 3 == 0]
squares
squares_dict = {i: i**2 for i in range(30) if i % 3 == 0}
squares_dict
sum([i**2 for i in range(10)])
