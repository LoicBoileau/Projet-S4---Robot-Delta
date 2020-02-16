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

#from QtCharts import QChartView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1095, 799)
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
        #self.graph = QChartView(self.centralwidget)
        #self.graph.setObjectName(u"graph")
        #self.graph.setGeometry(QRect(10, 70, 331, 191))
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
        self.frame_vision.setGeometry(QRect(10, 270, 591, 301))
        self.frame_vision.setFrameShape(QFrame.StyledPanel)
        self.frame_vision.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_vision)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 0, 59, 17))
        self.frame_command1 = QFrame(self.centralwidget)
        self.frame_command1.setObjectName(u"frame_command1")
        self.frame_command1.setGeometry(QRect(610, 0, 321, 571))
        self.frame_command1.setFrameShape(QFrame.StyledPanel)
        self.frame_command1.setFrameShadow(QFrame.Raised)
        self.label_theta1 = QLabel(self.frame_command1)
        self.label_theta1.setObjectName(u"label_theta1")
        self.label_theta1.setGeometry(QRect(10, 164, 56, 20))
        self.label_theta1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_x = QLineEdit(self.frame_command1)
        self.lineEdit_x.setObjectName(u"lineEdit_x")
        self.lineEdit_x.setGeometry(QRect(72, 54, 234, 20))
        self.button_command = QPushButton(self.frame_command1)
        self.button_command.setObjectName(u"button_command")
        self.button_command.setGeometry(QRect(12, 506, 151, 61))
        font1 = QFont()
        font1.setPointSize(11)
        self.button_command.setFont(font1)
        self.button_command.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"\n"
"background-color: white;\n"
"border-color: rgb(0, 255, 125);")
        self.lineEdit_command = QLineEdit(self.frame_command1)
        self.lineEdit_command.setObjectName(u"lineEdit_command")
        self.lineEdit_command.setGeometry(QRect(170, 506, 51, 61))
        self.lineEdit_command.setFont(font1)
        self.lineEdit_command.setAlignment(Qt.AlignCenter)
        self.checkBox_cinDir = QCheckBox(self.frame_command1)
        self.checkBox_cinDir.setObjectName(u"checkBox_cinDir")
        self.checkBox_cinDir.setGeometry(QRect(12, 26, 291, 20))
        self.lineEdit_y = QLineEdit(self.frame_command1)
        self.lineEdit_y.setObjectName(u"lineEdit_y")
        self.lineEdit_y.setGeometry(QRect(72, 80, 234, 20))
        self.label_z = QLabel(self.frame_command1)
        self.label_z.setObjectName(u"label_z")
        self.label_z.setGeometry(QRect(10, 106, 56, 20))
        self.label_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.frame_command1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 5, 296, 20))
        self.label_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_theta1 = QLineEdit(self.frame_command1)
        self.lineEdit_theta1.setObjectName(u"lineEdit_theta1")
        self.lineEdit_theta1.setGeometry(QRect(72, 164, 234, 20))
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
        self.EStop = QPushButton(self.frame_command1)
        self.EStop.setObjectName(u"EStop")
        self.EStop.setGeometry(QRect(12, 296, 296, 121))
        font2 = QFont()
        font2.setPointSize(22)
        self.EStop.setFont(font2)
        self.EStop.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"\n"
"border-color: red;\n"
"background-color: pink;\n"
"color: red;\n"
"\n"
"EStop{ background-color: white }")
        self.label_theta3 = QLabel(self.frame_command1)
        self.label_theta3.setObjectName(u"label_theta3")
        self.label_theta3.setGeometry(QRect(10, 216, 56, 20))
        self.label_theta3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_theta2 = QLineEdit(self.frame_command1)
        self.lineEdit_theta2.setObjectName(u"lineEdit_theta2")
        self.lineEdit_theta2.setGeometry(QRect(72, 190, 234, 20))
        self.lineEdit_theta3 = QLineEdit(self.frame_command1)
        self.lineEdit_theta3.setObjectName(u"lineEdit_theta3")
        self.lineEdit_theta3.setGeometry(QRect(72, 216, 234, 20))
        self.lineEdit_z = QLineEdit(self.frame_command1)
        self.lineEdit_z.setObjectName(u"lineEdit_z")
        self.lineEdit_z.setGeometry(QRect(72, 106, 234, 20))
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
        self.button_command_Stop.setStyleSheet(u"border: 2px solid #8f8f91;\n"
"background-color: white;\n"
"\n"
"")
        self.label_2 = QLabel(self.frame_command1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 430, 296, 71))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1095, 26))
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
        self.button_command.setText(QCoreApplication.translate("MainWindow", u"Start Command", None))
        self.lineEdit_command.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox_cinDir.setText(QCoreApplication.translate("MainWindow", u"Cinématique directe", None))
        self.label_z.setText(QCoreApplication.translate("MainWindow", u"z", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cinématique", None))
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.checkBox_cinInv.setText(QCoreApplication.translate("MainWindow", u"Cinématique inverse", None))
        self.EStop.setText(QCoreApplication.translate("MainWindow", u"Arrêt d'urgence", None))
        self.label_theta3.setText(QCoreApplication.translate("MainWindow", u"theta3", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.pushButton_Params.setText(QCoreApplication.translate("MainWindow", u"Envoie Parametres", None))
        self.label_theta2.setText(QCoreApplication.translate("MainWindow", u"theta2", None))
        self.button_command_Stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"This is the command manager :\n"
" - 1 : test\n"
" - 2 : ...", None))
        self.menuOption.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
    # retranslateUi

