

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
    
    def __init__(self, parent=None, title='', picks=[], othCheckBox=None, row=0, column=0,side=tk.LEFT, anchor=tk.W):
      self.Frame = tk.Frame(parent)
      self.Frame.grid(row=row,column=column)

      self.otherCheckBox = othCheckBox
      self.checkBoxVar = tk.IntVar()
      self.checkButton = tk.Checkbutton(self.Frame, text=title, variable=self.checkBoxVar, command=self.checkboxClicked)
      self.checkButton.pack()
      self.vars = []
      self.entries = []
      for pick in picks:
         var = tk.DoubleVar()
         lbl = tk.Label(self.Frame,text=pick)
         entry = tk.Entry(self.Frame)
         entry.insert(0, '0')
         lbl.pack(side=side, anchor=anchor, expand=tk.YES)
         entry.pack(side=side, anchor=anchor, expand=tk.YES)
         self.vars.append(var)
         self.entries.append(entry)

    def checkboxClicked(self):
        self.checkButton.config(state=tk.DISABLED)
        if self.getOtherCheckButton() != None:
            #for 
            if self.getOtherCheckButton().getCheckBoxState() == 1:
                self.getOtherCheckButton().deselectCheckBox()
                self.getOtherCheckButton().config(state=tk.NORMAL)
        else:
            print('There is no associated checkbox to the one you clicked on')

    def getCheckBoxState(self):
        return self.checkBoxVar.get()

    def getOtherCheckButton(self):
        return self.otherCheckBox.checkButton

    def setOtherCheckBox(self, otherCheckBox):
        self.otherCheckBox = otherCheckBox
        

#Widgets Function -----------------------------------------------------------
def debuggingButton():
    counter.set(counter.get()+1)
    string = 'I got clicked ' + counter.get().__str__() + ' times'
    mylabel = tk.Label(root,text = string).grid(row=10, column=0)
    print(checkBOXcineInv.getCheckBoxState())
    print(checkBOXcineDir.getCheckBoxState())


def eStopPressed():
    tk.Label(root,text='Emergency Stop has been pressed').grid(row=1,column=2)


#Widgets --------------------------------------------------------------------
label1 = tk.Label(root, text='Hello World!')
label2 = tk.Label(root, text='This is a positionned label')
debuggingButton = tk.Button(root, text = 'Click', padx = 40, command = debuggingButton, bg = 'blue', fg = '#ffffff')

checkBOXcineInv = checkboxCinematique(root, 'Cinématique inverse', ['x' , 'y' ,'z'], column = 4, row = 4)
checkBOXcineDir = checkboxCinematique(root, 'Cinématique directe', ['theta1' , 'theta2' ,'theta3'], column = 4, row = 5, othCheckBox=checkBOXcineInv)
checkBOXcineInv.setOtherCheckBox(checkBOXcineDir)

assert(checkBOXcineInv.getOtherCheckButton() != None)
assert(checkBOXcineDir.getOtherCheckButton() != None)
print(checkBOXcineInv.getCheckBoxState())
print(checkBOXcineDir.getCheckBoxState())

eStopButton = tk.Button(root, text = 'E-Stop', command = eStopPressed, bg = 'red', fg = 'white')


#Positionning ---------------------------------------------------------------

label1.grid(row=1, column=2)
label2.grid(row=0, column=0)
debuggingButton.grid(row=1, column=0)


eStopButton.grid(row=2,column=0)

root.mainloop() 
