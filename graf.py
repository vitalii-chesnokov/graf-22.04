from tkinter import *
from tkinter import simpledialog as sd
import  matplotlib.pyplot as plt #Y funktsiooni loomiseks
import numpy  #X vahemik X[min,max]
def Vaal():
    """Joonestatakse vaal paraabolite abil matplotlib mooduli kasutades
    """
    x1=numpy.arange(0,9,0.5)
    y1=(2/27)*x1**2-3
    x2=numpy.arange(-10,0,0.5)
    y2=0.04*x2**2-3
    x3=numpy.arange(-9,-3,0.5)
    y3=(2/4)*(x3+6)**2+1
    x4=numpy.arange(-3,9,0.5)
    y4=-(1/12)*(x4-3)**2+6
    x5=numpy.arange(5,8.3,0.5)
    y5=(1/9)*(x5-5)**2+2
    x6=numpy.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=numpy.arange(-13,-9,0.5)
    y7=-(0.75)*(x7+11)**2+6
    x8=numpy.arange(-15,-13,0.5)
    y8=-(0.5)*(x8+13)**2+3
    x9=numpy.arange(-15,-10,0.5) #min,max, steep
    y9=[1]*len(x9)
    x10=numpy.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure()
    #plt.plot(x1,y1,"r:*",x2,y2,"m-s")
    for i in range(1,11):
        plt.plot(eval(f"x{i}"), eval(f"y{i}"))
    plt.title
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

def Prillid():
    """
    """
    x1=numpy.arange(-9,-1,0.7)
    y1=-(1/16)*(x1+5)**2+2
    x2=numpy.arange(1,9,0.7)
    y2=-(1/16)*(x2-5)**2+2
    x3=numpy.arange(-9,-1,0.7)
    y3=(1/4)*(x3+5)**2-3
    x4=numpy.arange(1,9,0.7)
    y4=(1/4)*(x4-5)**2-3
    x5=numpy.arange(-9,-6,0.7)
    y5=-(x5+7)**2+5
    x6=numpy.arange(6,9,0.7)
    y6=-(x6-7)**2+5
    x7=numpy.arange(-1,1,0.7)
    y7=-(0.5*x7)**2+1.5
    plt.figure()
    for i in range(1,8):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"))
    plt.title
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show

def Vihmavari():
    """
    """
    x1=numpy.arange(-12,12,0.7)
    y1=-(1/18)*x1**2+12
    x2=numpy.arange(-4,4,0.7)
    y2=-(1/8)*x2**2+6
    x3=numpy.arange(-12,-4,0.7)
    y3=-(1/8)*(x2+8)**2+6
    x4=numpy.arange(4,12,0.7)
    y4=-(1/8)*(x4-8)**2+6
    x5=numpy.arange(-4,-0.3,0.7)
    y5=2*(x5+3)**2-9
    x6=numpy.arange(-4,-0.2,0.7)
    y6=1.5*(x6+3)**2-10
    plt.figure()
    for i in range(1,8):
        plt.plot(eval(f"x{i}"),eval(f"y{i}"))
        plt.title
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show
aken=Tk()
aken.geometry("500x500")
aken.title("Akna pealkiri")
aken.configure(bg="#DCDCDC")
aken.iconbitmap("icon.ico")
raam=Frame(aken)
vl=Button(raam,
            text="Vaal",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Vaal)
pr=Button(raam,
          text="Prillid",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Prillid)
vh=Button(raam,
            text="Vihmavari",
            bg="#7B68EE",
            fg="white",
            font="Britannic_Bold 16",
            width=16,
            command=Vihmavari)
vl.grid(row=0, column=0)
pr.grid(row=1,column=2)
vh.grid(row=0, column=1)
aken.mainloop()