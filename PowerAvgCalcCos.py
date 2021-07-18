import math

no=25          #THE NUMBER OF AVERAGES
mu=10000
xi=-100       #INITIAL X
xf=100           #FINAL X
n=(math.sqrt((xf-xi)**2)/(no*mu-1))
x=[xi]
y=[]
i=0
j=0
mean=[]
k=5
t=0
q=mu-1
ex=[xi]


#----------------Define the function--------------
def f(x):
    return (6.69*10**12)*math.cos(x*10**(-2))
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


while (t+i-mu) != no*mu  :
    i=0
    m=0
    while i != mu:
        #print(t+i)
        m=m+mn(t,i)
        i+=1
    mean.append(round(m/mu,4))
    t+=mu
#----------------------------------------------------
i=0
while i != len(mean):
    ex.append(round(ex[-1]+(xf-xi)/no,4))
    i+=1

#-----------------PRINTING RESULTS-------------------
j=0
while j != len(mean):
    print(ex[j],"to", ex[j+1], " ", mean[j])
    j+=1

