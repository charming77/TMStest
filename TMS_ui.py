# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TMS.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1011, 556)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(360, 470, 81, 41))
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(-10, 240, 621, 211))
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 72, 15))
        self.lineEdit_9 = QLineEdit(self.widget_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(80, 10, 421, 21))
        self.pushButton_6 = QPushButton(self.widget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(510, 10, 93, 28))
        self.textEdit_3 = QTextEdit(self.widget_4)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(80, 50, 421, 151))
        self.pushButton_7 = QPushButton(self.widget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(510, 50, 93, 28))
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 30, 72, 15))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 140, 591, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)

        self.textEdit_2 = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.horizontalLayout.addWidget(self.textEdit_2)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 90, 591, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.horizontalLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(20, 60, 589, 29))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_5.addWidget(self.lineEdit_2)

        self.horizontalSpacer = QSpacerItem(68, 24, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_6.addWidget(self.lineEdit_3)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(640, 60, 160, 82))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_8.addWidget(self.lineEdit_6)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_7.addWidget(self.lineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(820, 60, 160, 82))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_10.addWidget(self.lineEdit_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_9.addWidget(self.lineEdit_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(60, 470, 81, 41))
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(210, 470, 81, 41))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(810, 460, 201, 41))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(640, 140, 341, 321))
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(640, 150, 160, 296))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_3.addWidget(self.pushButton_19)

        self.pushButton_18 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_3.addWidget(self.pushButton_18)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_3.addWidget(self.pushButton_12)

        self.pushButton_14 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_3.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_3.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_3.addWidget(self.pushButton_16)

        self.pushButton_13 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_3.addWidget(self.pushButton_13)

        self.pushButton_20 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout_3.addWidget(self.pushButton_20)

        self.pushButton_17 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_3.addWidget(self.pushButton_17)

        self.pushButton_21 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.verticalLayout_3.addWidget(self.pushButton_21)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1011, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f4d\u673a\u6536\u53d1\u6570\u636e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Boot\u6587\u4ef6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165\u6587\u4ef6", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u7aef", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5199\u5165", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\uff1a", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001ID\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536ID\uff1a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u65e7\u7248\u672c\u53f7", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6\u7248\u672c\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u65b0\u7248\u672c\u53f7", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u786c\u4ef6\u7248\u672c\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u7248\u672c\uff1a", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005\uff1a\u90b5\u9038\u98de\uff0c\u5468\u5bb6\u5174", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Todo color list", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

