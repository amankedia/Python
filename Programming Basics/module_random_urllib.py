import random
print(random.randint(1,20))
#randint(1,20) #error
from random import randint
print(randint(1,20)) #now no error
from random import random #random is a method in random package
random()
#print(randint(1,20)) #would give error as random now referes to method
#to resolve use following
import random as rand
print(rand.randint(1,100))
import urllib.request
urllib.request.urlopen('http://www.google.com')
urllib.__path__
