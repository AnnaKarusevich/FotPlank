import numpy as np
from functions import parsing
import csv
import matplotlib.pyplot as plt 
name='rec\\2500.tsv'
x,y=parsing(name,0,1)
# plt.plot(x,y,'b')
plt.plot(x,y,'ro')
a =  4435 
b = -223
f=a*x**2+b*x
plt.plot(x,f)
plt.ylabel('$J$,мА',fontsize=12) 
plt.xlabel('$I(d^2)$, у.е.',fontsize=12) 
plt.grid () 
plt.savefig('2500.pdf')
plt.show()
