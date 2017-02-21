""" A Functional Breakfast """

cheese = 'cheddar'

def mix_and_cook():
    print('Mixing the ingredients')
    print('Greasing the frying pan')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')
    
def make_omlette(ingredient):
    mix_and_cook()
    omelette = 'a {} omelette'.format(ingredient)
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a delicious pancake'
    return pancake

def make_pizza():
    mix_and_cook()
    pizza = 'a {} pizza'.format(cheese)
    return pizza

def make_lasagna():
    global cheese
    cheese = 'swiss'
    mix_and_cook()
    lasagna = 'a {} pizza'.format(cheese)
    return lasagna

def make_pasta():
    mix_and_cook()
    pasta = 'a {} pizza'.format(cheese)
    return pasta

def fancy_omlette(*ingredients):
    mix_and_cook()
    omelette = 'a fancy omelette with {} ingredients'.format(len(ingredients))
    return omelette

omlet1   = make_omlette('cheese')
pancake1 = make_pancake()
