# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'color_scheme_select.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_colorSchemeSelect(object):
    def setupUi(self, colorSchemeSelect):
        if not colorSchemeSelect.objectName():
            colorSchemeSelect.setObjectName(u"colorSchemeSelect")
        colorSchemeSelect.resize(400, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorSchemeSelect.sizePolicy().hasHeightForWidth())
        colorSchemeSelect.setSizePolicy(sizePolicy)
        colorSchemeSelect.setMinimumSize(QSize(400, 100))
        colorSchemeSelect.setMaximumSize(QSize(400, 100))
        self.verticalLayout = QVBoxLayout(colorSchemeSelect)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.schemePath = QLineEdit(colorSchemeSelect)
        self.schemePath.setObjectName(u"schemePath")

        self.horizontalLayout.addWidget(self.schemePath)

        self.selectBtn = QPushButton(colorSchemeSelect)
        self.selectBtn.setObjectName(u"selectBtn")

        self.horizontalLayout.addWidget(self.selectBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonBox = QDialogButtonBox(colorSchemeSelect)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(colorSchemeSelect)
        self.buttonBox.rejected.connect(colorSchemeSelect.close)

        QMetaObject.connectSlotsByName(colorSchemeSelect)
    # setupUi

    def retranslateUi(self, colorSchemeSelect):
        colorSchemeSelect.setWindowTitle("")
        self.selectBtn.setText(QCoreApplication.translate("colorSchemeSelect", u"Choose", None))
    # retranslateUi

