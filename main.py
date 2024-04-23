from PySide6 import QtCore, QtWidgets, QtGui
from ui import mainWindow_ui as window
from ui import mainWindow_css as css
from reload import reloadModules

import sys
import time

reloadModules([window, css])


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
        self.total_seconds = self._seconds
        self.countDown = QtCore.QTimer(self)

        # connections
        self.startBtn.clicked.connect(self.startBtnClicked)
        self.countDown.timeout.connect(self.countDownTimer)

        self.studyList.setEnabled(False)

    def startBtnClicked(self):
        if self.startBtn.text() == "Start":
            self.startBtn.setText("Stop")
            self.countDown.start(1000)
            print("Timer Started")
        elif self.startBtn.text() == "Stop":
            self.countDown.stop()
            print("Timer Stopped")
            self._seconds = self.total_seconds
            self.startBtn.setText("Start")
            self.timer.display("04:00:00")
            self.progressBar.setValue(0)

    def displayTime(self):
        hours, remainder = divmod(self._seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        self.timer.display(f"{hours:02}:{minutes:02}:{seconds:02}")

    def countDownTimer(self):
        self._seconds -= 1
        self.displayTime()
        self.progressBar.setValue((1 - self._seconds / self.total_seconds) * 100)
        if self._seconds <= 0:
            self.countDown.stop()
            self.startBtn.setText("Start")
            self.timer.display("04:00:00")
            self.progressBar.setValue(100)
            print("Timer Finished")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
