from scipy.interpolate import interp1d
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker

fig = plt.figure() 
ax = fig.add_subplot(111) 

x=np.array([5.54*10**14, 5.37*10**14, 5.2*10**14, 5.03*10**14, 4.84*10**14, 4.64*10**14, 4.46*10**14, 4.25*10**14, 4.03*10**14,3.8*10**14])
y=np.array([5.875,5.5,5.25,5,4.5,3.75,3.25,2.5,1.125,0])

def lagranz(x,y,t):
    z=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1; p2=p2*1   
            else: 
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z
xnew=np.linspace(np.min(x),np.max(x),1)
ynew=[lagranz(x,y,i) for i in xnew]
plt.errorbar(x, y, xerr=0.3*10**14., yerr=0.25, c='navy', marker='.', ms=5, fmt='o')
#plt.plot(x,y,'-',xnew,ynew, color='crimson')
plt.axis([2*10**14,6*10**14, 0, 7])
plt.grid(color="steelblue", which="major", linestyle='-', linewidth=0.7)
plt.grid(color="grey", which="minor", linestyle=':', linewidth=0.5)
plt.ylabel('$V_з$,В')
plt.xlabel('частота,Гц')
plt.minorticks_on()
plt.title('Зависимость $V_з$ от частоты света')
plt.savefig('z3.pdf',dpi=300)
plt.show()
