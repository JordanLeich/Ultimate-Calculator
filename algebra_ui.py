from slope1_ui import *
from slope2_ui import *
from pythagore_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AlgebraWindow(object):
    def slope1(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Slope1Window()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def slope2(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Slope2Window()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def pytha(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_PythaWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 651, 81))
        self.label.setObjectName("label")
        self.slope_1 = QtWidgets.QPushButton(self.centralwidget)
        self.slope_1.setGeometry(QtCore.QRect(70, 140, 201, 51))
        self.slope_1.setObjectName("slope_1")
        self.slope_1.clicked.connect(self.slope1)
        self.slope_2 = QtWidgets.QPushButton(self.centralwidget)
        self.slope_2.setGeometry(QtCore.QRect(410, 140, 201, 51))
        self.slope_2.setObjectName("slope_2")
        self.slope_2.clicked.connect(self.slope2)
        self.pyth_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pyth_btn.setGeometry(QtCore.QRect(70, 250, 201, 51))
        self.pyth_btn.setObjectName("pyth_btn")
        self.pyth_btn.clicked.connect(self.pytha)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(410, 250, 201, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        # MainWindow.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algebra"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Algebra Section</span></p></body></html>"))
        self.slope_1.setText(_translate(
            "MainWindow", "Find Slope (Rise Over Run)"))
        self.slope_2.setText(_translate("MainWindow", "Find Slope Intercept"))
        self.pyth_btn.setText(_translate(
            "MainWindow", "Find Pythagorean Theorem"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AlgebraWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
