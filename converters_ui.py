from currency_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConvertionWindow(object):
    def currency_show(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_CurrencyWindow()
        self.window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.setupUi(self.window)
        self.window.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-60, 10, 791, 111))
        self.label.setStyleSheet("\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.temp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.temp_btn.setGeometry(QtCore.QRect(90, 112, 151, 61))
        self.temp_btn.setObjectName("temp_btn")
        self.mass_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mass_btn.setGeometry(QtCore.QRect(420, 110, 151, 61))
        self.mass_btn.setObjectName("mass_btn")
        self.len_btn = QtWidgets.QPushButton(self.centralwidget)
        self.len_btn.setGeometry(QtCore.QRect(90, 210, 151, 61))
        self.len_btn.setObjectName("len_btn")
        self.vol_btn = QtWidgets.QPushButton(self.centralwidget)
        self.vol_btn.setGeometry(QtCore.QRect(420, 210, 151, 61))
        self.vol_btn.setObjectName("vol_btn")
        self.curr_btn = QtWidgets.QPushButton(self.centralwidget)
        self.curr_btn.setGeometry(QtCore.QRect(90, 310, 151, 61))
        self.curr_btn.setObjectName("curr_btn")
        self.curr_btn.clicked.connect(self.currency_show)
        self.cry_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cry_btn.setGeometry(QtCore.QRect(420, 310, 151, 61))
        self.cry_btn.setObjectName("cry_btn")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(260, 390, 151, 61))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(MainWindow.hide)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Converters(Volumes, Currency, ...)"))
        self.label.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Welcome to the Ultimate Calculator</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\"> Conversions menu</span></p>\n"
                                      "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#ff007f;\"><br /></p></body></html>"))
        self.temp_btn.setText(_translate("MainWindow", "Temperatur Converter"))
        self.mass_btn.setText(_translate("MainWindow", "Mass Converter"))
        self.len_btn.setText(_translate("MainWindow", "Length Converter"))
        self.vol_btn.setText(_translate("MainWindow", "Volume Converter"))
        self.curr_btn.setText(_translate("MainWindow", "Currency Converter"))
        self.cry_btn.setText(_translate("MainWindow", "Crypto Converter"))
        self.exit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_ConvertionWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
