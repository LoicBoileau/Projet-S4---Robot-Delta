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

        self.setup()




    #-------------------Modification et connection des widgets ici----------------------------------
    def setup(self):

        #QTWidgets setuo
        self.button_group = QtGui.QButtonGroup(self) 
        self.button_group.addButton(self.checkBox_cinDir)
        self.button_group.addButton(self.checkBox_cinInv)
        self.checkBox_cinDir.setChecked(True)
        self.lineEdit_theta1.setEnabled(False)
        self.lineEdit_theta2.setEnabled(False)
        self.lineEdit_theta3.setEnabled(False)

        self.Slider_ManJog_theta1.setMaximum(2400)
        self.Slider_ManJog_theta2.setMaximum(2400)
        self.Slider_ManJog_theta3.setMaximum(2400)
        self.Slider_ManJog_theta1.setMinimum(1000)
        self.Slider_ManJog_theta2.setMinimum(1000)
        self.Slider_ManJog_theta3.setMinimum(1000)

        #Initialisation des variables globales
        self.commandNb = 1
        self.currentPort = ''
        self.counter = 0
        self.sliderIsClicked = False
        self.theta1 = (int)(self.label_theta1_confirmed.text())
        self.theta2 = (int)(self.label_theta2_confirmed.text())
        self.theta3 = (int)(self.label_theta3_confirmed.text())
        self.increments = (int)(self.lineEdit_ManJog_increments.text())

        #Thread setup
        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.createPortThread()
        #self.createCommCheckThread()
        self.serialPort = self.comboBoxPort.currentText()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        #self.timer.timeout.connect(self.creatSliderThread)
        #self.timer.start()

        #FUNCTIONS SETUP

        self.button_sendCommandNb.clicked.connect(self.sendCommandNumber)
        self.pushButton_Params.clicked.connect(self.paramUpdateCoordonneCart)
        self.EStop.clicked.connect(self.eStop)
        self.buttonUpdatePort.clicked.connect(self.createPortThread)
        self.button_command.clicked.connect(self.commandButtonStart)

        self.checkBox_cinDir.stateChanged.connect(self.checkboxCinDirClicked)
        self.checkBox_cinInv.stateChanged.connect(self.checkboxCinInvClicked)
        self.comboBoxPort.currentIndexChanged.connect(self.portChanged)
        self.lineEdit_ManJog_increments.editingFinished.connect(self.updateIncrements)

        self.Slider_ManJog_theta1.sliderPressed.connect(self.createManJogThread)
        self.Slider_ManJog_theta2.sliderPressed.connect(self.createManJogThread)
        self.Slider_ManJog_theta3.sliderPressed.connect(self.createManJogThread)

        self.Slider_ManJog_theta1.sliderReleased.connect(self.sliderRealesed)
        self.Slider_ManJog_theta2.sliderReleased.connect(self.sliderRealesed)
        self.Slider_ManJog_theta3.sliderReleased.connect(self.sliderRealesed)


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
            self.label_x_confirmed.setText(self.lineEdit_z.text())
            self.label_y_confirmed.setText(self.lineEdit_z.text())
            self.label_z_confirmed.setText(self.lineEdit_z.text())
        else:
            self.label_theta1_confirmed.setText(self.lineEdit_theta1.text())
            self.label_theta2_confirmed.setText(self.lineEdit_theta2.text())
            self.label_theta3_confirmed.setText(self.lineEdit_theta3.text())

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


    #FONCTIONS de commande
    def commandButtonStart(self):
        cmd = self.commandNb
        answerCmdNb = cmd

        print('start button has been pressed')
        #Vérifie que la commande a envoyer doit être angulaire ou cartésienne
        if (self.checkBox_cinInv.stateChanged.connect(self.checkboxCinInvClicked)):
            cmd += 3

        if cmd == 1:
            print('---------COMMAND 1----------\n')
            if self.counter < 1:
                self.theta1 = 1500
                self.theta2 = 1500
                self.theta3 = 1500

                self.counter = self.counter + 1;
            else:
                self.theta1 = 2000
                self.theta2 = 2000
                self.theta3 = 2000

                self.counter = self.counter - 1;

            answerCmdNb = self.sendMotorPositionAngle(cmd,self.theta1,self.theta2,self.theta3)

        elif cmd == 2:
            print("Command 2 is getting executed")

        elif cmd == 3:
            print('---------COMMAND 3----------\n')
            self.theta1 = (int)(self.label_theta1_confirmed.text())
            self.theta2 = (int)(self.label_theta2_confirmed.text())
            self.theta3 = (int)(self.label_theta3_confirmed.text())

            answerCmdNb = self.sendMotorPositionAngle(cmd,self.theta1,self.theta2,self.theta3)

        elif cmd == 4:
            print('---------COMMAND 1 CARTESIAN----------\n')
            if self.counter < 1:
                self.x = .1
                self.y = .1
                self.z = .1

                self.counter = self.counter + 1;
            else:
                self.x = .1
                self.y = .1
                self.z = .2

                self.counter = self.counter - 1;

            answerCmdNb = self.sendCartesianCoord(cmd,self.x,self.y,self.z)

        else:
            print("The command ", self.commandNb, " is not a known command")

        print('--------------------------\n')

    def sendMotorPositionAngle(self, cmdNb, theta1, theta2, theta3):
        """Function to send data to the Open CR, also used with a different thread so the loop wont block until it receives data """

        if cmdNb >= 1: #Only if the motors are moved
            self.updateSliderManJog()

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
            answer = -1
            print("!****Erreur de comm****!")
            return (int)(answer)

        if answer != cmdNb: #Verification pour voir si il n'y a pas eu d'erreur de comm
            return 0

        return (int)(answer)

    #FONCTION d'envoi de coordonnées cartésiennes 

    def calculTheta(self, x, y, z):
        
        rA = 0.08083 
        rB = 0.06606
        base = rA/(2*sqrt(3))
        effecteur = rB/(2*sqrt(3))

        l_bicep = 0.10183
        l_avantBras = 0.21562

        y = y - effecteur;

        ni = (x^2 + y^2 + z^2 + l_bicep^2 - l_avantBras^2 + base^2)/(2*z);
        mi = (-base - y)/z;
        li = -(ni + mi*-base)^2 + l_bicep*(mi^2*l_bicep + l_bicep);

        if(li < 0): # Position impossible
            singularite = 1;
            print("Erreur de singularité, veuillez entrer une autre commande")
            return -1
        else:
            yi = (-base - ni*mi - sqrt(li))/(mi^2 + 1);
            zi = ni + mi*yi;
            theta = 180 * atan(-zi/(-base - yi))/pi;
    
            if(yi > -base): # On choisi l'autre solution
                theta = theta + 180;
            end
    
            singularite = 0;
            return(float)(theta)


    def sendCartesianCoord(self, cmdNb, x, y, z):
       
        # Calcul de thetas
        theta1 = calculTheta(self, x, y, z)
        theta2 = calculTheta(self, x*cos(120*pi/180) + y*sin(120*pi/180), y*cos(120*pi/180) - x*sin(120*pi/180),z)
        theta3 = calculTheta(self, x*cos(120*pi/180) - y*sin(120*pi/180), y*cos(120*pi/180) + x*sin(120*pi/180),z)
        # Envoi de la commande cartésienne sous forme angulaire
        sendMotorPositionAngle(self,cmdNb,theta1,theta2,theta3)


    #FONCTIONS pour Manual jog

    def sliderClicked(self):
        self.sliderIsClicked = True
        currentValueTheta1 = self.theta1
        currentValueTheta2 = self.theta2
        currentValueTheta3 = self.theta3

        while self.sliderIsClicked:
            if currentValueTheta1 != self.Slider_ManJog_theta1.value() \
                    or currentValueTheta2 != self.Slider_ManJog_theta2.value() \
                    or currentValueTheta3 != self.Slider_ManJog_theta3.value():

                self.theta1 = self.Slider_ManJog_theta1.value()
                self.theta2 = self.Slider_ManJog_theta2.value()
                self.theta3 = self.Slider_ManJog_theta3.value()

                result = self.sendMotorPositionAngle(1, self.theta1, self.theta2, self.theta3)

                currentValueTheta1 = self.theta1
                currentValueTheta2 = self.theta2
                currentValueTheta3 = self.theta3

            time.sleep(0.1)
    
    def sliderRealesed(self):
        self.sliderIsClicked = False
        

    def updateSliderManJog(self):
        if self.theta1 != self.Slider_ManJog_theta1.value():
            self.Slider_ManJog_theta1.setValue(self.theta1)
        if self.theta2 != self.Slider_ManJog_theta2.value():
            self.Slider_ManJog_theta2.setValue(self.theta2)
        if self.theta3 != self.Slider_ManJog_theta3.value():
            self.Slider_ManJog_theta3.setValue(self.theta3)

    def updateIncrements(self):
        self.increments = (int)(self.lineEdit_ManJog_increments.text())
        print("Increments has been changed to ", self.increments)


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
    def createManJogThread(self):
        worker = Worker(self.sliderClicked) # Any other args, kwargs are passed to the run function
        self.threadpool.start(worker)

    def sendMotorAngleThread(self, cmdNb, theta1, theta2, theta3):
        worker = Worker(self.sendMotorPositionAngle, cmdNb, theta1, theta2, theta3)
        self.threadpool.start(worker)

    def sendCartCoordThread(self, cmdNb, x, y, z):
        worker = Worker(self.sendCartesianCoord, cmdNb, x, y, z)
        self.threadpool.start(worker)
   
    def createPortThread(self):
        worker = Worker(self.updatePort) # Used to check for new ports when button is clicked
        self.threadpool.start(worker)





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