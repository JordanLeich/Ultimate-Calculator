from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi


class TimeWindow(QMainWindow):
    def __init__(self):
        super(TimeWindow, self).__init__()
        loadUi("uis/Ui_Base/time_convert.ui", self)

        self.go_btn.clicked.connect(self.convert)
        self.exit_btn.clicked.connect(self.hide)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = TimeWindow()
    window.show()
    sys.exit(app.exec_())
