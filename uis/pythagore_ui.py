from math import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PythaWindow(object):
    def pytha(self):
        try:
            side = self.comboBox.currentText()
            if side == "A":
                b = int(self.line_2.text())
                c = int(self.line_3.text())
                a = sqrt(c*c-b*b)
                self.line_1.setText(str(a))
            elif side == "B":
                a = int(self.line_1.text())
                c = int(self.line_3.text())
                b = sqrt(c*c-a*a)
                self.line_2.setText(str(b))
            elif side == "C":
                a = int(self.line_1.text())
                b = int(self.line_2.text())
                c = sqrt(a*a+b*b)
                self.line_3.setText(str(c))
        except:
            self.line_1.setText("Try Again ...!")
            self.line_2.setText("Try Again ...!")
            self.line_3.setText("Try Again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(150, 20, 191, 41))
        self.line_1.setObjectName("line_1")
        self.line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(150, 90, 191, 41))
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(150, 160, 191, 41))
        self.line_3.setObjectName("line_3")
        self.go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_btn.setGeometry(QtCore.QRect(40, 310, 151, 51))
        self.go_btn.setObjectName("go_btn")
        self.go_btn.clicked.connect(self.pytha)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(260, 310, 141, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 30, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 81, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 230, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 240, 101, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Pythagorean Theorem"))
        self.go_btn.setText(_translate("MainWindow", "Calculate Length"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Side A</span></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Side B</span></p><p><br/></p></body></html>"))
        self.label_3.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Side C</span></p><p><br/></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "A"))
        self.comboBox.setItemText(1, _translate("MainWindow", "B"))
        self.comboBox.setItemText(2, _translate("MainWindow", "C"))
        self.label_4.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Side to calculate</span></p><p><br/></p><p><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_PythaWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
