from PySide6 import QtCore, QtWidgets, QtGui
from ui import mainWindow_ui as window
from ui import mainWindow_css as css


class MainWindow(QtWidgets.QMainWindow, window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(css.STYLESHEET)
        self.setWindowTitle("Main Window")
        self.startBtn.clicked.connect("Start Button Clicked")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWindow()
    widget.show()
    app.exec()
