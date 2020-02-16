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
#Dont forget to recompile it if you want the updated UI.
import sys
from PySide2 import QtWidgets
from Mainwindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    #initialisation du mainwindow object qui se trouve dans mainwindow.py
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setupConnection()

    #Ajout des fonctions pour connecter
    def commandButtonClicked(self):
        self.lineEdit_command.setText('-1')
    #Modification et connection des widgets ici
    def setupConnection(self):
        self.button_command.clicked.connect(self.commandButtonClicked)


    


app = QtWidgets.QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())