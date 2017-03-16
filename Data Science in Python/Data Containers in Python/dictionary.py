capitals = {'United States': 'Washington, DC','France': 'Paris','Italy': 'Rome'}
capitals['Italy']
capitals['Spain'] = 'Madrid'
capitals
'Germany' in capitals
'Italy' in capitals
morecapitals = {'Germany': 'Berlin','United Kingdom': 'London'}
capitals.update(morecapitals)
capitals
del capitals['United States']
for key in capitals:
	print(key,capitals[key])

for key in capitals.keys():
	print(key)
for value in capitals.values():
	print(value)
for key,value in capitals.items():
	print(key,value)