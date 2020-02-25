# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created: Sat Feb 22 17:39:05 2020
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1028, 724)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(341, 201, 0, 0))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 9, 80, 20))
        self.label_5.setObjectName("label_5")
        self.JsonKey = QtGui.QLineEdit(self.centralwidget)
        self.JsonKey.setGeometry(QtCore.QRect(120, 40, 221, 20))
        self.JsonKey.setAlignment(QtCore.Qt.AlignCenter)
        self.JsonKey.setObjectName("JsonKey")
        self.comboBoxPort = QtGui.QComboBox(self.centralwidget)
        self.comboBoxPort.setGeometry(QtCore.QRect(120, 10, 261, 20))
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 40, 241, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.graph = QtGui.QGraphicsView(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(10, 70, 331, 191))
        self.graph.setObjectName("graph")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(350, 70, 251, 191))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.frame_vision = QtGui.QFrame(self.centralwidget)
        self.frame_vision.setGeometry(QtCore.QRect(10, 280, 591, 281))
        self.frame_vision.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_vision.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_vision.setObjectName("frame_vision")
        self.label = QtGui.QLabel(self.frame_vision)
        self.label.setGeometry(QtCore.QRect(260, 0, 59, 17))
        self.label.setObjectName("label")
        self.frame_command1 = QtGui.QFrame(self.centralwidget)
        self.frame_command1.setGeometry(QtCore.QRect(610, 0, 311, 581))
        self.frame_command1.setStyleSheet("")
        self.frame_command1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_command1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_command1.setObjectName("frame_command1")
        self.label_theta1 = QtGui.QLabel(self.frame_command1)
        self.label_theta1.setGeometry(QtCore.QRect(10, 164, 56, 20))
        self.label_theta1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_theta1.setObjectName("label_theta1")
        self.lineEdit_x = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_x.setGeometry(QtCore.QRect(72, 54, 91, 20))
        self.lineEdit_x.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.button_command = QtGui.QPushButton(self.frame_command1)
        self.button_command.setGeometry(QtCore.QRect(12, 506, 151, 61))
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
        self.lineEdit_ChangeCommand.setGeometry(QtCore.QRect(200, 370, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_ChangeCommand.setFont(font)
        self.lineEdit_ChangeCommand.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_ChangeCommand.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ChangeCommand.setObjectName("lineEdit_ChangeCommand")
        self.checkBox_cinDir = QtGui.QCheckBox(self.frame_command1)
        self.checkBox_cinDir.setGeometry(QtCore.QRect(12, 26, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_cinDir.setFont(font)
        self.checkBox_cinDir.setObjectName("checkBox_cinDir")
        self.lineEdit_y = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_y.setGeometry(QtCore.QRect(72, 80, 91, 20))
        self.lineEdit_y.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.label_z = QtGui.QLabel(self.frame_command1)
        self.label_z.setGeometry(QtCore.QRect(10, 106, 56, 20))
        self.label_z.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_z.setObjectName("label_z")
        self.label_6 = QtGui.QLabel(self.frame_command1)
        self.label_6.setGeometry(QtCore.QRect(10, 5, 296, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.lineEdit_theta1 = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_theta1.setGeometry(QtCore.QRect(72, 164, 234, 20))
        self.lineEdit_theta1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_theta1.setObjectName("lineEdit_theta1")
        self.label_x = QtGui.QLabel(self.frame_command1)
        self.label_x.setGeometry(QtCore.QRect(10, 54, 56, 20))
        self.label_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_x.setObjectName("label_x")
        self.line_3 = QtGui.QFrame(self.frame_command1)
        self.line_3.setGeometry(QtCore.QRect(1, 5, 3, 560))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.checkBox_cinInv = QtGui.QCheckBox(self.frame_command1)
        self.checkBox_cinInv.setGeometry(QtCore.QRect(12, 136, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox_cinInv.setFont(font)
        self.checkBox_cinInv.setObjectName("checkBox_cinInv")
        self.EStop = QtGui.QPushButton(self.frame_command1)
        self.EStop.setGeometry(QtCore.QRect(12, 296, 296, 60))
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
        self.label_theta3.setGeometry(QtCore.QRect(10, 216, 56, 20))
        self.label_theta3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_theta3.setObjectName("label_theta3")
        self.lineEdit_theta2 = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_theta2.setGeometry(QtCore.QRect(72, 190, 234, 20))
        self.lineEdit_theta2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_theta2.setObjectName("lineEdit_theta2")
        self.lineEdit_theta3 = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_theta3.setGeometry(QtCore.QRect(72, 216, 234, 20))
        self.lineEdit_theta3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_theta3.setObjectName("lineEdit_theta3")
        self.lineEdit_z = QtGui.QLineEdit(self.frame_command1)
        self.lineEdit_z.setGeometry(QtCore.QRect(72, 106, 91, 20))
        self.lineEdit_z.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_z.setObjectName("lineEdit_z")
        self.label_y = QtGui.QLabel(self.frame_command1)
        self.label_y.setGeometry(QtCore.QRect(10, 80, 56, 20))
        self.label_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_y.setObjectName("label_y")
        self.pushButton_Params = QtGui.QPushButton(self.frame_command1)
        self.pushButton_Params.setGeometry(QtCore.QRect(12, 256, 296, 23))
        self.pushButton_Params.setObjectName("pushButton_Params")
        self.label_theta2 = QtGui.QLabel(self.frame_command1)
        self.label_theta2.setGeometry(QtCore.QRect(10, 190, 56, 20))
        self.label_theta2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_theta2.setObjectName("label_theta2")
        self.button_command_Stop = QtGui.QPushButton(self.frame_command1)
        self.button_command_Stop.setGeometry(QtCore.QRect(227, 506, 81, 61))
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
        self.label_2.setGeometry(QtCore.QRect(12, 370, 181, 131))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_x_confimed = QtGui.QLabel(self.frame_command1)
        self.label_x_confimed.setGeometry(QtCore.QRect(200, 54, 91, 20))
        self.label_x_confimed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(111, 111, 111);")
        self.label_x_confimed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x_confimed.setObjectName("label_x_confimed")
        self.label_y_confimed = QtGui.QLabel(self.frame_command1)
        self.label_y_confimed.setGeometry(QtCore.QRect(200, 80, 91, 20))
        self.label_y_confimed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(111, 111, 111);")
        self.label_y_confimed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y_confimed.setObjectName("label_y_confimed")
        self.label_z_confimed = QtGui.QLabel(self.frame_command1)
        self.label_z_confimed.setGeometry(QtCore.QRect(200, 106, 91, 20))
        self.label_z_confimed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(111, 111, 111);")
        self.label_z_confimed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_z_confimed.setObjectName("label_z_confimed")
        self.label_commandNumber = QtGui.QLabel(self.frame_command1)
        self.label_commandNumber.setGeometry(QtCore.QRect(170, 506, 51, 61))
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
        self.button_sendCommandNb.setGeometry(QtCore.QRect(250, 370, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_sendCommandNb.setFont(font)
        self.button_sendCommandNb.setObjectName("button_sendCommandNb")
        self.buttonUpdatePort = QtGui.QPushButton(self.centralwidget)
        self.buttonUpdatePort.setGeometry(QtCore.QRect(410, 5, 93, 30))
        self.buttonUpdatePort.setObjectName("buttonUpdatePort")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 26))
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
        self.JsonKey.setText(QtGui.QApplication.translate("MainWindow", "flag", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Messages:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Donnees brutes:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "vision", None, QtGui.QApplication.UnicodeUTF8))
        self.label_theta1.setText(QtGui.QApplication.translate("MainWindow", "theta1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_x.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.button_command.setText(QtGui.QApplication.translate("MainWindow", "Start Command", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ChangeCommand.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_cinDir.setText(QtGui.QApplication.translate("MainWindow", "Cinematique directe", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_y.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_z.setText(QtGui.QApplication.translate("MainWindow", "z", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Cinematique", None, QtGui.QApplication.UnicodeUTF8))
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
"<p align=\"center\" style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">This is the command</span></p>\n"
"<p align=\"center\" style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">manager :</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt;\">- 1 : Start/Stop to position</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt;\">- 2 : Manual jog</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_x_confimed.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_y_confimed.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_z_confimed.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_commandNumber.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.button_sendCommandNb.setText(QtGui.QApplication.translate("MainWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonUpdatePort.setText(QtGui.QApplication.translate("MainWindow", "Update Ports", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOption.setTitle(QtGui.QApplication.translate("MainWindow", "Option", None, QtGui.QApplication.UnicodeUTF8))

