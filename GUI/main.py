from converters import *
from arith import *
from time_convert import *
from algebra import *
from stock import *

from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser


class Ui_MainWindow(object):
    def converters_show(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_ConvertionWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def basic_arith(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_MathWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def time_show(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_TimeWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def algebra_show(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AlgebraWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def stock_show(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_StockWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def credits(self):
        webbrowser.open_new(
            "https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 791, 111))
        self.label.setStyleSheet("\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.Math_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Math_btn.setGeometry(QtCore.QRect(110, 140, 211, 71))
        self.Math_btn.setObjectName("Math_btn")
        self.Math_btn.clicked.connect(self.basic_arith)
        self.stock_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stock_btn.setGeometry(QtCore.QRect(480, 260, 211, 71))
        self.stock_btn.setObjectName("stock_btn")
        self.stock_btn.clicked.connect(self.stock_show)
        self.conv_btn = QtWidgets.QPushButton(self.centralwidget)
        self.conv_btn.setGeometry(QtCore.QRect(110, 260, 211, 71))
        self.conv_btn.setObjectName("conv_btn")
        self.conv_btn.clicked.connect(self.converters_show)
        self.Alg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Alg_btn.setGeometry(QtCore.QRect(480, 140, 211, 71))
        self.Alg_btn.setObjectName("Alg_btn")
        self.Alg_btn.clicked.connect(self.algebra_show)
        self.time_btn = QtWidgets.QPushButton(self.centralwidget)
        self.time_btn.setGeometry(QtCore.QRect(110, 380, 211, 71))
        self.time_btn.setObjectName("time_btn")
        self.time_btn.clicked.connect(self.time_show)
        self.cred_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cred_btn.setGeometry(QtCore.QRect(480, 380, 211, 71))
        self.cred_btn.setObjectName("cred_btn")
        self.cred_btn.clicked.connect(self.credits)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(300, 480, 201, 71))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "The Ultimate Calculator"))
        self.label.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Welcome to the Ultimate Calculator</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Welcome to the Ultimate Calculator by <i>Jordan Leich<i/></span></p></body></html>"))
        self.Math_btn.setText(_translate("MainWindow", "Basic Arithmetics"))
        self.stock_btn.setText(_translate("MainWindow", "Stock Market"))
        self.conv_btn.setText(_translate("MainWindow", "Converters"))
        self.Alg_btn.setText(_translate("MainWindow", "Algebra"))
        self.time_btn.setText(_translate("MainWindow", "Time Converter"))
        self.cred_btn.setText(_translate("MainWindow", "Credits"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
