# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(664, 473)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(664, 473))
        MainWindow.setMaximumSize(QSize(664, 473))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        sizePolicy.setHeightForWidth(self.page1.sizePolicy().hasHeightForWidth())
        self.page1.setSizePolicy(sizePolicy)
        self.page1.setMinimumSize(QSize(650, 430))
        self.page1.setMaximumSize(QSize(650, 430))
        self.verticalLayout_2 = QVBoxLayout(self.page1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.page1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bgLabel1 = QLabel(self.groupBox)
        self.bgLabel1.setObjectName(u"bgLabel1")
        self.bgLabel1.setText(u"")

        self.verticalLayout_4.addWidget(self.bgLabel1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnInstall = QPushButton(self.groupBox)
        self.btnInstall.setObjectName(u"btnInstall")
        icon = QIcon()
        iconThemeName = u"system-software-install"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnInstall.setIcon(icon)

        self.gridLayout.addWidget(self.btnInstall, 0, 0, 1, 2)

        self.btnGparted = QPushButton(self.groupBox)
        self.btnGparted.setObjectName(u"btnGparted")
        icon1 = QIcon()
        iconThemeName = u"drive-harddisk"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnGparted.setIcon(icon1)

        self.gridLayout.addWidget(self.btnGparted, 0, 2, 1, 2)

        self.btnWebsite = QPushButton(self.groupBox)
        self.btnWebsite.setObjectName(u"btnWebsite")
        icon2 = QIcon()
        iconThemeName = u"applications-internet"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnWebsite.setIcon(icon2)

        self.gridLayout.addWidget(self.btnWebsite, 1, 0, 1, 1)

        self.btnWiki = QPushButton(self.groupBox)
        self.btnWiki.setObjectName(u"btnWiki")
        icon3 = QIcon()
        iconThemeName = u"x-office-address-book"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnWiki.setIcon(icon3)

        self.gridLayout.addWidget(self.btnWiki, 1, 1, 1, 1)

        self.btnIssue = QPushButton(self.groupBox)
        self.btnIssue.setObjectName(u"btnIssue")
        icon4 = QIcon()
        iconThemeName = u"dialog-warning"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnIssue.setIcon(icon4)

        self.gridLayout.addWidget(self.btnIssue, 1, 2, 1, 1)

        self.btnContrib = QPushButton(self.groupBox)
        self.btnContrib.setObjectName(u"btnContrib")
        icon5 = QIcon()
        iconThemeName = u"applications-development"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnContrib.setIcon(icon5)

        self.gridLayout.addWidget(self.btnContrib, 1, 3, 1, 1)

        self.btnChat = QPushButton(self.groupBox)
        self.btnChat.setObjectName(u"btnChat")
        icon6 = QIcon()
        iconThemeName = u"user-available"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnChat.setIcon(icon6)

        self.gridLayout.addWidget(self.btnChat, 2, 0, 1, 1)

        self.btnSwayWiki = QPushButton(self.groupBox)
        self.btnSwayWiki.setObjectName(u"btnSwayWiki")
        self.btnSwayWiki.setIcon(icon3)

        self.gridLayout.addWidget(self.btnSwayWiki, 2, 1, 1, 1)

        self.btnQuit = QPushButton(self.groupBox)
        self.btnQuit.setObjectName(u"btnQuit")
        icon7 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon7 = QIcon.fromTheme(iconThemeName)
        else:
            icon7.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnQuit.setIcon(icon7)

        self.gridLayout.addWidget(self.btnQuit, 2, 2, 1, 1)

        self.btnNext = QPushButton(self.groupBox)
        self.btnNext.setObjectName(u"btnNext")
        icon8 = QIcon()
        iconThemeName = u"go-next"
        if QIcon.hasThemeIcon(iconThemeName):
            icon8 = QIcon.fromTheme(iconThemeName)
        else:
            icon8.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnNext.setIcon(icon8)

        self.gridLayout.addWidget(self.btnNext, 2, 3, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_3 = QVBoxLayout(self.page2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.page2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.bgLabel2 = QLabel(self.groupBox_2)
        self.bgLabel2.setObjectName(u"bgLabel2")
        self.bgLabel2.setText(u"")

        self.verticalLayout_5.addWidget(self.bgLabel2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btnPrev = QPushButton(self.groupBox_2)
        self.btnPrev.setObjectName(u"btnPrev")
        icon9 = QIcon()
        iconThemeName = u"go-previous"
        if QIcon.hasThemeIcon(iconThemeName):
            icon9 = QIcon.fromTheme(iconThemeName)
        else:
            icon9.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnPrev.setIcon(icon9)

        self.gridLayout_2.addWidget(self.btnPrev, 2, 0, 1, 1)

        self.btnQuit2 = QPushButton(self.groupBox_2)
        self.btnQuit2.setObjectName(u"btnQuit2")
        self.btnQuit2.setIcon(icon7)

        self.gridLayout_2.addWidget(self.btnQuit2, 2, 2, 1, 1)

        self.btnShell = QPushButton(self.groupBox_2)
        self.btnShell.setObjectName(u"btnShell")
        icon10 = QIcon()
        iconThemeName = u"utilities-terminal"
        if QIcon.hasThemeIcon(iconThemeName):
            icon10 = QIcon.fromTheme(iconThemeName)
        else:
            icon10.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnShell.setIcon(icon10)

        self.gridLayout_2.addWidget(self.btnShell, 1, 0, 1, 1)

        self.btnUpd = QPushButton(self.groupBox_2)
        self.btnUpd.setObjectName(u"btnUpd")
        icon11 = QIcon()
        iconThemeName = u"system-software-update"
        if QIcon.hasThemeIcon(iconThemeName):
            icon11 = QIcon.fromTheme(iconThemeName)
        else:
            icon11.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnUpd.setIcon(icon11)

        self.gridLayout_2.addWidget(self.btnUpd, 1, 2, 1, 1)

        self.btnInput = QPushButton(self.groupBox_2)
        self.btnInput.setObjectName(u"btnInput")
        icon12 = QIcon()
        iconThemeName = u"input-keyboard"
        if QIcon.hasThemeIcon(iconThemeName):
            icon12 = QIcon.fromTheme(iconThemeName)
        else:
            icon12.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnInput.setIcon(icon12)

        self.gridLayout_2.addWidget(self.btnInput, 2, 1, 1, 1)

        self.btnTheme = QPushButton(self.groupBox_2)
        self.btnTheme.setObjectName(u"btnTheme")
        icon13 = QIcon()
        iconThemeName = u"preferences-desktop-theme"
        if QIcon.hasThemeIcon(iconThemeName):
            icon13 = QIcon.fromTheme(iconThemeName)
        else:
            icon13.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnTheme.setIcon(icon13)

        self.gridLayout_2.addWidget(self.btnTheme, 0, 0, 1, 1)

        self.btnDrivers = QPushButton(self.groupBox_2)
        self.btnDrivers.setObjectName(u"btnDrivers")
        icon14 = QIcon()
        iconThemeName = u"preferences-system"
        if QIcon.hasThemeIcon(iconThemeName):
            icon14 = QIcon.fromTheme(iconThemeName)
        else:
            icon14.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnDrivers.setIcon(icon14)

        self.gridLayout_2.addWidget(self.btnDrivers, 0, 1, 1, 1)

        self.btnDisplays = QPushButton(self.groupBox_2)
        self.btnDisplays.setObjectName(u"btnDisplays")
        icon15 = QIcon()
        iconThemeName = u"video-display"
        if QIcon.hasThemeIcon(iconThemeName):
            icon15 = QIcon.fromTheme(iconThemeName)
        else:
            icon15.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnDisplays.setIcon(icon15)

        self.gridLayout_2.addWidget(self.btnDisplays, 0, 2, 1, 1)

        self.btnSoftware = QPushButton(self.groupBox_2)
        self.btnSoftware.setObjectName(u"btnSoftware")
        self.btnSoftware.setIcon(icon)

        self.gridLayout_2.addWidget(self.btnSoftware, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkAutostart = QCheckBox(self.centralwidget)
        self.checkAutostart.setObjectName(u"checkAutostart")

        self.horizontalLayout.addWidget(self.checkAutostart)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Thanks for trying Ubuntu Sway Remix!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Want to learn more about the project? Please find the links below.", None))
        self.btnInstall.setText(QCoreApplication.translate("MainWindow", u"Run Calamaes Installer", None))
        self.btnGparted.setText(QCoreApplication.translate("MainWindow", u"Run GParted", None))
        self.btnWebsite.setText(QCoreApplication.translate("MainWindow", u"Website", None))
        self.btnWiki.setText(QCoreApplication.translate("MainWindow", u"Ubuntu Sway Wiki", None))
        self.btnIssue.setText(QCoreApplication.translate("MainWindow", u"Issue Tracker", None))
        self.btnContrib.setText(QCoreApplication.translate("MainWindow", u"Contribute", None))
        self.btnChat.setText(QCoreApplication.translate("MainWindow", u"Matrix Chat", None))
        self.btnSwayWiki.setText(QCoreApplication.translate("MainWindow", u"Sway Wiki", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Thanks for trying Ubuntu Sway Remix!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Advanced options", None))
        self.btnPrev.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.btnQuit2.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.btnShell.setText(QCoreApplication.translate("MainWindow", u"Change shell", None))
        self.btnUpd.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.btnInput.setText(QCoreApplication.translate("MainWindow", u"Input Settings", None))
        self.btnTheme.setText(QCoreApplication.translate("MainWindow", u"Change GTK theme", None))
        self.btnDrivers.setText(QCoreApplication.translate("MainWindow", u"Additional Drivers", None))
        self.btnDisplays.setText(QCoreApplication.translate("MainWindow", u"Display Settings", None))
        self.btnSoftware.setText(QCoreApplication.translate("MainWindow", u"Install Software", None))
        self.checkAutostart.setText(QCoreApplication.translate("MainWindow", u"Autostart", None))
    # retranslateUi

