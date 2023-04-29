# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warning.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WarningMessage(object):
    def setupUi(self, WarningMessage):
        if not WarningMessage.objectName():
            WarningMessage.setObjectName(u"WarningMessage")
        WarningMessage.resize(640, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WarningMessage.sizePolicy().hasHeightForWidth())
        WarningMessage.setSizePolicy(sizePolicy)
        WarningMessage.setMinimumSize(QSize(640, 100))
        WarningMessage.setMaximumSize(QSize(640, 100))
        self.verticalLayout = QVBoxLayout(WarningMessage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(WarningMessage)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(WarningMessage)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(WarningMessage)
        self.buttonBox.accepted.connect(WarningMessage.accept)

        QMetaObject.connectSlotsByName(WarningMessage)
    # setupUi

    def retranslateUi(self, WarningMessage):
        WarningMessage.setWindowTitle("")
        self.label.setText(QCoreApplication.translate("WarningMessage", u"Your system is already installed! If you wish to reinstall it, boot from the installation media.", None))
    # retranslateUi

