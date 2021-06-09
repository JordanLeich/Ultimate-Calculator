from uis.slope1_ui import Slope1Window
from uis.slope2_ui import Slope2Window
from uis.pythagore_ui import PythaWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class AlgebraWindow(QMainWindow):
    def __init__(self, path=""):
        super(AlgebraWindow, self).__init__()
        # Loading All the components needed

        self.path = f"{path}Ui_Base/algebra.ui"
        self.xpath = path
        loadUi(self.path, self)

        # Setting the Windows needed
        self.slope1 = Slope1Window(self.xpath)
        self.slope2 = Slope2Window(self.xpath)
        self.pytha = PythaWindow(self.xpath)

        # Setting the buttons functions
        self.slope_1.clicked.connect(self.slope1.show)
        self.slope_2.clicked.connect(self.slope2.show)
        self.pyth_btn.clicked.connect(self.pytha.show)
        self.exit_btn.clicked.connect(self.hide)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AlgebraWindow()
    window.show()
    sys.exit(app.exec_())
