#This is a example code copying from Zhihu to learn animation in matplotlib.

import matplotlib.animation as animation
from pylab import *
from numpy import *

omega=0.1
Lambda=2
#omega2=0.07
k=2*pi/Lambda
def WW(t,omega,k):
    x=linspace(0,10,200)
    return (x,cos(omega*t-k*x))
def update(t,omega,k):
   # print(t)
    x,y=WW(t,omega,k)
    line.set_data((x,y))
    ax.set_xlim(0,10)
    ax.set_ylim(-1,1)
    return line

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ani = animation.FuncAnimation(fig, update,frames=800,fargs=(omega,k))
show()