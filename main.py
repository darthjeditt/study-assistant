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
        self._seconds = 120  # 14400
        self.timer.display(
            f"{self._seconds // 3600:02}:{self._seconds // 60:02}:{self._seconds % 60:02}"
        )
        self.progressBar.setValue(0)
        self.total_seconds = self._seconds
        self.countDown = QtCore.QTimer(self)

        # connections
        self.startBtn.clicked.connect(self.startBtnClicked)
        self.countDown.timeout.connect(self.countDownTimer)

    def startBtnClicked(self):
        if self.startBtn.text() == "Start":
            self.startBtn.setText("Pause")
            self.countDown.start(1000)
            print("Timer Started")
        elif self.startBtn.text() == "Pause":
            self.countDown.stop()
            print("Timer Paused")
            self.startBtn.setText("Start")
            self.progressBar.setValue(0)

    def countDownTimer(self):
        self._seconds -= 1
        self.progressBar.setValue((1 - self._seconds / self.total_seconds) * 100)
        print((1 - self._seconds / self.total_seconds) * 100)
        self.timer.display(
            f"{self._seconds // 3600:02}:{self._seconds // 60:02}:{self._seconds % 60:02}"
        )
        if self._seconds <= 0:
            self.countDown.stop()
            self.startBtn.setText("Start")
            self.timer.display(
                f"{self._seconds // 3600:02}:{self._seconds // 60:02}:{self._seconds % 60:02}"
            )
            self.progressBar.setValue(100)
            print("Timer Finished")

    def studyListStuff(self):
        self.studyList.addItem("Item 1")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
