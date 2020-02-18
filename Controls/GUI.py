#Block comment in python : ctrl+K and ctrl+c to comment and ctrl+k and ctrl+u to uncomment
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
#Dont forget to recompile it if you want the updated UI. To recompile go to readMe.
import sys
from PySide2 import QtWidgets, QtCore
from Mainwindow import Ui_MainWindow
import serial.tools.list_ports
import time

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #initialisation du mainwindow object qui se trouve dans mainwindow.py
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.setup()


    #Ajout des fonctions pour connecter
    def eStop():
        #self.timer.stop() #uncomment if you need to stop the timer thread loop which updates elements in the UI
        ''

    def commandButtonClicked(self):
        self.lineEdit_command.setText('-1')

    def paramUpdateCoordonneCart(self):
        """Pour updater les coordonnees cartesiennes lorsqu'elles sont modifiees"""
        self.xx = float(self.lineEdit_x.text())
        self.yy = float(self.lineEdit_y.text())
        self.zz = float(self.lineEdit_z.text())
        self.label_x_confimed.setText(str(self.xx))
        self.label_y_confimed.setText(str(self.yy))
        self.label_z_confimed.setText(str(self.zz))

    #Thread functions
    def createTimeThread(self):
        worker = Worker(self.timeTenthOfASecCheck, 'test') # Any other args, kwargs are passed to the run function
        self.threadpool.start(worker)

    def timeTenthOfASecCheck(self,*args,**kwargs):
        print('The timer thread is runing')
            
        

    #Modification et connection des widgets ici
    def setup(self):
        self.button_command.clicked.connect(self.commandButtonClicked)
        self.pushButton_Params.clicked.connect(self.paramUpdateCoordonneCart)
        self.EStop.clicked.connect(self.eStop)

        ports = list(serial.tools.list_ports.comports())
        self.comboBoxPort.addItems(ports)
        self.serialPort = self.comboBoxPort.currentText()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.createTimeThread)
        self.timer.start()





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