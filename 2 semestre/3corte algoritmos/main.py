# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagina final de corteuBAlra.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 710)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, -90, 811, 791))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.483, y1:0, x2:0.492401, y2:1, stop:0 rgba(0, 71, 223, 255), stop:0.363636 rgba(96, 147, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border-radious:20px;\n"
"border: 1px solid #00007f;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 290, 121, 31))
        self.label.setStyleSheet(u"background-color: rgba(0, 0 ,0, 0%);\n"
"font: 75 12pt \"Arial\";\n"
"border:None;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 400, 131, 31))
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0 ,0, 0%);\n"
"font: 75 12pt \"Arial\";\n"
"border:None;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.usuarios = QLineEdit(self.frame)
        self.usuarios.setObjectName(u"usuarios")
        self.usuarios.setGeometry(QRect(310, 340, 171, 24))
        self.usuarios.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:None;")
        self.usuarios.setAlignment(Qt.AlignCenter)
        self.contrasena = QLineEdit(self.frame)
        self.contrasena.setObjectName(u"contrasena")
        self.contrasena.setGeometry(QRect(310, 440, 171, 24))
        self.contrasena.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:None;")
        self.contrasena.setAlignment(Qt.AlignCenter)
        self.salir = QPushButton(self.frame)
        self.salir.setObjectName(u"salir")
        self.salir.setGeometry(QRect(360, 700, 80, 24))
        self.salir.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0, 0%);	\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:reflect, x1:0.483, y1:0, x2:0.492401, y2:1, stop:0 rgba(0, 71, 223, 255), stop:0.363636 rgba(96, 147, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 0px;\n"
"}")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(200, 620, 411, 23))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	backgroud-color: rgba(0,0,0,0%);\n"
"	border-radius:25px;\n"
"border: 1px solid #00007f;\n"
"\n"
"\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.995263, y1:0.563, x2:0,y2:0.574, stop:0.301843 rgba(11, 255,240,255), stop:1 rgba(68, 0, 127, 255));\n"
"\n"
"	border-radious:25px;\n"
"\n"
"}")
        self.progressBar.setValue(0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 550, 181, 51))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 255, 0);	\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 5px solid #000000;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(255, 255, 0);\n"
"	font: 75 12pt \"MS Shell Dlg 2\";\n"
"border: 5px solid #ffffff;\n"
"}")
        self.usuario_incorrecto = QLabel(self.frame)
        self.usuario_incorrecto.setObjectName(u"usuario_incorrecto")
        self.usuario_incorrecto.setGeometry(QRect(340, 370, 121, 31))
        self.usuario_incorrecto.setStyleSheet(u"background-color: rgba(0, 0 ,0, 0%);\n"
"font: 75 10pt \"Arial\";\n"
"color: rgb(255, 0, 0);\n"
"border:None;")
        self.usuario_incorrecto.setAlignment(Qt.AlignCenter)
        self.contrasena_incorrecta = QLabel(self.frame)
        self.contrasena_incorrecta.setObjectName(u"contrasena_incorrecta")
        self.contrasena_incorrecta.setGeometry(QRect(340, 460, 121, 31))
        self.contrasena_incorrecta.setStyleSheet(u"background-color: rgba(0, 0 ,0, 0%);\n"
"font: 75 10pt \"Arial\";\n"
"color: rgb(255, 0, 0);\n"
"border:None;")
        self.contrasena_incorrecta.setAlignment(Qt.AlignCenter)
        self.cargando = QLabel(self.frame)
        self.cargando.setObjectName(u"cargando")
        self.cargando.setGeometry(QRect(360, 650, 91, 16))
        self.cargando.setStyleSheet(u"background-color: rgba(0, 0 ,0, 0%);\n"
"font: 75 10pt \"Arial\";\n"
"color: rgb(255, 0, 0);\n"
"border:None;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.salir.clicked.connect(self.frame.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CONTRASE\u00d1A", None))
        self.usuarios.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su usuario", None))
        self.contrasena.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese su contrase\u00f1a", None))
        self.salir.setText(QCoreApplication.translate("MainWindow", u"salir", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"INICIAR SESION", None))
        self.usuario_incorrecto.setText("")
        self.contrasena_incorrecta.setText("")
        self.cargando.setText("")
    # retranslateUi

