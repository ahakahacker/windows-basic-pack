# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 301)
        MainWindow.setMinimumSize(QtCore.QSize(521, 271))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 32, 521, 271))
        self.frame.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 501, 251))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    border: none;\n"
"} \n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(76, 76, 76);\n"
"    color: white;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"    \n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"")
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("")
        self.tab_4.setObjectName("tab_4")
        self.frame_2 = QtWidgets.QFrame(self.tab_4)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 501, 221))
        self.frame_2.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 50, 461, 101))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 142, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 501, 221))
        self.frame_3.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(32)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 120, 461, 81))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(28)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(73, 73, 73);\n"
"border: none;\n"
"color: rgb(120, 120, 120);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 501, 221))
        self.frame_4.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(19)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 90, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(13)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 90, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_5 = QtWidgets.QFrame(self.tab_3)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 501, 221))
        self.frame_5.setStyleSheet("background-color: rgb(71, 71, 71);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_14.setGeometry(QtCore.QRect(20, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(14)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_11.setGeometry(QtCore.QRect(260, 90, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_10.setGeometry(QtCore.QRect(260, 160, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(13)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_12.setGeometry(QtCore.QRect(260, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(14)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 90, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(14)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton {\n"
"    background-color: rgb(76, 76, 76);\n"
"    border: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(260, 200, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(6)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 521, 32))
        self.frame_6.setStyleSheet("background-color: rgb(60, 60, 60);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_15.setGeometry(QtCore.QRect(483, 10, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Code Pro Black")
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("QPushButton:hover {\n"
"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(76, 76, 76);\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_16.setGeometry(QtCore.QRect(450, 10, 21, 20))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(13)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("QPushButton:hover {\n"
"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 149, 0);\n"
"}\n"
"QPushButton {\n"
"color: white;\n"
"border-radius: 10px;\n"
"background-color: rgb(76, 76, 76);\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 431, 16))
        font = QtGui.QFont()
        font.setFamily("Code Pro Bold")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WBP"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Windows Basic Pack</span></p><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">установи нужные компоненты в один клик</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#3a3a3a;\">это онлайн версия приложения т.е занимает мало места, но скачивает все</span></p><p align=\"center\"><span style=\" color:#3a3a3a;\">компоненты из интернета. вы можете скачать оффлайн версию</span></p><p align=\"center\"><span style=\" color:#3a3a3a;\">в релизе на github</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "веб установка"))
        self.pushButton_2.setText(_translate("MainWindow", "оффлайн установка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "DirectX"))
        self.pushButton_3.setText(_translate("MainWindow", "VC++ 2015, 2017, 2019 и 2022"))
        self.pushButton_4.setText(_translate("MainWindow", "VC++ 2013 (12.0)"))
        self.pushButton_5.setText(_translate("MainWindow", "VC++ 2012 (11.0 update 4)"))
        self.pushButton_6.setText(_translate("MainWindow", "VC++ 2010 (10.0 SP1)"))
        self.pushButton_7.setText(_translate("MainWindow", "VC++ 2008 (9.0 SP1)"))
        self.pushButton_8.setText(_translate("MainWindow", "VC++ 2005 (8.0 SP1)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Visual C++"))
        self.pushButton_14.setText(_translate("MainWindow", ".NET Framework 4.6.2"))
        self.pushButton_9.setText(_translate("MainWindow", ".NET Framework 4.8.1"))
        self.pushButton_11.setText(_translate("MainWindow", ".NET Framework 4.7"))
        self.pushButton_10.setText(_translate("MainWindow", ".NET Framework 3.5 (SP1)"))
        self.pushButton_12.setText(_translate("MainWindow", ".NET Framework 4.7.2"))
        self.pushButton_13.setText(_translate("MainWindow", ".NET Framework 4.7.1"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; color:#ffffff;\">3.5 cкачивается долго</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", ".NET Framework Runtime "))
        self.pushButton_15.setText(_translate("MainWindow", "x"))
        self.pushButton_16.setText(_translate("MainWindow", "-"))
        self.label_3.setText(_translate("MainWindow", "Windows Basic Pack"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())