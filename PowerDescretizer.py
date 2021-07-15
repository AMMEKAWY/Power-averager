import math


mu=10000
xi=0
xf=18
n=(math.sqrt((xf-xi)**2)/(18*mu-1))
x=[xi]
y=[]
i=0
j=0
mean=[]
k=5
t=0
q=mu-1


#----------------Define the function--------------
def f(x):
    return x**2

#-----------------Building the x axis-------------
while x[i] < xf:
    x.append(round((x[i]+n),4))
    i+=1
x.append(xf)
del(x[-1])
#-----------------Building the y axis-------------
while len(y) != len(x):
    y.append(round(f(x[j]),4))
    j+=1
#------------------calculating the average---------
def mn(t,i):
    return y[t+i]


while (t+i-mu) != 18*mu  :
    i=0
    m=0
    while i != mu:
        #print(t+i)
        m=m+mn(t,i)
        i+=1
    mean.append(round(m/mu,4))
    t+=mu

#-----------------PRINTING RESULTS-------------------
j=0
while j != len(mean):
    print(mean[j])
    j+=1

