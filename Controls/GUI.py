#Block comment en python : ctrl+K and ctrl+c to comment and ctrl+k and ctrl+u
#to uncomment
#*****************

#-------------------------------------------------------
#Cette section prend le fichier Mainwindow.py et l'execute.
#Ne pas oublier de recompiler le .py lorsqu'une modification est faite dans le fichier .ui
#Pour savoir la commande, aller lire le readMe.
import sys
from PySide import QtGui, QtCore
from Mainwindow34 import Ui_MainWindow
import os
import serial.tools.list_ports
import serial
import time
import struct


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    #initialisation du mainwindow object qui se trouve dans mainwindow.py
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.button_group = QtGui.QButtonGroup(self) #creer checkboxes exclusives
        self.button_group.addButton(self.checkBox_cinDir)
        self.button_group.addButton(self.checkBox_cinInv)
        self.checkBox_cinDir.setChecked(True)
        self.lineEdit_theta1.setEnabled(False)
        self.lineEdit_theta2.setEnabled(False)
        self.lineEdit_theta3.setEnabled(False)

        self.commandNb = 1
        self.currentPort = ''

        self.setup()


    #-----------------Ajout des fonctions pour connecter--------------------------------------
    def eStop(self):
        #self.timer.stop() #uncomment si tu veux arrêter la loop de timer qui créer une thread a chaque délai
        ''

    def sendCommandNumber(self):
        self.commandNb = self.lineEdit_ChangeCommand.text()
        try:
            cmdNb = int(self.commandNb)
        except:
            cmdNb = 0
            print('Ceci n''est pas une commande')
            return
        if cmdNb < 1 and cmdNb != 0:
            self.commandNb = 0
            print('Mauvais numero de commande')
        else:
            self.commandNb = cmdNb;
        self.label_commandNumber.setText(str(self.commandNb))
        print('Command is set to: ', self.commandNb)

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

    #--------------------FONCTIONS de commande---------------------------------------------
    def commandButtonStart(self):
        cmd = self.commandNb
        print('start button has been pressed')
        if cmd == 1:
            print("Command 1 is getting executed")
        elif cmd == 2:
            print("Command 2 is getting executed")
        elif cmd == 3:
            print('---------COMMAND 3----------\n')
            self.communicationTest()
            print('\n----------------------------')
        else:
            print("The command ", self.commandNb, " is not a known command")
 
    #cmd1:

    #cmd2:

    #cmd3: (Test de la communication)
    def communicationTest(self):

        message = struct.pack('h',35)
        print('Sending this message: ',message,'\n')
        try:
            self.SerComm = serial.Serial(port=self.currentPort, baudrate=57600)
            print('Trying to open port :', self.currentPort)
            try:
                self.SerComm.open()
                print('\t-> Port', self.currentPort,' is open')
            except:
                print('\t-> Port', self.currentPort,' did not open')
        
            self.SerComm.write(message)
            print('Message has been send')
            #print(struct.unpack('h',message))
            self.SerComm.close()
        except:
            print('The message did not send')


    #---------------------FONCTIONS pour self.comboBoxPort-------------------------------------
    def updatePort(self):
        print('A search for ports has been created')
        infoPorts = list(serial.tools.list_ports.comports())
        self.comboBoxPort.clear()
        self.listNamePorts = []
        for ports in infoPorts:
            self.listNamePorts.append(ports[0])
        self.comboBoxPort.addItems(self.listNamePorts)
        self.currentPort = self.comboBoxPort.currentText()
        print('A search for ports has closed') 

    def portChanged(self):
        self.currentPort = self.comboBoxPort.currentText()
        print('Port: ', self.currentPort)
    
    #-----------------------Thread functions------------------------------------------------------
    def createTimeThread(self):
        worker = Worker(self.timeSecCheck) # Any other args, kwargs are passed to the run function
        self.threadpool.start(worker)
   
    def createPortThread(self):
        worker = Worker(self.updatePort) # Used to check for new ports when button is clicked
        self.threadpool.start(worker)

    #-------------------Modification et connection des widgets ici----------------------------------
    def setup(self):
        self.button_sendCommandNb.clicked.connect(self.sendCommandNumber)
        self.pushButton_Params.clicked.connect(self.paramUpdateCoordonneCart)
        self.EStop.clicked.connect(self.eStop)
        self.buttonUpdatePort.clicked.connect(self.createPortThread)
        self.button_command.clicked.connect(self.commandButtonStart)

        self.checkBox_cinDir.stateChanged.connect(self.checkboxCinDirClicked)
        self.checkBox_cinInv.stateChanged.connect(self.checkboxCinInvClicked)
        self.comboBoxPort.currentIndexChanged.connect(self.portChanged)

        self.createPortThread()
        self.serialPort = self.comboBoxPort.currentText()

        self.timerASec = QtCore.QTimer()
        self.timerASec.setInterval(1000)
        self.timerASec.timeout.connect(self.createTimeThread)
        #self.timer3Sec.start()





#---------------------------Thread Class-----------------------------------
class Worker(QtCore.QRunnable):
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


app = QtGui.QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())