from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class Slope2Window(QMainWindow):
    def __init__(self, path=""):
        super(Slope2Window, self).__init__()

        self.path = f"{path}Ui_Base/slope2.ui"
        loadUi(self.path, self)

        self.go_btn.clicked.connect(self.slope)
        self.exit_btn.clicked.connect(self.hide)

    def slope(self):
        try:
            m = float(self.line_1.text())
            x = float(self.line_2.text())
            b = float(self.line_3.text())
            y = m * x + b
            self.line_4.setText(str(y))
        except:
            self.line_4.setText("Try Again ...!")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Slope2Window()
    window.show()
    sys.exit(app.exec_())
