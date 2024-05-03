from PySide6 import QtCore, QtWidgets, QtGui
from ui import mainWindow_ui as window
from ui import mainWindow_css as css
from ui import studySettingsWindow_ui as studySettings
from reload import reloadModules

import sys
import time

reloadModules([window, css])


class StudySettingsDialog(QtWidgets.QDialog, studySettings.Ui_countDownDialog):
    timeAdjustment = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setStyleSheet(css.STYLESHEET)

        # connections
        self.buttonBox.accepted.connect(self.saveTime)

    def saveTime(self):
        newTime = int(self.adjustTimerSeconds.text())
        self.timeAdjustment.emit(newTime)


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
        self.studyListStuff()
        self.studySettings = studySettings.Ui_countDownDialog()

        # connections
        self.startBtn.clicked.connect(self.startBtnClicked)
        self.countDown.timeout.connect(self.countDownTimer)
        self.actionStudy_Settings.triggered.connect(self.changeStudyList)

    def startBtnClicked(self):
        if self.startBtn.text() == "Start":
            self.startBtn.setText("Pause")
            self.countDown.start(1000)
            print("Timer Started")
        elif self.startBtn.text() == "Pause":
            self.countDown.stop()
            print("Timer Paused")
            self.startBtn.setText("Start")
            self.progressBar.setValue((1 - self._seconds / self.total_seconds) * 100)

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

        funny = 100

        while funny > 0:
            self.studyList.addItem("STUDY LOTS OF STUFF")
            funny -= 1

    def changeStudyList(self):
        self.studySettingsDialog = StudySettingsDialog(self)
        self.studySettingsDialog.timeAdjustment.connect(self.changeTime)
        self.studySettingsDialog.show()

    def changeTime(self, new_time):
        self._seconds = new_time
        self.updateDisplayTimer()

    def updateDisplayTimer(self):
        # Update the timer display to reflect the new time
        self.timer.display(
            f"{self._seconds // 3600:02}:{(self._seconds % 3600) // 60:02}:{self._seconds % 60:02}"
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
