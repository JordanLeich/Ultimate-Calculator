
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Slope1Window(object):
    def slope(self):
        try:
            y2 = float(self.line_1.text())
            y1 = float(self.line_2.text())
            x2 = float(self.line_3.text())
            x1 = float(self.line_4.text())

            slope = (y2 - y1) / (x2 - x1)
            self.line_5.setText(str(slope))
        except:
            self.line_5.setText("Try Again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(150, 30, 191, 41))
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(150, 90, 191, 41))
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(150, 150, 191, 41))
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(150, 210, 191, 41))
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(150, 280, 191, 41))
        self.line_5.setObjectName("line_5")
        self.go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_btn.setGeometry(QtCore.QRect(70, 350, 131, 51))
        self.go_btn.setObjectName("go_btn")
        self.go_btn.clicked.connect(self.slope)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(260, 350, 131, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 220, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 280, 81, 31))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Slope (Rise Over Run)"))
        self.go_btn.setText(_translate("MainWindow", "Go"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Y2</span></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Y1</span></p></body></html>"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">X2</span></p></body></html>"))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">X1</span></p></body></html>"))
        self.label_5.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Slope</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Slope1Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
