
import tkinter as tk

#ROOT -----------------------------------------------------------------------
root = tk.Tk()
root.title('GUI for delta Robot')

#Global Variables -----------------------------------------------------------
counter = tk.IntVar()

checkVarCinDir = tk.BooleanVar()
checkVarCinInv = tk.BooleanVar()
estop = tk.BooleanVar()

counter.set(0)

#Class ----------------------------------------------------------------------

class checkboxCinematique:
    
    def __init__(self, parent=None, title='', picks=[], othCheckBox=None, side=tk.LEFT, anchor=tk.W):
      self.Frame = tk.Frame(parent)
      self.Frame.grid(row=4,column=4)
      self.otherCheckBox = othCheckBox
      self.checkBoxVar = tk.IntVar()
      self.checkButton = tk.Checkbutton(self.Frame, text=title, variable=self.checkBoxVar, command=self.checkboxClicked)
      self.checkButton.pack()
      self.vars = []
      for pick in picks:
         var = tk.DoubleVar()
         lbl = tk.Label(self.Frame,text=pick)
         lbl.pack(side=side, anchor=anchor, expand=tk.YES)
         self.vars.append(var)

    def checkboxClicked(self):
        self.checkButton.config(state=tk.DISABLED)
        if self.getOtherCheckButton() != None:
            if self.getOtherCheckButton().getCheckBoxState() == 1:
                self.getOtherCheckButton().deselect()
                self.getOtherCheckButton().config(state=tk.NORMAL)
        else:
            print('There is no associated checkbox to the one you clicked on')

    def getCheckBoxState(self):
        return self.checkBoxVar

    def getOtherCheckButton(self):
        return self.otherCheckBox

    def setOtherCheckBox(self, otherCheckBox):
        self.otherCheckBox = otherCheckBox
        

#Widgets Function -----------------------------------------------------------
def buttonPressed():
    counter.set(counter.get()+1)
    string = 'I got clicked ' + counter.get().__str__() + ' times'
    mylabel = tk.Label(root,text = string).grid(row=10, column=0)


def clickCinInv():
    checkButtonCinInv.config(state=tk.DISABLED)
    checkButtonCinDir.deselect()
    checkButtonCinDir.config(state=tk.NORMAL)

def eStopPressed():
    tk.Label(root,text='Emergency Stop has been pressed').grid(row=1,column=2)


#Widgets --------------------------------------------------------------------
label1 = tk.Label(root, text='Hello World!')
label2 = tk.Label(root, text='This is a positionned label')
e = tk.Entry(root)
myButton = tk.Button(root, text = 'Click', padx = 40, command = buttonPressed, bg = 'blue', fg = '#ffffff')

checkBOX = checkboxCinematique(root, 'Cinématique directe', ['x' , 'y' ,'z'])

checkButtonCinInv = tk.Checkbutton(root, text='Cinématique directe', variable=checkVarCinInv, command=clickCinInv)
eStopButton = tk.Button(root, text = 'E-Stop', command = eStopPressed, bg = 'red', fg = 'white')


#Positionning ---------------------------------------------------------------

label1.grid(row=1, column=2)
label2.grid(row=0, column=0)
e.grid(row=1,column=3)
myButton.grid(row=1, column=0)

#checkButtonCinDir.grid(row=3,column=0)
checkButtonCinInv.grid(row=4,column=0)
eStopButton.grid(row=2,column=0)

root.mainloop() 

""" 

import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('500x570')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Driver Cam')
frame.config(background='light blue')
label = Label(frame, text="Driver Cam",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)



def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Mayur Kadam\n2. Abhishek Ezhava \n3. Rajendra Patil \n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)



def exitt():
   exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame = capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   


   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,command=web,text='Open Cam',font=('helvetica 15 bold'))
but1.place(x=5,y=104)


but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',command=exitt,font=('helvetica 15 bold'))
but5.place(x=210,y=478)


root.mainloop()

"""
