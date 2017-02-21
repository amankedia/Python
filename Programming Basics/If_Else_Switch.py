""" Ordering A Pizza That Verne Can Eat """

# things that Verne does not eat
diet_restrictions = set(['meat','cheese'])

# decide which pizza to order      
if 'meat' and 'cheese' in diet_restrictions:
    print('Get a vegan pizza.')

elif 'meat' in diet_restrictions:
    print('Get a cheese pizza.')
    
else:
    print('Get something else.')


""" Switch """

specials = {'Sunday'    : 'spinach', 
            'Monday'    : 'mushroom', 
            'Tuesday'   : 'pepperoni', 
            'Wednesday' : 'veggie',
            'Thursday'  : 'bbq chicken',
            'Friday'    : 'sausage',
            'Saturday'  : 'Hawaiian'}

def order(day):
    pizza = specials[day]
    print('Order the {} pizza.'.format(pizza))

# order the Saturday special!
order('Saturday')
