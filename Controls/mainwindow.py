# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1028, 724)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(341, 201, 0, 0))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 9, 80, 20))
        self.JsonKey = QLineEdit(self.centralwidget)
        self.JsonKey.setObjectName(u"JsonKey")
        self.JsonKey.setGeometry(QRect(120, 40, 221, 20))
        self.JsonKey.setAlignment(Qt.AlignCenter)
        self.comboBoxPort = QComboBox(self.centralwidget)
        self.comboBoxPort.setObjectName(u"comboBoxPort")
        self.comboBoxPort.setGeometry(QRect(200, 10, 235, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 40, 241, 20))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.graph = QGraphicsView(self.centralwidget)
        self.graph.setObjectName(u"graph")
        self.graph.setGeometry(QRect(10, 70, 331, 191))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 101, 20))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(350, 70, 251, 191))
        font = QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.frame_vision = QFrame(self.centralwidget)
        self.frame_vision.setObjectName(u"frame_vision")
        self.frame_vision.setGeometry(QRect(10, 280, 591, 301))
        self.frame_vision.setFrameShape(QFrame.StyledPanel)
        self.frame_vision.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_vision)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 0, 59, 17))
        self.frame_command1 = QFrame(self.centralwidget)
        self.frame_command1.setObjectName(u"frame_command1")
        self.frame_command1.setGeometry(QRect(610, 0, 321, 581))
        self.frame_command1.setStyleSheet(u"")
        self.frame_command1.setFrameShape(QFrame.StyledPanel)
        self.frame_command1.setFrameShadow(QFrame.Raised)
        self.label_theta1 = QLabel(self.frame_command1)
        self.label_theta1.setObjectName(u"label_theta1")
        self.label_theta1.setGeometry(QRect(10, 164, 56, 20))
        self.label_theta1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_x = QLineEdit(self.frame_command1)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        self.lineEdit_x.setGeometry(QRect(72, 54, 91, 20))
        self.lineEdit_x.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.button_command = QPushButton(self.frame_command1)
        self.button_command.setObjectName(u"button_command")
        self.button_command.setGeometry(QRect(12, 506, 151, 61))
        font1 = QFont()
        font1.setPointSize(11)
        self.button_command.setFont(font1)
        self.button_command.setStyleSheet(u"#button_command{\n"
"border: 2px solid;\n"
"background-color: white;\n"
"	border-top-color: rgb(85, 255, 0);\n"
"	border-left-color: rgb(85, 255, 0);\n"
"	border-right-color: rgb(67, 203, 0);\n"
"	border-bottom-color: rgb(67, 203, 0);\n"
"}\n"
"#button_command:pressed{\n"
"	background-color: rgb(85, 255, 0);\n"
"}")
        self.lineEdit_command = QLineEdit(self.frame_command1)
        self.lineEdit_command.setObjectName(u"lineEdit_command")
        self.lineEdit_command.setGeometry(QRect(200, 370, 41, 41))
        self.lineEdit_command.setFont(font1)
        self.lineEdit_command.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_command.setAlignment(Qt.AlignCenter)
        self.checkBox_cinDir = QCheckBox(self.frame_command1)
        self.checkBox_cinDir.setObjectName(u"checkBox_cinDir")
        self.checkBox_cinDir.setGeometry(QRect(12, 26, 291, 20))
        self.checkBox_cinDir.setFont(font)
        self.lineEdit_y = QLineEdit(self.frame_command1)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        self.lineEdit_y.setGeometry(QRect(72, 80, 91, 20))
        self.lineEdit_y.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_z = QLabel(self.frame_command1)
        self.label_z.setObjectName(u"label_z")
        self.label_z.setGeometry(QRect(10, 106, 56, 20))
        self.label_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.frame_command1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 5, 296, 20))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_theta1 = QLineEdit(self.frame_command1)
        self.lineEdit_theta1.setObjectName(u"lineEdit_theta1")
        self.lineEdit_theta1.setGeometry(QRect(72, 164, 234, 20))
        self.lineEdit_theta1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_x = QLabel(self.frame_command1)
        self.label_x.setObjectName(u"label_x")
        self.label_x.setGeometry(QRect(10, 54, 56, 20))
        self.label_x.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_3 = QFrame(self.frame_command1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1, 5, 3, 560))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.checkBox_cinInv = QCheckBox(self.frame_command1)
        self.checkBox_cinInv.setObjectName(u"checkBox_cinInv")
        self.checkBox_cinInv.setGeometry(QRect(12, 136, 291, 20))
        self.checkBox_cinInv.setFont(font)
        self.EStop = QPushButton(self.frame_command1)
        self.EStop.setObjectName(u"EStop")
        self.EStop.setGeometry(QRect(12, 296, 296, 60))
        font2 = QFont()
        font2.setPointSize(22)
        self.EStop.setFont(font2)
        self.EStop.setStyleSheet(u"#EStop {\n"
"border: 2px solid;\n"
"border-radius: 6px;\n"
"\n"
"color: red;\n"
"	border-top-color: rgb(255, 0, 0);\n"
"	border-right-color: rgb(202, 0, 0);\n"
"	border-bottom-color: rgb(202, 0, 0);\n"
"	border-left-color: rgb(255, 0, 0);\n"
"background-color: pink;\n"
"}\n"
"#EStop:pressed \n"
"{ \n"
"background-color: white;\n"
"}")
        self.label_theta3 = QLabel(self.frame_command1)
        self.label_theta3.setObjectName(u"label_theta3")
        self.label_theta3.setGeometry(QRect(10, 216, 56, 20))
        self.label_theta3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_theta2 = QLineEdit(self.frame_command1)
        self.lineEdit_theta2.setObjectName(u"lineEdit_theta2")
        self.lineEdit_theta2.setGeometry(QRect(72, 190, 234, 20))
        self.lineEdit_theta2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_theta3 = QLineEdit(self.frame_command1)
        self.lineEdit_theta3.setObjectName(u"lineEdit_theta3")
        self.lineEdit_theta3.setGeometry(QRect(72, 216, 234, 20))
        self.lineEdit_theta3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_z = QLineEdit(self.frame_command1)
        self.lineEdit_z.setObjectName(u"lineEdit_z")
        self.lineEdit_z.setGeometry(QRect(72, 106, 91, 20))
        self.lineEdit_z.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_y = QLabel(self.frame_command1)
        self.label_y.setObjectName(u"label_y")
        self.label_y.setGeometry(QRect(10, 80, 56, 20))
        self.label_y.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_Params = QPushButton(self.frame_command1)
        self.pushButton_Params.setObjectName(u"pushButton_Params")
        self.pushButton_Params.setGeometry(QRect(12, 256, 296, 23))
        self.label_theta2 = QLabel(self.frame_command1)
        self.label_theta2.setObjectName(u"label_theta2")
        self.label_theta2.setGeometry(QRect(10, 190, 56, 20))
        self.label_theta2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.button_command_Stop = QPushButton(self.frame_command1)
        self.button_command_Stop.setObjectName(u"button_command_Stop")
        self.button_command_Stop.setGeometry(QRect(227, 506, 81, 61))
        font3 = QFont()
        font3.setPointSize(14)
        self.button_command_Stop.setFont(font3)
        self.button_command_Stop.setStyleSheet(u"#button_command_Stop{\n"
"border: 2px solid ;\n"
"background-color: white;\n"
"	border-top-color: rgb(116, 116, 116);\n"
"	border-left-color: rgb(116, 116, 116);\n"
"	border-right-color: rgb(11, 11, 11);\n"
"	border-bottom-color: rgb(11, 11, 11);\n"
"\n"
"}\n"
"#button_command_Stop:pressed{\n"
"	\n"
"	color:rgb(255, 255, 255);\n"
"	border-color: rgb(255, 0, 0);\n"
"	background-color: rgb(184, 184, 184);\n"
"}")
        self.label_2 = QLabel(self.frame_command1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 370, 296, 131))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_x_confimed = QLabel(self.frame_command1)
        self.label_x_confimed.setObjectName(u"label_x_confimed")
        self.label_x_confimed.setGeometry(QRect(200, 54, 91, 20))
        self.label_x_confimed.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(111, 111, 111);")
        self.label_x_confimed.setAlignment(Qt.AlignCenter)
        self.label_y_confimed = QLabel(self.frame_command1)
        self.label_y_confimed.setObjectName(u"label_y_confimed")
        self.label_y_confimed.setGeometry(QRect(200, 80, 91, 20))
        self.label_y_confimed.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(111, 111, 111);")
        self.label_y_confimed.setAlignment(Qt.AlignCenter)
        self.label_z_confimed = QLabel(self.frame_command1)
        self.label_z_confimed.setObjectName(u"label_z_confimed")
        self.label_z_confimed.setGeometry(QRect(200, 106, 91, 20))
        self.label_z_confimed.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid;\n"
"border-color: rgb(111, 111, 111);")
        self.label_z_confimed.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.frame_command1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 506, 51, 61))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border-color: rgb(111, 111, 111);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.button_send = QPushButton(self.frame_command1)
        self.button_send.setObjectName(u"button_send")
        self.button_send.setGeometry(QRect(250, 370, 51, 41))
        self.button_send.setFont(font1)
        self.label_2.raise_()
        self.label_theta1.raise_()
        self.lineEdit_x.raise_()
        self.button_command.raise_()
        self.lineEdit_command.raise_()
        self.checkBox_cinDir.raise_()
        self.lineEdit_y.raise_()
        self.label_z.raise_()
        self.label_6.raise_()
        self.lineEdit_theta1.raise_()
        self.label_x.raise_()
        self.line_3.raise_()
        self.checkBox_cinInv.raise_()
        self.EStop.raise_()
        self.label_theta3.raise_()
        self.lineEdit_theta2.raise_()
        self.lineEdit_theta3.raise_()
        self.lineEdit_z.raise_()
        self.label_y.raise_()
        self.pushButton_Params.raise_()
        self.label_theta2.raise_()
        self.button_command_Stop.raise_()
        self.label_x_confimed.raise_()
        self.label_y_confimed.raise_()
        self.label_z_confimed.raise_()
        self.label_7.raise_()
        self.button_send.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1028, 21))
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName(u"menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.JsonKey.setText(QCoreApplication.translate("MainWindow", u"flag", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Messages:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Donnees brutes:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"vision", None))
        self.label_theta1.setText(QCoreApplication.translate("MainWindow", u"theta1", None))
        self.lineEdit_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_command.setText(QCoreApplication.translate("MainWindow", u"Start Command", None))
        self.lineEdit_command.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.checkBox_cinDir.setText(QCoreApplication.translate("MainWindow", u"Cinematique directe", None))
        self.lineEdit_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_z.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cinematique", None))
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.checkBox_cinInv.setText(QCoreApplication.translate("MainWindow", u"Cinematique inverse", None))
#if QT_CONFIG(whatsthis)
        self.EStop.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Stop</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.EStop.setText(QCoreApplication.translate("MainWindow", u"Arr\u00eat d'urgence", None))
        self.label_theta3.setText(QCoreApplication.translate("MainWindow", u"theta3", None))
        self.lineEdit_z.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.pushButton_Params.setText(QCoreApplication.translate("MainWindow", u"Envoie Parametres", None))
        self.label_theta2.setText(QCoreApplication.translate("MainWindow", u"theta2", None))
        self.button_command_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">This is the command manager :</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">- 1 : Start/Stop to position</span></p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">- 2 : Manual jog</span></p></body></html>", None))
        self.label_x_confimed.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_y_confimed.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_z_confimed.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.menuOption.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
    # retranslateUi

