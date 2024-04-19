# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLCDNumber, QLabel,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 658)
        self.actionGeneral = QAction(MainWindow)
        self.actionGeneral.setObjectName(u"actionGeneral")
        self.actionBlocked_Apps = QAction(MainWindow)
        self.actionBlocked_Apps.setObjectName(u"actionBlocked_Apps")
        self.actionStudy_Settings = QAction(MainWindow)
        self.actionStudy_Settings.setObjectName(u"actionStudy_Settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.studyList = QPlainTextEdit(self.centralwidget)
        self.studyList.setObjectName(u"studyList")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.studyList.sizePolicy().hasHeightForWidth())
        self.studyList.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.studyList)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.timer = QLCDNumber(self.centralwidget)
        self.timer.setObjectName(u"timer")
        self.timer.setSmallDecimalPoint(False)
        self.timer.setMode(QLCDNumber.Dec)

        self.verticalLayout_2.addWidget(self.timer)

        self.startBtn = QPushButton(self.centralwidget)
        self.startBtn.setObjectName(u"startBtn")

        self.verticalLayout_2.addWidget(self.startBtn)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 980, 21))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionGeneral)
        self.menuSettings.addAction(self.actionBlocked_Apps)
        self.menuSettings.addAction(self.actionStudy_Settings)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGeneral.setText(QCoreApplication.translate("MainWindow", u"General", None))
        self.actionBlocked_Apps.setText(QCoreApplication.translate("MainWindow", u"Blocked Apps", None))
        self.actionStudy_Settings.setText(QCoreApplication.translate("MainWindow", u"Study Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Today's Study Session", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"Start/Pause", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi




import typing
if typing.TYPE_CHECKING:

    class _TypeHint:
        """Auto-generated type hinting class"""

        MainWindow: QMainWindow = QMainWindow()
        actionGeneral: QAction = QAction(MainWindow)
        actionBlocked_Apps: QAction = QAction(MainWindow)
        actionStudy_Settings: QAction = QAction(MainWindow)
        centralwidget: QWidget = QWidget(MainWindow)
        verticalLayout: QVBoxLayout = QVBoxLayout(centralwidget)
        horizontalLayout: QHBoxLayout = QHBoxLayout()
        verticalLayout_3: QVBoxLayout = QVBoxLayout()
        label: QLabel = QLabel(centralwidget)
        studyList: QPlainTextEdit = QPlainTextEdit(centralwidget)
        verticalLayout_2: QVBoxLayout = QVBoxLayout()
        label_2: QLabel = QLabel(centralwidget)
        timer: QLCDNumber = QLCDNumber(centralwidget)
        startBtn: QPushButton = QPushButton(centralwidget)
        progressBar: QProgressBar = QProgressBar(centralwidget)
        menubar: QMenuBar = QMenuBar(MainWindow)
        menuSettings: QMenu = QMenu(menubar)
        statusbar: QStatusBar = QStatusBar(MainWindow)
