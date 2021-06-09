from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QStatusBar, QMenuBar
from uis.converters_ui import ConvertersWindow
from uis.time_convert_ui import TimeWindow
from uis.algebra_ui import AlgebraWindow
from uis.stock_ui import StockWindow
from uis.arith_calculator_ui import Arithmetic
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Ultimate Calculator")
        self.resize(800, 600)

        self.menubar = QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.converters = ConvertersWindow()
        self.time = TimeWindow()
        self.algebra = AlgebraWindow()
        self.stock = StockWindow()
        self.basic_arith = Arithmetic()

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, -10, 791, 111))
        self.label.setStyleSheet("\n"
                                 "font: 16pt \"MS Shell Dlg 2\";")
        self.label.setToolTip(
            "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Ultimate "
            "Calculator</span></p><p align=\"center\"><br/></p></body></html>")
        self.label.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                           "p, li { white-space: pre-wrap; }\n"
                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; "
                           "font-weight:400; font-style:normal;\">\n "
                           "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; "
                           "margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                           "font-weight:600; color:#ff007f;\">Ultimate Calculator by <i>Jordan "
                           "Leich<i/></span></p></body></html>")

        self.Math_btn = QPushButton(self)
        self.Math_btn.setGeometry(QtCore.QRect(110, 140, 211, 71))
        self.Math_btn.clicked.connect(self.basic_arith.show)
        self.Math_btn.setText("Basic Arithmetics")

        self.stock_btn = QPushButton(self)
        self.stock_btn.setGeometry(QtCore.QRect(480, 260, 211, 71))
        self.stock_btn.clicked.connect(self.stock.show)
        self.stock_btn.setText("Stock Market")

        self.conv_btn = QPushButton(self)
        self.conv_btn.setGeometry(QtCore.QRect(110, 260, 211, 71))
        self.conv_btn.clicked.connect(self.converters.show)
        self.conv_btn.setText("Converters")

        self.Alg_btn = QPushButton(self)
        self.Alg_btn.setGeometry(QtCore.QRect(480, 140, 211, 71))
        self.Alg_btn.clicked.connect(self.algebra.show)
        self.Alg_btn.setText("Algebra")

        self.time_btn = QPushButton(self)
        self.time_btn.setGeometry(QtCore.QRect(110, 380, 211, 71))
        self.time_btn.clicked.connect(self.time.show)
        self.time_btn.setText("Time Converter")

        self.cred_btn = QPushButton(self)
        self.cred_btn.setGeometry(QtCore.QRect(480, 380, 211, 71))
        self.cred_btn.clicked.connect(self.credits)
        self.cred_btn.setText("Credits")

        self.exit_btn = QPushButton(self)
        self.exit_btn.setGeometry(QtCore.QRect(300, 480, 201, 71))
        self.exit_btn.clicked.connect(exit)
        self.exit_btn.setText("Exit") \
 \
    @staticmethod
    def credits():
        webbrowser.open_new(
            "https://github.com/JordanLeich/Ultimate-Calculator/graphs/contributors")


def start_gui():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_gui()
