from PySide6 import QtCore, QtWidgets, QtGui
from ui import mainWindow_ui as window
from ui import mainWindow_css as css

import sys
import time


class MainWindow(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self.setupUi(self)
        self.setStyleSheet(css.STYLESHEET)
        self.setWindowTitle("Main Window")
        self.timer.setDigitCount(8)
        self.timer.display("04:00:00")
        self.progressBar.setValue(0)
        self._seconds = 14400

        # connections
        self.startBtn.clicked.connect(self.startBtnClicked)

    def startBtnClicked(self):
        if self.startBtn.text() == "Start":
            self.startBtn.setText("Stop")
            self.timer.startTimer(1000)
            self.timer.connect(self.displayTime)
        elif self.startBtn.text() == "Stop":
            self.startBtn.setText("Start")
            self.timer.display("04:00:00")
            self.timer.disconnect()
        print("Start Button Clicked")

    def displayTime(self):
        self.timer.setText(time.strftime("%H:%M:%S", time.gmtime(self._seconds)))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
