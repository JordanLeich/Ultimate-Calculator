from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class Slope1Window(QMainWindow):
    def __init__(self):
        super(Slope1Window, self).__init__()
        loadUi("uis/Ui_Base/slope1.ui", self)

        self.go_btn.clicked.connect(self.slope)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Slope1Window()
    window.show()
    sys.exit(app.exec_())
