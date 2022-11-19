import random
from math import sin,cos,pi,log
#from tkinter imoport *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from itertools import count


#画布的宽
CANVAS_WIDTH=6.4
#画布的高 
CANVAS_HEIGHT=4.8
#画布水平中心
CANVAS_CENTER_X=CANVAS_WIDTH/2
#画布垂直中心
CANVAS_CENTER_Y=CANVAS_HEIGHT/2
#IMAGE_ENLARGE=11
HEART_COLOR='#FFFFFF'

def data_gen():
    for cnt in count():
        t=cnt/10
        yield ( 16*(np.sin(t)**3),(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)))

#def calc(time):
    #t=
    #return ( 16*(np.sin(t)**3),(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)))
    #return (t,(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)))

def init():
    xdata,ydata=[],[]
    line.set_line(xdata,ydata)
    return line

def update(data):
    #print(time)
    #x,y=calc(time)
    x,y=data
    print("x:{}".format(x))
    print("y:{}".format(y))
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata,ydata)
    ax.set_xlim(-100,100)
    ax.set_ylim(-100,100)
    return line

if __name__=='__main__':
    xdata=[]
    ydata=[]
    fig=plt.figure(figsize=(CANVAS_WIDTH*2,CANVAS_HEIGHT*2))
    ax=fig.add_subplot()
    ax.grid()
    ax.set_title("Heart",fontdict={"fontsize":18})
    line,=ax.plot([],[],lw=2)
    ani=FuncAnimation(fig,update,data_gen)
    plt.show()
    
    
   
    
    
   



