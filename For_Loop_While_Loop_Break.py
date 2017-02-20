""" Loading the Dishwasher """
#For Loop

# dirty dishes in the sink
sink = ['bowl','plate','cup']

for dish in list(sink):
    print('Putting {} in the dishwasher'.format(dish))
    sink.remove(dish)

# check that the sink is empty
print(sink)

""" Scrubbing A Stuborn Pan """
#While Loop

import random

dirty = True # state of the pan
scrub_count = 0 # number of scrubs

while(dirty):

    scrub_count += 1
    print('Scrub the pan: {}'.format(scrub_count))
    
    if not random.randint(0,9):
        print('All clean!')
        dirty = False
    else:
        print('Still dirty...')  

    print('Rinse & check if the pan is clean.') 


""" Putting Away Clean Dishes """
#Break Statement

import random

# 20 clean dishes in dishwasher
dishwasher = ['plate','bowl','cup','knife','fork',
              'spoon','plate','spoon','bowl','cup',
              'knife','cup','cup','fork','bowl',
              'fork','plate','cup','spoon','knife']

for dish in list(dishwasher):

    # check space left in cabinet
    if not random.randint(0,19):
        print('Out of space!')
        break
    else:
        print('Putting {} in the cabinet'.format(dish))
        dishwasher.remove(dish)
