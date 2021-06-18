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
window.geometry("132x132")

canvas = Canvas(window,width=132,height=132,bg="white")
canvas.pack()
x ,y =0,0

now = np.zeros((28,28))
model = load_model("mymodel.h5")

def draw(event):
    x1, y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2,fill="black")
    if 0<=(y1//4)<28 and 0<= (x1//4) <28:  
        now[y1//4][x1//4]=1

def erease(event):
    canvas.delete("all")
    global now
    now = np.zeros((28,28))

def guess(event):

    global now
    xhat = now.reshape((1,28,28,1))
    yhat = model.predict_classes(xhat)
    messagebox.showinfo(message=str(yhat))

canvas.bind("<B1-Motion>",draw)
window.bind("<Button-3>",erease)
window.bind("<Button-2>",guess)

window.mainloop()
