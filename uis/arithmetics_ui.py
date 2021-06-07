from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MathWindow(object):
    def addition(self, number1, number2):
        return number1 + number2

    def subtract(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 * number2

    def power(self, number1, number2):
        return number1 ** number2

    def divide(self, number1, number2):
        return number1 / number2

    def operations(self):
        try:
            first_number = float(self.first_line.text())
            second_number = float(self.second_line.text())
            operation = self.opert_box.currentText()
            if operation == 'Add':
                add = self.addition(first_number, second_number)
                self.out_line.setText(str(add))
            elif operation == 'Subtract':
                sub = self.subtract(first_number, second_number)
                self.out_line.setText(str(sub))
            elif operation == 'Multiply':
                mult = self.multiply(first_number, second_number)
                self.out_line.setText(str(mult))
            elif operation == 'Divide':
                div = self.divide(first_number, second_number)
                self.out_line.setText(str(div))
            elif operation == 'Power':
                power = self.power(first_number, second_number)
                self.out_line.setText(str(power))
        except:
            self.out_line.setText("Try Again...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first_line = QtWidgets.QLineEdit(self.centralwidget)
        self.first_line.setGeometry(QtCore.QRect(150, 30, 201, 31))
        self.first_line.setObjectName("first_line")
        self.second_line = QtWidgets.QLineEdit(self.centralwidget)
        self.second_line.setGeometry(QtCore.QRect(150, 140, 201, 31))
        self.second_line.setObjectName("second_line")
        self.opert_box = QtWidgets.QComboBox(self.centralwidget)
        self.opert_box.setGeometry(QtCore.QRect(150, 80, 201, 31))
        self.opert_box.setObjectName("opert_box")
        self.opert_box.addItem("")
        self.opert_box.addItem("")
        self.opert_box.addItem("")
        self.opert_box.addItem("")
        self.opert_box.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 33, 101, 20))
        self.label.setObjectName("label")
        self.second_number = QtWidgets.QLabel(self.centralwidget)
        self.second_number.setGeometry(QtCore.QRect(30, 150, 101, 20))
        self.second_number.setObjectName("second_number")
        self.operation = QtWidgets.QLabel(self.centralwidget)
        self.operation.setGeometry(QtCore.QRect(30, 90, 101, 20))
        self.operation.setObjectName("operation")
        self.out_line = QtWidgets.QLineEdit(self.centralwidget)
        self.out_line.setGeometry(QtCore.QRect(150, 210, 201, 51))
        self.out_line.setObjectName("out_line")
        self.go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_btn.setGeometry(QtCore.QRect(60, 320, 131, 51))
        self.go_btn.setObjectName("go_btn")
        self.go_btn.clicked.connect(self.operations)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(260, 320, 131, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(30, 220, 101, 20))
        self.output.setObjectName("output")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Basic Arithmetics"))
        self.opert_box.setItemText(0, _translate("MainWindow", "Add"))
        self.opert_box.setItemText(1, _translate("MainWindow", "Subtract"))
        self.opert_box.setItemText(2, _translate("MainWindow", "Multiply"))
        self.opert_box.setItemText(3, _translate("MainWindow", "Divide"))
        self.opert_box.setItemText(4, _translate("MainWindow", "Power"))
        self.label.setText(_translate("MainWindow", "First Number"))
        self.second_number.setText(_translate("MainWindow", "Second Number"))
        self.operation.setText(_translate("MainWindow", "Operation"))
        self.go_btn.setText(_translate("MainWindow", "Go"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.output.setText(_translate("MainWindow", "Output"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MathWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
