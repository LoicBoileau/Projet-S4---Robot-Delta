# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created: Sat Apr 18 12:41:44 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(849, 724)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(341, 201, 0, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 14, 80, 20))
        self.label_5.setObjectName("label_5")
        self.comboBoxPort = QtGui.QComboBox(self.centralwidget)
        self.comboBoxPort.setGeometry(QtCore.QRect(90, 15, 221, 20))
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.frame_command1 = QtGui.QFrame(self.centralwidget)
        self.frame_command1.setGeometry(QtCore.QRect(30, 40, 431, 581))
        self.frame_command1.setStyleSheet("")
        self.frame_command1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_command1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_command1.setObjectName("frame_command1")
        self.label_theta1 = QtGui.QLabel(self.frame_command1)
        self.label_theta1.setGeometry(QtCore.QRect(190, 164, 56, 20))
        self.label_theta1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theta1.setObjectName("label_theta1")
        self.lineEdit_x = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_x.setGeometry(QtCore.QRect(45, 54, 130, 20))
        self.lineEdit_x.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.button_command = QtGui.QPushButton(self.frame_command1)
        self.button_command.setGeometry(QtCore.QRect(12, 510, 235, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_command.setFont(font)
        self.button_command.setStyleSheet("#button_command{\n"
"border: 2px solid;\n"
"background-color: white;\n"
"    border-top-color: rgb(85, 255, 0);\n"
"    border-left-color: rgb(85, 255, 0);\n"
"    border-right-color: rgb(67, 203, 0);\n"
"    border-bottom-color: rgb(67, 203, 0);\n"
"}\n"
"#button_command:pressed{\n"
"    background-color: rgb(85, 255, 0);\n"
"}")
        self.button_command.setObjectName("button_command")
        self.lineEdit_ChangeCommand = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_ChangeCommand.setGeometry(QtCore.QRect(310, 370, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_ChangeCommand.setFont(font)
        self.lineEdit_ChangeCommand.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_ChangeCommand.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ChangeCommand.setObjectName("lineEdit_ChangeCommand")
        self.checkBox_cinDir = QtGui.QCheckBox(self.frame_command1)
        self.checkBox_cinDir.setGeometry(QtCore.QRect(12, 26, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_cinDir.setFont(font)
        self.checkBox_cinDir.setObjectName("checkBox_cinDir")
        self.lineEdit_y = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_y.setGeometry(QtCore.QRect(45, 80, 130, 20))
        self.lineEdit_y.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.label_z = QtGui.QLabel(self.frame_command1)
        self.label_z.setGeometry(QtCore.QRect(190, 106, 56, 20))
        self.label_z.setAlignment(QtCore.Qt.AlignCenter)
        self.label_z.setObjectName("label_z")
        self.label_6 = QtGui.QLabel(self.frame_command1)
        self.label_6.setGeometry(QtCore.QRect(10, 5, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_x = QtGui.QLabel(self.frame_command1)
        self.label_x.setGeometry(QtCore.QRect(190, 54, 56, 20))
        self.label_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x.setObjectName("label_x")
        self.checkBox_cinInv = QtGui.QCheckBox(self.frame_command1)
        self.checkBox_cinInv.setGeometry(QtCore.QRect(12, 136, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_cinInv.setFont(font)
        self.checkBox_cinInv.setObjectName("checkBox_cinInv")
        self.EStop = QtGui.QPushButton(self.frame_command1)
        self.EStop.setGeometry(QtCore.QRect(12, 296, 411, 60))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.EStop.setFont(font)
        self.EStop.setStyleSheet("#EStop {\n"
"border: 2px solid;\n"
"border-radius: 6px;\n"
"\n"
"color: red;\n"
"    border-top-color: rgb(255, 0, 0);\n"
"    border-right-color: rgb(202, 0, 0);\n"
"    border-bottom-color: rgb(202, 0, 0);\n"
"    border-left-color: rgb(255, 0, 0);\n"
"background-color: pink;\n"
"}\n"
"#EStop:pressed \n"
"{ \n"
"background-color: white;\n"
"}")
        self.EStop.setObjectName("EStop")
        self.label_theta3 = QtGui.QLabel(self.frame_command1)
        self.label_theta3.setGeometry(QtCore.QRect(190, 216, 56, 20))
        self.label_theta3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theta3.setObjectName("label_theta3")
        self.lineEdit_z = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_z.setGeometry(QtCore.QRect(45, 106, 130, 20))
        self.lineEdit_z.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_z.setObjectName("lineEdit_z")
        self.label_y = QtGui.QLabel(self.frame_command1)
        self.label_y.setGeometry(QtCore.QRect(190, 80, 56, 20))
        self.label_y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y.setObjectName("label_y")
        self.pushButton_Params = QtGui.QPushButton(self.frame_command1)
        self.pushButton_Params.setGeometry(QtCore.QRect(12, 256, 411, 26))
        self.pushButton_Params.setObjectName("pushButton_Params")
        self.label_theta2 = QtGui.QLabel(self.frame_command1)
        self.label_theta2.setGeometry(QtCore.QRect(190, 190, 56, 20))
        self.label_theta2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theta2.setObjectName("label_theta2")
        self.button_command_Stop = QtGui.QPushButton(self.frame_command1)
        self.button_command_Stop.setGeometry(QtCore.QRect(323, 510, 100, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_command_Stop.setFont(font)
        self.button_command_Stop.setStyleSheet("#button_command_Stop{\n"
"border: 2px solid ;\n"
"background-color: white;\n"
"    border-top-color: rgb(116, 116, 116);\n"
"    border-left-color: rgb(116, 116, 116);\n"
"    border-right-color: rgb(11, 11, 11);\n"
"    border-bottom-color: rgb(11, 11, 11);\n"
"\n"
"}\n"
"#button_command_Stop:pressed{\n"
"    \n"
"    color:rgb(255, 255, 255);\n"
"    border-color: rgb(255, 0, 0);\n"
"    background-color: rgb(184, 184, 184);\n"
"}")
        self.button_command_Stop.setObjectName("button_command_Stop")
        self.label_2 = QtGui.QLabel(self.frame_command1)
        self.label_2.setGeometry(QtCore.QRect(12, 370, 301, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_x_confirmed = QtGui.QLabel(self.frame_command1)
        self.label_x_confirmed.setGeometry(QtCore.QRect(260, 54, 130, 20))
        self.label_x_confirmed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(111, 111, 111);")
        self.label_x_confirmed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x_confirmed.setObjectName("label_x_confirmed")
        self.label_y_confirmed = QtGui.QLabel(self.frame_command1)
        self.label_y_confirmed.setGeometry(QtCore.QRect(260, 80, 130, 20))
        self.label_y_confirmed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_y_confirmed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y_confirmed.setObjectName("label_y_confirmed")
        self.label_z_confirmed = QtGui.QLabel(self.frame_command1)
        self.label_z_confirmed.setGeometry(QtCore.QRect(260, 106, 130, 20))
        self.label_z_confirmed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_z_confirmed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_z_confirmed.setObjectName("label_z_confirmed")
        self.label_commandNumber = QtGui.QLabel(self.frame_command1)
        self.label_commandNumber.setGeometry(QtCore.QRect(260, 510, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_commandNumber.setFont(font)
        self.label_commandNumber.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border-color: rgb(111, 111, 111);")
        self.label_commandNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.label_commandNumber.setObjectName("label_commandNumber")
        self.button_sendCommandNb = QtGui.QPushButton(self.frame_command1)
        self.button_sendCommandNb.setGeometry(QtCore.QRect(372, 370, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_sendCommandNb.setFont(font)
        self.button_sendCommandNb.setObjectName("button_sendCommandNb")
        self.lineEdit_theta1 = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_theta1.setGeometry(QtCore.QRect(45, 164, 130, 20))
        self.lineEdit_theta1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_theta1.setObjectName("lineEdit_theta1")
        self.label_theta1_confirmed = QtGui.QLabel(self.frame_command1)
        self.label_theta1_confirmed.setGeometry(QtCore.QRect(260, 164, 130, 20))
        self.label_theta1_confirmed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_theta1_confirmed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theta1_confirmed.setObjectName("label_theta1_confirmed")
        self.label_7 = QtGui.QLabel(self.frame_command1)
        self.label_7.setGeometry(QtCore.QRect(20, 395, 291, 106))
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.lineEdit_theta2 = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_theta2.setGeometry(QtCore.QRect(45, 190, 130, 20))
        self.lineEdit_theta2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_theta2.setObjectName("lineEdit_theta2")
        self.lineEdit_theta3 = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_theta3.setGeometry(QtCore.QRect(45, 216, 130, 20))
        self.lineEdit_theta3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_theta3.setObjectName("lineEdit_theta3")
        self.label_theta2_confirmed = QtGui.QLabel(self.frame_command1)
        self.label_theta2_confirmed.setGeometry(QtCore.QRect(260, 190, 130, 20))
        self.label_theta2_confirmed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_theta2_confirmed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theta2_confirmed.setObjectName("label_theta2_confirmed")
        self.label_theta3_confirmed = QtGui.QLabel(self.frame_command1)
        self.label_theta3_confirmed.setGeometry(QtCore.QRect(260, 216, 130, 20))
        self.label_theta3_confirmed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_theta3_confirmed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_theta3_confirmed.setObjectName("label_theta3_confirmed")
        self.label_11 = QtGui.QLabel(self.frame_command1)
        self.label_11.setGeometry(QtCore.QRect(350, 70, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.buttonUpdatePort = QtGui.QPushButton(self.centralwidget)
        self.buttonUpdatePort.setGeometry(QtCore.QRect(350, 10, 93, 30))
        self.buttonUpdatePort.setObjectName("buttonUpdatePort")
        self.frame_ManJog = QtGui.QFrame(self.centralwidget)
        self.frame_ManJog.setGeometry(QtCore.QRect(470, 50, 301, 321))
        self.frame_ManJog.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_ManJog.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_ManJog.setObjectName("frame_ManJog")
        self.label_12 = QtGui.QLabel(self.frame_ManJog)
        self.label_12.setGeometry(QtCore.QRect(0, 5, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_ManJog_Motor1 = QtGui.QLabel(self.frame_ManJog)
        self.label_ManJog_Motor1.setGeometry(QtCore.QRect(10, 170, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_ManJog_Motor1.setFont(font)
        self.label_ManJog_Motor1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ManJog_Motor1.setObjectName("label_ManJog_Motor1")
        self.label_ManJog_theta2 = QtGui.QLabel(self.frame_ManJog)
        self.label_ManJog_theta2.setGeometry(QtCore.QRect(90, 170, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_ManJog_theta2.setFont(font)
        self.label_ManJog_theta2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ManJog_theta2.setObjectName("label_ManJog_theta2")
        self.label_ManJog_theta3 = QtGui.QLabel(self.frame_ManJog)
        self.label_ManJog_theta3.setGeometry(QtCore.QRect(170, 170, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_ManJog_theta3.setFont(font)
        self.label_ManJog_theta3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ManJog_theta3.setObjectName("label_ManJog_theta3")
        self.label_ManJog_Increments = QtGui.QLabel(self.frame_ManJog)
        self.label_ManJog_Increments.setGeometry(QtCore.QRect(70, 270, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_ManJog_Increments.setFont(font)
        self.label_ManJog_Increments.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ManJog_Increments.setObjectName("label_ManJog_Increments")
        self.lineEdit_ManJog_increments = QtGui.QLineEdit(self.frame_ManJog)
        self.lineEdit_ManJog_increments.setGeometry(QtCore.QRect(180, 270, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_ManJog_increments.setFont(font)
        self.lineEdit_ManJog_increments.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_ManJog_increments.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ManJog_increments.setObjectName("lineEdit_ManJog_increments")
        self.pushButton_ManJog_up = QtGui.QPushButton(self.frame_ManJog)
        self.pushButton_ManJog_up.setGeometry(QtCore.QRect(50, 200, 211, 28))
        self.pushButton_ManJog_up.setObjectName("pushButton_ManJog_up")
        self.pushButton_ManJog_dwn = QtGui.QPushButton(self.frame_ManJog)
        self.pushButton_ManJog_dwn.setGeometry(QtCore.QRect(50, 230, 211, 28))
        self.pushButton_ManJog_dwn.setObjectName("pushButton_ManJog_dwn")
        self.Slider_ManJog_theta1 = QtGui.QSlider(self.frame_ManJog)
        self.Slider_ManJog_theta1.setGeometry(QtCore.QRect(40, 40, 22, 131))
        self.Slider_ManJog_theta1.setOrientation(QtCore.Qt.Vertical)
        self.Slider_ManJog_theta1.setObjectName("Slider_ManJog_theta1")
        self.Slider_ManJog_theta2 = QtGui.QSlider(self.frame_ManJog)
        self.Slider_ManJog_theta2.setGeometry(QtCore.QRect(120, 40, 22, 131))
        self.Slider_ManJog_theta2.setOrientation(QtCore.Qt.Vertical)
        self.Slider_ManJog_theta2.setObjectName("Slider_ManJog_theta2")
        self.Slider_ManJog_theta3 = QtGui.QSlider(self.frame_ManJog)
        self.Slider_ManJog_theta3.setGeometry(QtCore.QRect(200, 40, 22, 131))
        self.Slider_ManJog_theta3.setOrientation(QtCore.Qt.Vertical)
        self.Slider_ManJog_theta3.setObjectName("Slider_ManJog_theta3")
        self.pushButton_ManJog_Max = QtGui.QPushButton(self.frame_ManJog)
        self.pushButton_ManJog_Max.setGeometry(QtCore.QRect(240, 37, 51, 21))
        self.pushButton_ManJog_Max.setObjectName("pushButton_ManJog_Max")
        self.lineEdit_ManJog_Max = QtGui.QLineEdit(self.frame_ManJog)
        self.lineEdit_ManJog_Max.setGeometry(QtCore.QRect(240, 60, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_ManJog_Max.setFont(font)
        self.lineEdit_ManJog_Max.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_ManJog_Max.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ManJog_Max.setObjectName("lineEdit_ManJog_Max")
        self.lineEdit_ManJog_Min = QtGui.QLineEdit(self.frame_ManJog)
        self.lineEdit_ManJog_Min.setGeometry(QtCore.QRect(240, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_ManJog_Min.setFont(font)
        self.lineEdit_ManJog_Min.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_ManJog_Min.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ManJog_Min.setObjectName("lineEdit_ManJog_Min")
        self.pushButton_ManJog_Min = QtGui.QPushButton(self.frame_ManJog)
        self.pushButton_ManJog_Min.setGeometry(QtCore.QRect(240, 153, 51, 21))
        self.pushButton_ManJog_Min.setObjectName("pushButton_ManJog_Min")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 26))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtGui.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_theta1.setText(QtGui.QApplication.translate("MainWindow", "theta1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_x.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_command.setText(QtGui.QApplication.translate("MainWindow", "Start Command", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ChangeCommand.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_cinDir.setText(QtGui.QApplication.translate("MainWindow", "Cinematique directe", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_y.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_z.setText(QtGui.QApplication.translate("MainWindow", "z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cinematique</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_x.setText(QtGui.QApplication.translate("MainWindow", "x", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_cinInv.setText(QtGui.QApplication.translate("MainWindow", "Cinematique inverse", None, QtGui.QApplication.UnicodeUTF8))
        self.EStop.setWhatsThis(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Stop</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.EStop.setText(QtGui.QApplication.translate("MainWindow", "Arrêt d\'urgence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_theta3.setText(QtGui.QApplication.translate("MainWindow", "theta3", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_z.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_y.setText(QtGui.QApplication.translate("MainWindow", "y", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Params.setText(QtGui.QApplication.translate("MainWindow", "Envoie Parametres", None, QtGui.QApplication.UnicodeUTF8))
        self.label_theta2.setText(QtGui.QApplication.translate("MainWindow", "theta2", None, QtGui.QApplication.UnicodeUTF8))
        self.button_command_Stop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">This is the command manager :</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_x_confirmed.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_y_confirmed.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_z_confirmed.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_commandNumber.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sendCommandNb.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_theta1.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_theta1_confirmed.setText(QtGui.QApplication.translate("MainWindow", "2000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">- 1 : Go to home (2000/1750)</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">- 2 : Déplacement cartésien préenregistrer</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">- 3 : Déplacement </span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">- 4 : Mouvement en boucle 1</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">- 5 : Mouvement en boucle 2</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_theta2.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_theta3.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_theta2_confirmed.setText(QtGui.QApplication.translate("MainWindow", "2000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_theta3_confirmed.setText(QtGui.QApplication.translate("MainWindow", "2000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Cinematique", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUpdatePort.setText(QtGui.QApplication.translate("MainWindow", "Update Ports", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Manual Jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ManJog_Motor1.setText(QtGui.QApplication.translate("MainWindow", "Theta1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ManJog_theta2.setText(QtGui.QApplication.translate("MainWindow", "Theta2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ManJog_theta3.setText(QtGui.QApplication.translate("MainWindow", "Theta3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ManJog_Increments.setText(QtGui.QApplication.translate("MainWindow", "Incréments :", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ManJog_increments.setText(QtGui.QApplication.translate("MainWindow", "100", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ManJog_up.setText(QtGui.QApplication.translate("MainWindow", "UP", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ManJog_dwn.setText(QtGui.QApplication.translate("MainWindow", "DOWN", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ManJog_Max.setText(QtGui.QApplication.translate("MainWindow", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ManJog_Max.setText(QtGui.QApplication.translate("MainWindow", "2400", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ManJog_Min.setText(QtGui.QApplication.translate("MainWindow", "1000", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ManJog_Min.setText(QtGui.QApplication.translate("MainWindow", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOption.setTitle(QtGui.QApplication.translate("MainWindow", "Option", None, QtGui.QApplication.UnicodeUTF8))

