#!/usr/bin/env python3

# This file is part of Ubuntu Sway Remix project

# SPDX-FileCopyrightText: 2022 Aleksey Samoilov <samoilov.lex@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import sys
import subprocess
import shutil
from pathlib import Path
from os.path import expanduser

from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                               QDialog, QGroupBox, QGridLayout, QCheckBox,
                               QRadioButton, QLabel, QStackedWidget,
                               QDialogButtonBox, QHBoxLayout)
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

home = expanduser("~")
user = os.getlogin()
source = "/usr/share/applications/ubuntusway-welcome.desktop"
dest = home + "/.config/autostart/ubuntusway-welcome.desktop"


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 420)
        self.setupUi()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def setupUi(self):
        self.groupBox = QGroupBox("Thanks for trying Ubuntu Sway Remix!")
        gridLayout = QGridLayout()
        vboxLayout = QVBoxLayout()

        btnWebsite = QPushButton("Website", self)
        iconWebsite = QIcon.fromTheme("applications-internet")
        btnWebsite.setIcon(iconWebsite)
        btnWebsite.clicked.connect(self.on_clicked_website)

        btnWiki = QPushButton("Ubuntu Sway Wiki", self)
        iconWiki = QIcon.fromTheme("x-office-address-book")
        btnWiki.setIcon(iconWiki)
        btnWiki.clicked.connect(self.on_clicked_wiki)

        btnIssue = QPushButton("Issue Tracker", self)
        iconIssue = QIcon.fromTheme("dialog-warning")
        btnIssue.setIcon(iconIssue)
        btnIssue.clicked.connect(self.on_clicked_issue)

        btnContrib = QPushButton("Contribute", self)
        iconContrib = QIcon.fromTheme("applications-development")
        btnContrib.setIcon(iconContrib)
        btnContrib.clicked.connect(self.on_clicked_contribute)

        btnChat = QPushButton("Matrix Chat", self)
        iconChat = QIcon.fromTheme("user-available")
        btnChat.setIcon(iconChat)
        btnChat.clicked.connect(self.on_clicked_matrix)

        btnNext = QPushButton("Next", self)
        iconNext = QIcon.fromTheme("go-next")
        btnNext.setIcon(iconNext)
        btnNext.clicked.connect(self.on_clicked_next)

        btnQuit = QPushButton("Quit", self)
        iconQuit = QIcon.fromTheme("application-exit")
        btnQuit.setIcon(iconQuit)
        btnQuit.clicked.connect(self.exitApp)

        btnSwayWiki = QPushButton("Sway Wiki", self)
        iconSwayWiki = QIcon.fromTheme("x-office-address-book")
        btnSwayWiki.setIcon(iconSwayWiki)
        btnSwayWiki.clicked.connect(self.on_clicked_sway_wiki)

        btnInstall = QPushButton("Run Calamares Installer", self)
        iconInstaller = QIcon.fromTheme("system-software-install")
        btnInstall.setIcon(iconInstaller)
        btnInstall.clicked.connect(self.on_clicked_btnInstall)

        btnGparted = QPushButton("Run GParted", self)
        iconGpated = QIcon.fromTheme("drive-harddisk")
        btnGparted.setIcon(iconGpated)
        btnGparted.clicked.connect(self.on_clicked_btnGparted)

        label = QLabel()
        pixmap = QPixmap("/usr/share/ubuntusway-welcome/logo.png")
        pixmap = pixmap.scaled(600, 300, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)

        label2 = QLabel()
        text = ["Want to learn more about the project? "
                "Please find the links below."]
        label2.setText(text[0])
        self.checkAutostart = QCheckBox("Autostart")
        self.checkAutostart.toggled.connect(self.on_checked_autostart)

        if Path(dest).is_file():
            self.checkAutostart.setChecked(True)

        gridLayout.addWidget(btnWebsite, 1, 0, 1, 1)
        gridLayout.addWidget(btnWiki, 1, 1, 1, 1)
        gridLayout.addWidget(btnIssue, 1, 2, 1, 1)
        gridLayout.addWidget(btnContrib, 1, 3, 1, 1)
        gridLayout.addWidget(btnChat, 2, 0, 1, 1)
        gridLayout.addWidget(btnNext, 2, 3, 1, 1)
        gridLayout.addWidget(btnQuit, 2, 2, 1, 1)
        gridLayout.addWidget(btnSwayWiki, 2, 1, 1, 1)
        gridLayout.addWidget(btnInstall, 0, 0, 1, 2)
        gridLayout.addWidget(btnGparted, 0, 2, 1, 2)

        vboxLayout.addWidget(label, 0, Qt.AlignCenter)
        vboxLayout.addWidget(label2, 0, Qt.AlignCenter)
        vboxLayout.addLayout(gridLayout)
        vboxLayout.addWidget(self.checkAutostart, 0, Qt.AlignRight)
        self.groupBox.setLayout(vboxLayout)

    def on_checked_autostart(self):
        if self.checkAutostart.isChecked():
            if Path(dest).is_file() is False:
                shutil.copy(source, dest)
        else:
            os.unlink(dest)

    def on_clicked_btnInstall(self):
        msg = WarningMessage()
        if Path(f"/usr/bin/calamares").is_file() and user == "ubuntu":
            subprocess.run("sudo -E /usr/bin/calamares -d -style Fusion &", shell=True)
        else:
            msg.exec()

    def on_clicked_btnGparted(self):
        subprocess.run("xhost +si:localuser:root && pkexec /usr/sbin/gparted && xhost -si:localuser:root &", shell=True)

    def on_clicked_website(self):
        subprocess.run(["xdg-open", "https://ubuntusway.com"])

    def on_clicked_wiki(self):
        subprocess.run(["xdg-open", "https://github.com/Ubuntu-Sway/Ubuntu-Sway-Remix/wiki"])

    def on_clicked_sway_wiki(self):
        subprocess.run(["xdg-open", "https://github.com/swaywm/sway/wiki"])

    def on_clicked_issue(self):
        subprocess.run(["xdg-open", "https://github.com/Ubuntu-Sway/Ubuntu-Sway-Remix/issues"])

    def on_clicked_contribute(self):
        subprocess.run(["xdg-open", "https://github.com/Ubuntu-Sway"])

    def on_clicked_matrix(self):
        subprocess.run(["xdg-open", "https://matrix.to/#/#ubuntusway:matrix.org"])

    def on_clicked_next(self):
        window2 = Window2()
        widget.addWidget(window2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exitApp(self):
        app.exit()


class WarningMessage(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 100)
        self.setWindowTitle("Warning!")
        self.layout = QVBoxLayout()

        btnOk = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(btnOk)
        self.buttonBox.accepted.connect(self.accept)

        message = QLabel()
        mesage_text = ["Your system is already installed! "
                       "If you wish to reinstall it, "
                       "boot from the installation media."]
        message.setText(mesage_text[0])
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 420)
        self.setupUi()
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.groupBox2)
        self.setLayout(vbox2)
        self.show()

    def setupUi(self):
        self.groupBox2 = QGroupBox("Thanks for trying Ubuntu Sway Remix!")
        gridLayout2 = QGridLayout()
        vboxLayout2 = QVBoxLayout()

        btnShell = QPushButton("Change shell", self)
        iconShell = QIcon.fromTheme("utilities-terminal")
        btnShell.setIcon(iconShell)
        btnShell.clicked.connect(self.on_clicked_btnShell)

        btnPrev = QPushButton("Previous", self)
        iconPrev = QIcon.fromTheme("go-previous")
        btnPrev.setIcon(iconPrev)
        btnPrev.clicked.connect(self.on_clicked_previous)

        btnQuit = QPushButton("Quit", self)
        iconQuit = QIcon.fromTheme("application-exit")
        btnQuit.setIcon(iconQuit)
        btnQuit.clicked.connect(self.exitApp)

        btnSoftware = QPushButton("Install software", self)
        iconSoftware = QIcon.fromTheme("system-software-install")
        btnSoftware.setIcon(iconSoftware)
        btnSoftware.clicked.connect(self.on_clicked_btnSoftware)

        btnUpd = QPushButton("Check for updates", self)
        iconUpd = QIcon.fromTheme("system-software-update")
        btnUpd.setIcon(iconUpd)
        btnUpd.clicked.connect(self.on_clicked_btnUpd)

        label = QLabel()
        pixmap = QPixmap("/usr/share/ubuntusway-welcome/logo.png")
        pixmap = pixmap.scaled(600, 300, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)

        label2 = QLabel()
        text = "Advanced options"
        label2.setText(text)

        gridLayout2.addWidget(btnShell, 0, 0, 1, 1)
        gridLayout2.addWidget(btnPrev, 2, 0, 1, 1)
        gridLayout2.addWidget(btnQuit, 2, 2, 1, 1)
        gridLayout2.addWidget(btnSoftware, 0, 1, 1, 1)
        gridLayout2.addWidget(btnUpd, 0, 2, 1, 1)

        vboxLayout2.addWidget(label, 0, Qt.AlignCenter)
        vboxLayout2.addWidget(label2, 0, Qt.AlignCenter)
        vboxLayout2.addLayout(gridLayout2)
        self.groupBox2.setLayout(vboxLayout2)

    def on_clicked_btnSoftware(self):
        subprocess.run("gpk-application &", shell=True)

    def on_clicked_btnUpd(self):
        subprocess.run("gpk-update-viewer &", shell=True)

    def on_clicked_btnShell(self):
        self.select = ShellSelectWindow()
        self.select.show()

    def on_clicked_previous(self):
        window1 = Window1()
        widget.addWidget(window1)
        widget.setCurrentIndex(widget.currentIndex()-1)

    def exitApp(self):
        app.exit()


class ShellSelectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 150)
        self.setWindowTitle("Change shell")
        self.setupUi()
        vbox3 = QVBoxLayout()
        vbox3.addWidget(self.groupBox3)
        self.setLayout(vbox3)
        self.show()

    def setupUi(self):
        Hlayout = QHBoxLayout()
        Vlayout = QVBoxLayout()

        self.groupBox3 = QGroupBox("Select shell:")

        self.btnBash = QRadioButton("Bash (Default)")
        self.btnBash.setChecked(True)
        self.btnZSH = QRadioButton("ZSH")
        self.btnFish = QRadioButton("Fish")
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Apply", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton("Close", QDialogButtonBox.RejectRole)
        self.buttonBox.accepted.connect(self.apply)
        self.buttonBox.rejected.connect(self.cancel)

        Hlayout.addWidget(self.btnBash)
        Hlayout.addWidget(self.btnZSH)
        Hlayout.addWidget(self.btnFish)
        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(self.buttonBox)
        self.groupBox3.setLayout(Vlayout)

    def apply(self):
        if self.btnBash.isChecked():
            self.shell = "/usr/bin/bash"
            subprocess.run(["pkexec", "chsh", "-s", self.shell, user])
        elif self.btnFish.isChecked():
            self.shell = "/usr/bin/fish"
            subprocess.run(["pkexec", "chsh", "-s", self.shell, user])
        else:
            self.shell = "/usr/bin/zsh"
            subprocess.run(["pkexec", "chsh", "-s", self.shell, user])

    def cancel(self):
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = QStackedWidget()
    window1 = Window1()
    window2 = Window2()
    widget.addWidget(window1)
    widget.addWidget(window2)
    widget.setFixedHeight(420)
    widget.setFixedWidth(640)
    widget.show()
    sys.exit(app.exec_())
