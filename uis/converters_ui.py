from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import QtCore, QtWidgets
from uis.currency_ui import CurrencyWindow
from uis.length_ui import LengthWindow
from uis.volume_ui import VolumeWindow
from uis.temp_ui import TemperatureWindow
from uis.mass_ui import MassWindow
from uis.crypto_ui import CryptoWindow


class ConvertersWindow(QMainWindow):
    def __init__(self, path=""):
        super(ConvertersWindow, self).__init__()
        self.setWindowTitle("Converters(Volumes, Currency, ...)")
        self.resize(672, 509)
        self.path = path

        self.currency = CurrencyWindow(self.path)
        self.length = LengthWindow(self.path)
        self.volume = VolumeWindow(self.path)
        self.temperature = TemperatureWindow(self.path)
        self.mass = MassWindow(self.path)
        self.crypto = CryptoWindow(self.path)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))

        self.label = QLabel(self)
        self.label.setStyleSheet("\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.label.setGeometry(QtCore.QRect(-60, 10, 791, 111))
        self.label.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                           "p, li { white-space: pre-wrap; }\n"
                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                           "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\"> Conversions menu</span></p>\n"
                           "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600; color:#ff007f;\"><br /></p></body></html>")
        self.label.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Welcome to the Ultimate Calculator</span></p><p align=\"center\"><br/></p></body></html>")

        self.temp_btn = QPushButton(self)
        self.temp_btn.setGeometry(QtCore.QRect(90, 112, 151, 61))
        self.temp_btn.setText("Temperature Converter")
        self.temp_btn.clicked.connect(self.temperature.show)

        self.mass_btn = QPushButton(self)
        self.mass_btn.setGeometry(QtCore.QRect(420, 110, 151, 61))
        self.mass_btn.setText("Mass Converter")
        self.mass_btn.clicked.connect(self.mass.show)

        self.len_btn = QPushButton(self)
        self.len_btn.setGeometry(QtCore.QRect(90, 210, 151, 61))
        self.len_btn.setText("Length Converter")
        self.len_btn.clicked.connect(self.length.show)

        self.vol_btn = QPushButton(self)
        self.vol_btn.setGeometry(QtCore.QRect(420, 210, 151, 61))
        self.vol_btn.setText("Volume Converter")
        self.vol_btn.clicked.connect(self.volume.show)

        self.curr_btn = QPushButton(self)
        self.curr_btn.setGeometry(QtCore.QRect(90, 310, 151, 61))
        self.curr_btn.setText("Currency Converter")
        self.curr_btn.clicked.connect(self.currency.show)

        self.cry_btn = QPushButton(self)
        self.cry_btn.setGeometry(QtCore.QRect(420, 310, 151, 61))
        self.cry_btn.setText("Crypto Converter")
        self.cry_btn.clicked.connect(self.crypto.show)

        self.exit = QPushButton(self)
        self.exit.setGeometry(QtCore.QRect(260, 390, 151, 61))
        self.exit.setText("Exit")
        self.exit.clicked.connect(self.hide)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ConvertersWindow()
    window.show()
    sys.exit(app.exec_())
