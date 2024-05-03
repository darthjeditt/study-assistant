# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'studySettingsWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_countDownDialog(object):
    def setupUi(self, countDownDialog):
        if not countDownDialog.objectName():
            countDownDialog.setObjectName(u"countDownDialog")
        countDownDialog.resize(358, 71)
        self.verticalLayout_2 = QVBoxLayout(countDownDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(countDownDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.adjustTimerSeconds = QLineEdit(countDownDialog)
        self.adjustTimerSeconds.setObjectName(u"adjustTimerSeconds")

        self.horizontalLayout.addWidget(self.adjustTimerSeconds)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(countDownDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(countDownDialog)
        self.buttonBox.accepted.connect(countDownDialog.accept)
        self.buttonBox.rejected.connect(countDownDialog.reject)

        QMetaObject.connectSlotsByName(countDownDialog)
    # setupUi

    def retranslateUi(self, countDownDialog):
        countDownDialog.setWindowTitle(QCoreApplication.translate("countDownDialog", u"Adjust Timer", None))
        self.label.setText(QCoreApplication.translate("countDownDialog", u"Adjust Timer (in seconds)", None))
    # retranslateUi




import typing
if typing.TYPE_CHECKING:

    class _TypeHint:
        """Auto-generated type hinting class"""

        Dialog: QDialog = QDialog()
        verticalLayout_2: QVBoxLayout = QVBoxLayout(countDownDialog)
        verticalLayout: QVBoxLayout = QVBoxLayout()
        horizontalLayout: QHBoxLayout = QHBoxLayout()
        label: QLabel = QLabel(countDownDialog)
        adjustTimerSeconds: QLineEdit = QLineEdit(countDownDialog)
        buttonBox: QDialogButtonBox = QDialogButtonBox(countDownDialog)
