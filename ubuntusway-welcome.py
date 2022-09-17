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
from i3ipc import Connection

from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                               QDialog, QGroupBox, QGridLayout, QCheckBox,
                               QRadioButton, QLabel, QStackedWidget, QFileDialog,
                               QDialogButtonBox, QHBoxLayout, QLineEdit)
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Qt

home = expanduser("~")
user = os.getlogin()
source = "/usr/share/applications/ubuntusway-welcome.desktop"
dest = home + "/.config/autostart/ubuntusway-welcome.desktop"
sway_config = home + "/.config/sway/config"

i3 = Connection()

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()

    def setupUi(self):
        self.groupBox = QGroupBox("Thanks for trying Ubuntu Sway Remix!")
        gridLayout = QGridLayout()
        vboxLayout = QVBoxLayout()

        self.btnWebsite = QPushButton("Website")
        self.iconWebsite = QIcon.fromTheme("applications-internet")
        self.btnWebsite.setIcon(self.iconWebsite)
        self.btnWebsite.clicked.connect(self.on_clicked_website)

        self.btnWiki = QPushButton("Ubuntu Sway Wiki")
        self.iconWiki = QIcon.fromTheme("x-office-address-book")
        self.btnWiki.setIcon(self.iconWiki)
        self.btnWiki.clicked.connect(self.on_clicked_wiki)

        self.btnIssue = QPushButton("Issue Tracker")
        self.iconIssue = QIcon.fromTheme("dialog-warning")
        self.btnIssue.setIcon(self.iconIssue)
        self.btnIssue.clicked.connect(self.on_clicked_issue)

        self.btnContrib = QPushButton("Contribute")
        self.iconContrib = QIcon.fromTheme("applications-development")
        self.btnContrib.setIcon(self.iconContrib)
        self.btnContrib.clicked.connect(self.on_clicked_contribute)

        self.btnChat = QPushButton("Matrix Chat")
        self.iconChat = QIcon.fromTheme("user-available")
        self.btnChat.setIcon(self.iconChat)
        self.btnChat.clicked.connect(self.on_clicked_matrix)

        self.btnNext = QPushButton("Next")
        self.iconNext = QIcon.fromTheme("go-next")
        self.btnNext.setIcon(self.iconNext)
        self.btnNext.clicked.connect(self.on_clicked_next)

        self.btnQuit = QPushButton("Quit")
        self.iconQuit = QIcon.fromTheme("application-exit")
        self.btnQuit.setIcon(self.iconQuit)
        self.btnQuit.clicked.connect(self.exitApp)

        self.btnSwayWiki = QPushButton("Sway Wiki")
        self.iconSwayWiki = QIcon.fromTheme("x-office-address-book")
        self.btnSwayWiki.setIcon(self.iconSwayWiki)
        self.btnSwayWiki.clicked.connect(self.on_clicked_sway_wiki)

        self.btnInstall = QPushButton("Run Calamares Installer")
        self.iconInstaller = QIcon.fromTheme("system-software-install")
        self.btnInstall.setIcon(self.iconInstaller)
        self.btnInstall.clicked.connect(self.on_clicked_btnInstall)

        self.btnGparted = QPushButton("Run GParted")
        self.iconGpated = QIcon.fromTheme("drive-harddisk")
        self.btnGparted.setIcon(self.iconGpated)
        self.btnGparted.clicked.connect(self.on_clicked_btnGparted)

        label = QLabel()
        pixmap = QPixmap("/usr/share/ubuntusway-welcome/logo.png")
        pixmap = pixmap.scaled(600, 300, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)

        label2 = QLabel()
        text = ["Want to learn more about the project? "
                "Please find the links below."]
        label2.setText(text[0])

        gridLayout.addWidget(self.btnWebsite, 1, 0, 1, 1)
        gridLayout.addWidget(self.btnWiki, 1, 1, 1, 1)
        gridLayout.addWidget(self.btnIssue, 1, 2, 1, 1)
        gridLayout.addWidget(self.btnContrib, 1, 3, 1, 1)
        gridLayout.addWidget(self.btnChat, 2, 0, 1, 1)
        gridLayout.addWidget(self.btnNext, 2, 3, 1, 1)
        gridLayout.addWidget(self.btnQuit, 2, 2, 1, 1)
        gridLayout.addWidget(self.btnSwayWiki, 2, 1, 1, 1)
        gridLayout.addWidget(self.btnInstall, 0, 0, 1, 2)
        gridLayout.addWidget(self.btnGparted, 0, 2, 1, 2)

        vboxLayout.addWidget(label, 0, Qt.AlignCenter)
        vboxLayout.addWidget(label2, 0, Qt.AlignCenter)
        vboxLayout.addLayout(gridLayout)
        self.groupBox.setLayout(vboxLayout)

    def on_clicked_btnInstall(self):
        msg = WarningMessage()
        if Path(f"/usr/bin/calamares").is_file() and user == "ubuntu":
            i3.command('exec /usr/bin/install-ubuntusway')
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
        page2 = Page2()
        stackWidget.addWidget(page2)
        stackWidget.setCurrentIndex(stackWidget.currentIndex()+1)

    def exitApp(self):
        app.exit()


class WarningMessage(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 100)
        self.setWindowTitle("Warning!")
        self.layout = QVBoxLayout()

        self.btnOk = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(self.btnOk)
        self.buttonBox.accepted.connect(self.accept)

        message = QLabel()
        mesage_text = ["Your system is already installed! "
                       "If you wish to reinstall it, "
                       "boot from the installation media."]
        message.setText(mesage_text[0])
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class Page2(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.vbox2 = QVBoxLayout()
        self.vbox2.addWidget(self.groupBox2)
        self.setLayout(self.vbox2)
        self.show()

    def setupUi(self):
        self.groupBox2 = QGroupBox("Thanks for trying Ubuntu Sway Remix!")
        gridLayout2 = QGridLayout()
        vboxLayout2 = QVBoxLayout()

        self.btnShell = QPushButton("Change shell")
        self.iconShell = QIcon.fromTheme("utilities-terminal")
        self.btnShell.setIcon(self.iconShell)
        self.btnShell.clicked.connect(self.on_clicked_btnShell)

        self.btnPrev = QPushButton("Previous")
        self.iconPrev = QIcon.fromTheme("go-previous")
        self.btnPrev.setIcon(self.iconPrev)
        self.btnPrev.clicked.connect(self.on_clicked_previous)

        self.btnQuit = QPushButton("Quit")
        self.iconQuit = QIcon.fromTheme("application-exit")
        self.btnQuit.setIcon(self.iconQuit)
        self.btnQuit.clicked.connect(self.exitApp)

        self.btnSoftware = QPushButton("Install Software")
        self.iconSoftware = QIcon.fromTheme("system-software-install")
        self.btnSoftware.setIcon(self.iconSoftware)
        self.btnSoftware.clicked.connect(self.on_clicked_btnSoftware)

        self.btnUpd = QPushButton("Check for updates")
        self.iconUpd = QIcon.fromTheme("system-software-update")
        self.btnUpd.setIcon(self.iconUpd)
        self.btnUpd.clicked.connect(self.on_clicked_btnUpd)

        self.btnTheme = QPushButton("Change GTK theme")
        self.iconTheme = QIcon.fromTheme("preferences-desktop-theme")
        self.btnTheme.setIcon(self.iconTheme)
        self.btnTheme.clicked.connect(self.on_clicked_btnTheme)

        self.btnScheme = QPushButton("Change Color Scheme")
        self.iconScheme = QIcon.fromTheme("preferences-desktop-theme")
        self.btnScheme.setIcon(self.iconScheme)
        self.btnScheme.clicked.connect(self.on_clicked_btnScheme)

        self.btnDisplays = QPushButton("Display Settings")
        self.iconDisplays = QIcon.fromTheme("video-display")
        self.btnDisplays.setIcon(self.iconDisplays)
        self.btnDisplays.clicked.connect(self.on_clicked_btnDisplays)

        self.btnInput = QPushButton("Input Settings")
        self.iconInput = QIcon.fromTheme("input-keyboard")
        self.btnInput.setIcon(self.iconInput)
        self.btnInput.clicked.connect(self.on_clicked_btnInput)

        label = QLabel()
        pixmap = QPixmap("/usr/share/ubuntusway-welcome/logo.png")
        pixmap = pixmap.scaled(600, 300, Qt.KeepAspectRatio)
        label.setPixmap(pixmap)

        label2 = QLabel()
        text = "Advanced options"
        label2.setText(text)

        gridLayout2.addWidget(self.btnShell, 1, 0, 1, 1)
        gridLayout2.addWidget(self.btnTheme, 0, 0, 1, 1)
        gridLayout2.addWidget(self.btnScheme, 0, 1, 1, 1)
        gridLayout2.addWidget(self.btnPrev, 3, 0, 1, 1)
        gridLayout2.addWidget(self.btnInput, 3, 1, 1, 1)
        gridLayout2.addWidget(self.btnQuit, 3, 2, 1, 1)
        gridLayout2.addWidget(self.btnSoftware, 1, 1, 1, 1)
        gridLayout2.addWidget(self.btnUpd, 1, 2, 1, 1)
        gridLayout2.addWidget(self.btnDisplays, 0, 2, 1, 1)

        vboxLayout2.addWidget(label, 0, Qt.AlignCenter)
        vboxLayout2.addWidget(label2, 0, Qt.AlignCenter)
        vboxLayout2.addLayout(gridLayout2)
        self.groupBox2.setLayout(vboxLayout2)

    def on_clicked_btnSoftware(self):
        i3.command('exec gpk-application')

    def on_clicked_btnUpd(self):
        i3.command('exec gpk-update-viewer')

    def on_clicked_btnShell(self):
        self.select = ShellSelectWindow()
        self.select.show()

    def on_clicked_previous(self):
        page1 = Page1()
        stackWidget.addWidget(page1)
        stackWidget.setCurrentIndex(stackWidget.currentIndex()-1)

    def on_clicked_btnTheme(self):
        i3.command('exec nwg-look')

    def on_clicked_btnScheme(self):
        self.scheme = ColorSchemeSelect()
        self.scheme.show

    def on_clicked_btnDisplays(self):
        i3.command('exec nwg-displays')

    def on_clicked_btnInput(self):
        subprocess.run("sway-input-config &", shell=True)

    def exitApp(self):
        app.exit()


class ShellSelectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 150)
        self.setWindowTitle("Change shell")
        self.setupUi()
        self.vbox3 = QVBoxLayout()
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton("Apply", QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton("Close", QDialogButtonBox.RejectRole)
        self.buttonBox.accepted.connect(self.apply)
        self.buttonBox.rejected.connect(self.cancel)
        self.vbox3.addWidget(self.groupBox3)
        self.vbox3.addWidget(self.buttonBox)
        self.setLayout(self.vbox3)
        self.show()

    def setupUi(self):
        Hlayout = QHBoxLayout()
        Vlayout = QVBoxLayout()

        self.groupBox3 = QGroupBox("Select shell:")

        self.btnBash = QRadioButton("Bash (Default)")
        self.btnBash.setChecked(True)
        self.btnZSH = QRadioButton("ZSH")
        self.btnFish = QRadioButton("Fish")

        Hlayout.addWidget(self.btnBash)
        Hlayout.addWidget(self.btnZSH)
        Hlayout.addWidget(self.btnFish)
        Vlayout.addLayout(Hlayout)
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

class ColorSchemeSelect(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 150)
        self.setWindowTitle("Change Color Scheme")
        self.setupUi()
        self.vbox4 = QVBoxLayout()
        self.buttonBox = QDialogButtonBox()
        self.btnApply = QPushButton("Apply")
        self.btnClose = QPushButton("Close")
        self.btnApply.setEnabled(False)
        self.btnApply.clicked.connect(self.applyScheme)
        self.btnClose.clicked.connect(self.cancel)
        self.buttonBox.addButton(self.btnApply, QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(self.btnClose, QDialogButtonBox.RejectRole)
        self.vbox4.addWidget(self.groupBox4)
        self.vbox4.addWidget(self.buttonBox)
        self.setLayout(self.vbox4)
        self.show()

    def setupUi(self):
        Hlayout = QHBoxLayout()
        Vlayout = QVBoxLayout()

        self.groupBox4 = QGroupBox("Select color scheme direcotry:")

        self.schemePath = QLineEdit()
        self.selectBtn = QPushButton("Choose")
        self.selectBtn.clicked.connect(self.openDialog)

        Hlayout.addWidget(self.schemePath)
        Hlayout.addWidget(self.selectBtn)
        Vlayout.addLayout(Hlayout)
        self.groupBox4.setLayout(Vlayout)

    def openDialog(self):
        dialog = QFileDialog.getExistingDirectory(self, 'Select color scheme directory', '/usr/share/ubuntusway/themes')

        if dialog:
            self.schemePath.setText(dialog)
            self.btnApply.setEnabled(True)

    def applyScheme(self):
        scheme_directory = self.schemePath.text()

        with open(sway_config, "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if "set $theme" in lines[i]:
                    line = lines[i].strip()

        scheme_path = f'set $theme {scheme_directory}'

        with open(sway_config, "r+") as w:
            conf = w.read()
            new_scheme = conf.replace(line, scheme_path)
            w.seek(0)
            w.truncate()
            w.write(new_scheme)

        i3.command('reload')

    def cancel(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(["Welcome to Ubuntu Sway Remix!"])

    def on_checked_autostart():
        if checkAutostart.isChecked():
            if Path(dest).is_file() is False:
                shutil.copy(source, dest)
        else:
            os.unlink(dest)

    checkAutostart = QCheckBox("Autostart")
    checkAutostart.toggled.connect(on_checked_autostart)

    if Path(dest).is_file():
            checkAutostart.setChecked(True)

    window = QWidget()
    window.setFixedSize(650, 430)

    layout = QVBoxLayout()

    stackWidget = QStackedWidget()
    page1 = Page1()
    page2 = Page2()
    stackWidget.addWidget(page1)
    stackWidget.addWidget(page2)

    layout.addWidget(stackWidget)
    layout.addWidget(checkAutostart, 0, Qt.AlignRight)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec_())
