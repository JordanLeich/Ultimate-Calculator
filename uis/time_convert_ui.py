
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimeWindow(object):
    def convert(self):
        try:
            number = float(self.first_line.text())
            from_ = self.unit_box.currentText()
            to = self.unit_box_2.currentText()
            total_seconds = 0

            if from_ == 'Year':
                number = number * 31536000
                total_seconds += number
            elif from_ == 'Month':
                number = number * 1036800
                total_seconds += number
            elif from_ == 'Day':
                number = number * 86400
                total_seconds += number
            elif from_ == 'Hour':
                number = number * 3600
                total_seconds += number
            elif from_ == 'Minute':
                number = number * 60
                total_seconds += number
            elif from_ == 'Second':
                total_seconds += number

            if to == 'Year':
                self.out_line.setText(str(total_seconds / 31536000)+' Years')
            elif to == 'Month':
                self.out_line.setText(str(total_seconds / 1036800)+' Months')
            elif to == 'Day':
                self.out_line.setText(str(total_seconds / 86400)+' Days')
            elif to == 'Hour':
                self.out_line.setText(str(total_seconds / 3600)+' Hours')
            elif to == 'Minute':
                self.out_line.setText(str(total_seconds / 60)+' Minutes')
            elif to == 'Second':
                self.out_line.setText(str(total_seconds)+' Seconds')

        except:
            self.out_line.setText("Try again ...!")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first_line = QtWidgets.QLineEdit(self.centralwidget)
        self.first_line.setGeometry(QtCore.QRect(150, 30, 201, 31))
        self.first_line.setObjectName("first_line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 29, 101, 31))
        self.label.setObjectName("label")
        self.unit_box = QtWidgets.QComboBox(self.centralwidget)
        self.unit_box.setGeometry(QtCore.QRect(150, 90, 201, 31))
        self.unit_box.setObjectName("unit_box")
        self.unit_box.addItem("")
        self.unit_box.addItem("")
        self.unit_box.addItem("")
        self.unit_box.addItem("")
        self.unit_box.addItem("")
        self.unit_box.addItem("")
        self.operation = QtWidgets.QLabel(self.centralwidget)
        self.operation.setGeometry(QtCore.QRect(30, 89, 111, 31))
        self.operation.setObjectName("operation")
        self.out_line = QtWidgets.QLineEdit(self.centralwidget)
        self.out_line.setGeometry(QtCore.QRect(150, 200, 201, 51))
        self.out_line.setObjectName("out_line")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(30, 210, 101, 31))
        self.output.setObjectName("output")
        self.go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.go_btn.setGeometry(QtCore.QRect(50, 300, 131, 51))
        self.go_btn.setObjectName("go_btn")
        self.go_btn.clicked.connect(self.convert)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(250, 300, 131, 51))
        self.exit_btn.setObjectName("exit_btn")
        self.exit_btn.clicked.connect(MainWindow.hide)
        self.unit_box_2 = QtWidgets.QComboBox(self.centralwidget)
        self.unit_box_2.setGeometry(QtCore.QRect(150, 150, 201, 31))
        self.unit_box_2.setObjectName("unit_box_2")
        self.unit_box_2.addItem("")
        self.unit_box_2.addItem("")
        self.unit_box_2.addItem("")
        self.unit_box_2.addItem("")
        self.unit_box_2.addItem("")
        self.unit_box_2.addItem("")
        self.operation_2 = QtWidgets.QLabel(self.centralwidget)
        self.operation_2.setGeometry(QtCore.QRect(30, 150, 111, 31))
        self.operation_2.setObjectName("operation_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Time Converter"))
        self.label.setText(_translate("MainWindow", "Your Number"))
        self.unit_box.setItemText(0, _translate("MainWindow", "Year"))
        self.unit_box.setItemText(1, _translate("MainWindow", "Month"))
        self.unit_box.setItemText(2, _translate("MainWindow", "Day"))
        self.unit_box.setItemText(3, _translate("MainWindow", "Hour"))
        self.unit_box.setItemText(4, _translate("MainWindow", "Minute"))
        self.unit_box.setItemText(5, _translate("MainWindow", "Second"))
        self.operation.setText(_translate("MainWindow", "From"))
        self.output.setText(_translate("MainWindow", "Output"))
        self.go_btn.setText(_translate("MainWindow", "Go"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.unit_box_2.setItemText(0, _translate("MainWindow", "Year"))
        self.unit_box_2.setItemText(1, _translate("MainWindow", "Month"))
        self.unit_box_2.setItemText(2, _translate("MainWindow", "Day"))
        self.unit_box_2.setItemText(3, _translate("MainWindow", "Hour"))
        self.unit_box_2.setItemText(4, _translate("MainWindow", "Minute"))
        self.unit_box_2.setItemText(5, _translate("MainWindow", "Second"))
        self.operation_2.setText(_translate("MainWindow", "To"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TimeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
