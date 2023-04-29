# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shell_select.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_shellSelect(object):
    def setupUi(self, shellSelect):
        if not shellSelect.objectName():
            shellSelect.setObjectName(u"shellSelect")
        shellSelect.resize(400, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(shellSelect.sizePolicy().hasHeightForWidth())
        shellSelect.setSizePolicy(sizePolicy)
        shellSelect.setMinimumSize(QSize(400, 150))
        shellSelect.setMaximumSize(QSize(400, 150))
        self.verticalLayout = QVBoxLayout(shellSelect)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(shellSelect)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnBash = QRadioButton(self.groupBox)
        self.btnBash.setObjectName(u"btnBash")

        self.horizontalLayout_2.addWidget(self.btnBash)

        self.btnZSH = QRadioButton(self.groupBox)
        self.btnZSH.setObjectName(u"btnZSH")

        self.horizontalLayout_2.addWidget(self.btnZSH)

        self.btnFish = QRadioButton(self.groupBox)
        self.btnFish.setObjectName(u"btnFish")

        self.horizontalLayout_2.addWidget(self.btnFish)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonBox = QDialogButtonBox(self.groupBox)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(shellSelect)
        self.buttonBox.rejected.connect(shellSelect.close)

        QMetaObject.connectSlotsByName(shellSelect)
    # setupUi

    def retranslateUi(self, shellSelect):
        shellSelect.setWindowTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("shellSelect", u"Select default shell:", None))
        self.btnBash.setText(QCoreApplication.translate("shellSelect", u"Bash (Default)", None))
        self.btnZSH.setText(QCoreApplication.translate("shellSelect", u"ZSH", None))
        self.btnFish.setText(QCoreApplication.translate("shellSelect", u"Fish", None))
    # retranslateUi

