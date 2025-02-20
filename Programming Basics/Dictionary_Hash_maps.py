""" A Rolodex Full of Friends """

# dictionary of name/number pairs
rolodex = {'Aaron'  : 5556069,
           'Bill'   : 5559824,
           'Dad'    : 5552603,
           'David'  : 5558331,
           'Dillon' : 5553538,
           'Jim'    : 5555547,
           'Mom'    : 5552603,
           'Olivia' : 5556397,
           'Verne'  : 5555309}


# look for Amanda (not in rolodex)
# print(rolodex['Amanda']) # causes an error

# add Amanda to the rolodex
rolodex['Amanda'] = 5559754
print(rolodex['Amanda'])

# overwrite David's number
print(rolodex['David'])
rolodex['David'] = 5550902
print(rolodex['David'])

# store a tuple with both numbers
rolodex['David'] = (5558331,5550902)
print(rolodex['David'])

# store each David's number with a unique key
rolodex['David'] = 5558331
rolodex['David (Amanda)'] = 5550902
print(rolodex['David'])
print(rolodex['David (Amanda)'])
print(rolodex)



""" A Rolodex Full of Friends """

# dictionary of name/number pairs
rolodex = {'Aaron'  : 5556069,
           'Bill'   : 5559824,
           'Dad'    : 5552603,
           'David'  : 5558331,
           'Dillon' : 5553538,
           'Jim'    : 5555547,
           'Mom'    : 5552603,
           'Olivia' : 5556397,
           'Verne'  : 5555309}

def caller_id(lookup_number):
    for name, num in rolodex.items():
        if num == lookup_number:
            return name

# reverse-lookup Olivia's number
print(caller_id(5556397))

# reverse-lookup a number not in the rolodex
print(caller_id(8675309))

# reverse-lookup number for Dad & Mom
print(caller_id(5552603))

