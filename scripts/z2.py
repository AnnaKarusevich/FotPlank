import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker

fig = plt.figure() 
ax = fig.add_subplot(111) 

# def f(x): #x— градусы 
# 	p1 =-3.668*10**(7) 
# 	p2=-9.329*10**(9) 
# 	p3 =7.457*10**(14) 
# 	f = p1*x**2 + p2*x + p3 
# 	return f 
# x=np.arange(200,3500,1) 
x=np.array([2.50*10**14, 2.70*10**14, 2.90*10**14, 3.10*10**14, 3.25*10**14, 3.40*10**14, 3.54*10**14,	3.68*10**14, 3.80*10**14, 3.92*10**14, 4.03*10**14, 4.14*10**14, 4.25*10**14, 4.36*10**14, 4.46*10**14, 4.55*10**14, 4.64*10**14, 4.73*10**14, 4.84*10**14, 4.93*10**14, 5.03*10**14, 5.11*10**14, 5.20*10**14, 5.28*10**14, 5.37*10**14, 5.45*10**14, 5.54*10**14, 5.63*10**14
])
y=np.array([2,5,11.5,18.5,23,24.5,24,22,19.5,17,15,12.5,10.5,8.5,7,6,5,4,3.5,3,2.7,2.5,2.2,2,1.9,1.7,1.6,1.5])
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
plt.errorbar(x, y, xerr=0.02*10**14., yerr=0.5, c='navy', marker='.', ms=5, fmt='o')
plt.plot(x,y,'-',xnew,ynew, color='crimson')
plt.axis([0,6*10**14, 0, 30])
plt.grid(color="steelblue", which="major", linestyle='-', linewidth=0.7)
plt.grid(color="grey", which="minor", linestyle=':', linewidth=0.5)
plt.ylabel('J,mA')
plt.xlabel('частота,Гц')
plt.minorticks_on()
plt.title('Зависимость тока фотоэлемента от частоты света')
plt.savefig('z2.pdf',dpi=300)
plt.show()



x=np.array([2.51*10**-14, 2.33*10**-14, 2.17*10**-14, 2.03*10**-14, 1.93*10**-14, 1.85*10**-14, 1.77*10**-14, 1.71*10**-14, 1.65*10**-14, 1.60*10**-14, 1.56*10**-14, 1.52*10**-14, 1.48*10**-14, 1.44*10**-14, 1.41*10**-14, 1.38*10**-14, 1.35*10**-14, 1.33*10**-14, 1.3*10**-14, 1.27*10**-14, 1.25*10**-14, 1.23*10**-14, 1.21*10**-14, 1.19*10**-14, 1.17*10**-14, 1.15*10**-14, 1.13*10**-14, 1.12*10**-14
])
y=np.array([2,5,11.5,18.5,23,24.5,24,22,19.5,17,15,12.5,10.5,8.5,7,6,5,4,3.5,3,2.7,2.5,2.2,2,1.9,1.7,1.6,1.5])
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
plt.errorbar(x, y, xerr=0.02*10**-14., yerr=0.5, c='navy', marker='.', ms=5, fmt='o')
plt.plot(x,y,'-',xnew,ynew, color='crimson')
plt.axis([0,6*10**-14, 0, 30])
plt.grid(color="steelblue", which="major", linestyle='-', linewidth=0.7)
plt.grid(color="grey", which="minor", linestyle=':', linewidth=0.5)
plt.ylabel('J,mA')
plt.xlabel('частота,Гц')
plt.minorticks_on()
# plt.title('Зависимость тока фотоэлемента от частоты света')
# plt.savefig('z2.pdf',dpi=300)
plt.show()
