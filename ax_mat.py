import random
from math import sin,cos,pi,log
#from tkinter imoport *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation



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


def calc(time):
    t=np.linspace(0,t,200)
    return ( 16*(np.sin(t)**3),(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)))

if __name__=='__main__':
    fig=plt.figure(figsize=(CANVAS_WIDTH*2,CANVAS_HEIGHT*2))
    ax=fig.add_subplot()
    ax.set_title("Heart",fontdict={"fontsize":18})
    line,=ax.plot([],[],lw=2)
    
    
    
   
    
    
    ax.plot(x,y)
    plt.show()



