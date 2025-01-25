# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Prototype_001YmWkjv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

# import source_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(303, 9, 674, 95))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 654, 75))
        font = QFont()
        font.setFamily(u"Inter")
        font.setPointSize(46)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 110, 1261, 581))
        self.frame_2.setMinimumSize(QSize(1261, 581))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(1020, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(406, 86))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(144, 40))

        self.verticalLayout_2.addWidget(self.label_3)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(406, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.pushButton_3.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.frame_8)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setMaximumSize(QSize(30, 30))
        self.pushButton_5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setMaximumSize(QSize(30, 30))
        self.pushButton_4.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.frame_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.horizontalSlider = QSlider(self.frame_8)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.horizontalSlider)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(406, 86))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(144, 40))

        self.verticalLayout_3.addWidget(self.label_4)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(406, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        self.pushButton_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        self.pushButton_7.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        self.pushButton_8.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_9)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        self.pushButton_9.setFont(font1)

        self.horizontalLayout_6.addWidget(self.pushButton_9)

        self.horizontalSlider_2 = QSlider(self.frame_9)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider_2)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(98, 98))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.graphicsView = QGraphicsView(self.frame_5)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMaximumSize(QSize(662, 426))

        self.horizontalLayout_7.addWidget(self.graphicsView)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(297, 16777215))
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.graphicsView_2 = QGraphicsView(self.frame_10)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setMaximumSize(QSize(297, 196))

        self.verticalLayout_4.addWidget(self.graphicsView_2)

        self.graphicsView_3 = QGraphicsView(self.frame_10)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setMaximumSize(QSize(297, 196))

        self.verticalLayout_4.addWidget(self.graphicsView_3)


        self.horizontalLayout_7.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.result_box = QFrame(self.frame_2)
        self.result_box.setObjectName(u"result_box")
        self.result_box.setEnabled(True)
        self.result_box.setMaximumSize(QSize(207, 543))
        self.result_box.setStyleSheet(u"#result_box{\n"
"		background-image: url(:/images/Rectangle 10.png);\n"
"}")
        self.result_box.setFrameShape(QFrame.NoFrame)
        self.result_box.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.result_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 95, 34))
        font2 = QFont()
        font2.setFamily(u"Inter")
        font2.setPointSize(18)
        self.label_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.result_box)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Water Level Detection", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"rec", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"pl", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"op", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"rec", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"pl", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"st", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"op", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Result :", None))
    # retranslateUi

