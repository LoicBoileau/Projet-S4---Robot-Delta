#Block comment in python : ctrl+K and ctrl+c to comment and ctrl+k and ctrl+u
#to uncomment
#*****************

#-------------------------------------------------------
#This section is to automatically compile the .ui file and run the application

#import sys
#from PySide2 import QtCore, QtGui, QtWidgets
#from PySide2.QtUiTools import QUiLoader

#loader = QUiLoader()

#app = QtWidgets.QApplication(sys.argv)
#window = loader.load("Mainwindow.ui", None)
#window.show()
#app.exec_()
#------------------------------------------------------

#-------------------------------------------------------
#This section is to take the mainwindow.py and run it.
#Dont forget to recompile it if you want the updated UI.  To recompile go to
#readMe.
import sys
from PySide2 import QtWidgets, QtCore
from Mainwindow import Ui_MainWindow
import os
import serial.tools.list_ports
import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #initialisation du mainwindow object qui se trouve dans mainwindow.py
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.button_group = QtWidgets.QButtonGroup(self) #creating exclusive checkboxes
        self.button_group.addButton(self.checkBox_cinDir)
        self.button_group.addButton(self.checkBox_cinInv)
        self.checkBox_cinDir.setChecked(True)
        self.lineEdit_theta1.setEnabled(False)
        self.lineEdit_theta2.setEnabled(False)
        self.lineEdit_theta3.setEnabled(False)

        self.setup()


    #-----------------Ajout des fonctions pour connecter--------------------------------------
    def eStop():
        #self.timer.stop() #uncomment if you need to stop the timer thread loop
        #which updates elements in the UI
        ''

    def commandButtonClicked(self):
        self.lineEdit_command.setText('-1')

    def paramUpdateCoordonneCart(self):
        """Pour updater les coordonnees cartesiennes lorsqu'elles sont modifiees"""
        if self.checkBox_cinDir.isChecked():
            self.xx = float(self.lineEdit_x.text())
            self.yy = float(self.lineEdit_y.text())
            self.zz = float(self.lineEdit_z.text())
            self.label_x_confimed.setText(str(self.xx))
            self.label_y_confimed.setText(str(self.yy))
            self.label_z_confimed.setText(str(self.zz))
        else:
            self.theta1 = float(self.lineEdit_theta1.text())
            '...A completer'

    def checkboxCinDirClicked(self):
        if not self.checkBox_cinDir.isChecked():
            self.lineEdit_x.setEnabled(False)
            self.lineEdit_y.setEnabled(False)
            self.lineEdit_z.setEnabled(False)
            self.lineEdit_theta1.setEnabled(True)
            self.lineEdit_theta2.setEnabled(True)
            self.lineEdit_theta3.setEnabled(True)

    def checkboxCinInvClicked(self):
        if not self.checkBox_cinInv.isChecked():
            self.lineEdit_x.setEnabled(True)
            self.lineEdit_y.setEnabled(True)
            self.lineEdit_z.setEnabled(True)
            self.lineEdit_theta1.setEnabled(False)
            self.lineEdit_theta2.setEnabled(False)
            self.lineEdit_theta3.setEnabled(False)
            
    def timeSecCheck(self,*args,**kwargs):
        print('The timer thread is runing')

    def updatePort(self):
        print('A search for ports has been created')
        infoPorts = list(serial.tools.list_ports.comports())
        currentText = self.comboBoxPort.currentText()
        self.comboBoxPort.clear()
        self.comboBoxPort.addItems(info[0] for info in infoPorts) 
        print('A search for ports has closed') 
    
    #-----------------------Thread functions------------------------------------------------------
    def createTimeThread(self):
        worker = Worker(self.timeSecCheck) # Any other args, kwargs are passed to the run function
        self.threadpool.start(worker)
   
    def createPortThread(self):
        worker = Worker(self.updatePort) # Any other args, kwargs are passed to the run function
        self.threadpool.start(worker)

    #-------------------Modification et connection des widgets ici----------------------------------
    def setup(self):
        self.button_command.clicked.connect(self.commandButtonClicked)
        self.pushButton_Params.clicked.connect(self.paramUpdateCoordonneCart)
        self.EStop.clicked.connect(self.eStop)
        self.checkBox_cinDir.stateChanged.connect(self.checkboxCinDirClicked)
        self.checkBox_cinInv.stateChanged.connect(self.checkboxCinInvClicked)
        self.buttonUpdatePort.clicked.connect(self.createPortThread)


        self.createPortThread()
        self.serialPort = self.comboBoxPort.currentText()

        self.timerASec = QtCore.QTimer()
        self.timerASec.setInterval(1000)
        self.timerASec.timeout.connect(self.createTimeThread)
        #self.timer3Sec.start()





#---------------------------Thread Class-----------------------------------
class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and 
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @QtCore.Slot()  # QtCore.Slot
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)



  


app = QtWidgets.QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())