from tkinter import *
import numpy as np
from keras.utils import np_utils 
from keras.datasets import mnist 
from keras.models import Sequential 
from keras import layers
from keras.layers import Dense, Activation
from keras.models import load_model
from tkinter import messagebox

window = Tk()
window.geometry("320x132")

canvas = Canvas(window,width=132,height=132,bg="white")
canvas.pack(side=LEFT)
x ,y =0,0

btnLabel = Label(window)
btnLabel.pack(side=LEFT)

mydata_x  = np.load("newData\\x_save.npy")
mydata_y  = np.load("newData\y_save.npy")



now = np.zeros((28,28))

def myFunc0():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=0
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  
def myFunc1():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=1
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  
def myFunc2():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=2
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  
def myFunc3():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=3
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  
def myFunc4():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=4
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  
def myFunc5():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=5
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  
def myFunc6():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=6
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  
def myFunc7():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=7
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  

def myFunc8():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(mydata_x,now)
    temp = np.zeros((1))  
    
    temp[0]=8
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  

def myFunc9():
    print("btnclicked")
    global now
    # save function
    global isfirst
    global mydata_x
    global mydata_y
    
    mydata_x = np.concatenate((mydata_x,now),axis=0)
    print(now)
    temp = np.zeros((1))  
    
    temp[0]=9
    mydata_y = np.concatenate((mydata_y,temp),axis=0)  

b0 = Button(btnLabel, text = "0" , command =myFunc0)
b1 = Button(btnLabel,text = "1" ,command =myFunc1)
b2 = Button(btnLabel,text = "2" ,command =myFunc2)
b3 = Button(btnLabel,text = "3" ,command =myFunc3)
b4 = Button(btnLabel,text = "4" ,command =myFunc4)
b5 = Button(btnLabel,text = "5" ,command =myFunc5)
b6 = Button(btnLabel,text = "6" ,command =myFunc6)
b7 = Button(btnLabel,text = "7" ,command =myFunc7)
b8 = Button(btnLabel,text = "8" ,command =myFunc8)
b9 = Button(btnLabel,text = "9" ,command =myFunc9)

b0.pack(side=LEFT)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
b4.pack(side=LEFT)
b5.pack(side=LEFT)
b6.pack(side=LEFT)
b7.pack(side=LEFT)
b8.pack(side=LEFT)
b9.pack(side=LEFT)





def draw(event):
    x1, y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill="black")
    print(y1//4 , x1//4)
    if 0<=(y1//4)<28 and 0<= (x1//4) <28:  
        now[y1//4][x1//4]=1
        

def erease(event):
    canvas.delete("all")
    global now
    now = np.zeros((28,28))

canvas.bind("<B1-Motion>",draw)
window.bind("<Button-3>",erease)




window.mainloop()

np.save("newData/x_save",mydata_x)
np.save("newData/y_save",mydata_y)

