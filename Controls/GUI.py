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
        self.counter = 0;


        self.setup()


    #-----------------Ajout des fonctions pour connecter--------------------------------------
    def eStop(self):
       """Bouton d'arrêt d'urgence"""
        
        

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
        """Pour updater les coordonnees cartesiennes ou joints lorsqu'elles sont modifiees"""
        if self.checkBox_cinDir.isChecked():
            self.xx = float(self.lineEdit_x.text())
            self.yy = float(self.lineEdit_y.text())
            self.zz = float(self.lineEdit_z.text())
            self.label_x_confirmed.setText(str(self.xx))
            self.label_y_confirmed.setText(str(self.yy))
            self.label_z_confirmed.setText(str(self.zz))
        else:
            self.theta1 = int(self.lineEdit_theta1.text())
            self.theta2 = int(self.lineEdit_theta2.text())
            self.theta3 = int(self.lineEdit_theta3.text())
            self.label_theta1_confirmed.setText(str(self.theta1))
            self.label_theta2_confirmed.setText(str(self.theta2))
            self.label_theta3_confirmed.setText(str(self.theta3))

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
        

    def packingMessageShort(self, msg1_cmdNb, msg2_short, msg3_short, msg4_short):
        """Msg1 stands for the command Nb, msg2 msg3 msg4 stand for the argument to send"""
        format = 'hhhh'
        size = struct.calcsize(format)
        st = struct.Struct(format)
        messageBuff = bytearray(size)
        #Sending a string needs to be in this format : b"abc..."
        st.pack_into(messageBuff, 0, msg1_cmdNb, msg2_short, msg3_short, msg4_short) 

        return messageBuff

    def timeSecCheck(self):
        print('the time thread is runing')

    #FONCTIONS de commande
    def commandButtonStart(self):
        cmd = self.commandNb
        answerCmdNb = cmd
        print('start button has been pressed')
        if cmd == 1:
            print('---------COMMAND 1----------\n')
            if self.counter < 1:
                answerCmdNb = self.sendMotorPositionAngle(cmd,1500,1500,1500)
                self.counter = self.counter + 1;
            else:
                answerCmdNb = self.sendMotorPositionAngle(cmd,2000,2000,2000)
                self.counter = self.counter - 1;

        elif cmd == 2:
            print("Command 2 is getting executed")

        elif cmd == 3:
            print('---------COMMAND 3----------\n')
            self.theta1 = (int)(self.label_theta1_confirmed.text())
            self.theta2 = (int)(self.label_theta2_confirmed.text())
            self.theta3 = (int)(self.label_theta3_confirmed.text())

            answerCmdNb = self.sendMotorPositionAngle(cmd,self.theta1,self.theta2,self.theta3)
        else:
            print("The command ", self.commandNb, " is not a known command")

        if answerCmdNb != cmd: #Verification pour voir si il n'y a pas eu d'erreur de comm
            print("!****Erreur de comm****!")
            
            #self.sendMotorAngleThread(cmd,1500,1500,1250)
        
        print('--------------------------\n')

    def sendMotorPositionAngle(self, cmdNb, theta1, theta2, theta3):
        """Function to send data to the Open CR, also used with a different thread so the loop wont block until it receives data """
        messageBuff = self.packingMessageShort(cmdNb, theta1, theta2, theta3)

        #create a thread to send the position and wait for response
        msgReceived = False
        print('Sending those angles: ', theta1,', ', theta2,', ', theta3)
        try:
            self.SerComm = serial.Serial(port=self.currentPort, baudrate=57600)
            self.SerComm.write(messageBuff)
            while msgReceived == False:
                if self.SerComm.in_waiting:
                    bytesReponse = self.SerComm.read(1)
                    msgReceived = True
            self.SerComm.close()
            answer = struct.unpack('B',bytesReponse)[0];
            print('\t-> [SUCCESS]With an response of : ', answer)
            
        except:
            print('\t-> [FAIL]Port', self.currentPort,' did not open')

        return (int)(answer)

    #FONCTIONS pour Manual jog
         


    #FONCTIONS pour self.comboBoxPort
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
    
    #-----------------------Thread creation functions to call------------------------------------------------------
    def createTimeThread(self):
        worker = Worker(self.timeSecCheck) # Any other args, kwargs are passed to the run function
        self.threadpool.start(worker)

    def sendMotorAngleThread(self, cmdNb, theta1, theta2, theta3):
        worker = Worker(self.sendMotorPositionAngle, cmdNb, theta1, theta2, theta3)
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
        #self.createCommCheckThread()
        self.serialPort = self.comboBoxPort.currentText()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.createTimeThread)
        #self.timer.start()





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