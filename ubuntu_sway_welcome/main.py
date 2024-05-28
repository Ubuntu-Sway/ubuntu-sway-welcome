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
from pathlib import Path
from i3ipc import Connection
from shutil import copy2
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialog,
                               QWidget, QDialogButtonBox, QFileDialog)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from ubuntu_sway_welcome.ui_mainwindow import Ui_MainWindow
from ubuntu_sway_welcome.ui_warning import Ui_WarningMessage
from ubuntu_sway_welcome.ui_shell_select import Ui_shellSelect

def get_config_home():
    config_home = os.getenv('XDG_CONFIG_HOME') if os.getenv('XDG_CONFIG_HOME') else os.path.join(
        os.getenv("HOME"), ".config/")
    return config_home

config_home = get_config_home()
dir_name = os.path.dirname(__file__)
user = os.getlogin()
desktop_file = os.path.join(dir_name, "resources/ubuntu-sway-welcome.desktop")
autostart_dir = os.path.join(config_home, "autostart/")
autostart_desktop_file = os.path.join(config_home, autostart_dir, "ubuntu-sway-welcome.desktop")

#i3 = Connection()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Backgound logo
        bg_logo = os.path.join(dir_name, "resources/logo.png")
        pixmap = QPixmap(bg_logo).scaled(600, 300, Qt.AspectRatioMode.KeepAspectRatio)
        self.ui.bgLabel1.setPixmap(pixmap)
        self.ui.bgLabel2.setPixmap(pixmap)

        # Autostart
        if os.path.isfile(autostart_desktop_file):
            self.ui.checkAutostart.setChecked(True)
        self.ui.checkAutostart.toggled.connect(self.on_check_autostart)

        # Page 1
        self.ui.btnInstall.clicked.connect(self.on_clicked_btnInstall)
        self.ui.btnGparted.clicked.connect(self.on_clicked_btnGparted)
        self.ui.btnWebsite.clicked.connect(self.on_clicked_website)
        self.ui.btnWiki.clicked.connect(self.on_clicked_wiki)
        self.ui.btnSwayWiki.clicked.connect(self.on_clicked_sway_wiki)
        self.ui.btnIssue.clicked.connect(self.on_clicked_issue)
        self.ui.btnContrib.clicked.connect(self.on_clicked_contribute)
        self.ui.btnChat.clicked.connect(self.on_clicked_matrix)
        self.ui.btnNext.clicked.connect(self.on_switch_page)
        self.ui.btnPrev.clicked.connect(self.on_switch_page)
        self.ui.btnQuit.clicked.connect(self.exitApp)

        # Page 2
        self.ui.btnTheme.clicked.connect(self.on_clicked_btnTheme)
        self.ui.btnDrivers.clicked.connect(self.on_clicked_btnDrivers)
        self.ui.btnDisplays.clicked.connect(self.on_clicked_btnDisplays)
        self.ui.btnShell.clicked.connect(self.on_clicked_btnShell)
        self.ui.btnSoftware.clicked.connect(self.on_clicked_btnSoftware)
        self.ui.btnUpd.clicked.connect(self.on_clicked_btnUpd)
        self.ui.btnInput.clicked.connect(self.on_clicked_btnInput)
        self.ui.btnQuit2.clicked.connect(self.exitApp)

    def on_clicked_btnInstall(self):
        self.msg = WarningMessage()
        self.msg.setWindowTitle("Warning!")
        if Path(f'{"/usr/bin/calamares"}').is_file() and user == "ubuntu":
            i3.command('exec /usr/bin/install-ubuntu-sway')
        else:
            self.msg.show()

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

    def on_clicked_btnSoftware(self):
        i3.command('exec gnome-software --mode=overview')

    def on_clicked_btnUpd(self):
        i3.command('exec update-manager')

    def on_clicked_btnShell(self):
        self.select = ShellSelectWindow()
        self.select.setWindowTitle("Shell selector")
        self.select.show()

    def on_clicked_btnTheme(self):
        i3.command('exec nwg-look')

    def on_clicked_btnDrivers(self):
        subprocess.run("/usr/bin/software-properties-gtk --open-tab=4 &", shell=True)

    def on_clicked_btnDisplays(self):
        i3.command('exec nwg-displays')

    def on_clicked_btnInput(self):
        subprocess.run("sway-input-config &", shell=True)

    def on_switch_page(self):
        if self.ui.stackedWidget.currentIndex() == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)

    def on_check_autostart(self):
        if self.ui.checkAutostart.isChecked():
            if os.path.exists(autostart_dir):
                if os.path.isfile(autostart_desktop_file) is False:
                    copy2(os.path.join(desktop_file),
                        os.path.join(config_home, "autostart/"))
            else:
                os.mkdir(autostart_dir)
                if os.path.isfile(autostart_desktop_file) is False:
                    copy2(os.path.join(dir_name, "resources/ubuntu-sway-welcome.desktop"),
                          os.path.join(config_home, "autostart/"))
        else:
            os.unlink(autostart_desktop_file)

    def exitApp(self):
        self.close()


class WarningMessage(QDialog):
    def __init__(self):
        super().__init__()
        self.warningDialog = Ui_WarningMessage()
        self.warningDialog.setupUi(self)


class ShellSelectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.shell_select = Ui_shellSelect()
        self.shell_select.setupUi(self)

        defaultShell = os.environ['SHELL']
        if defaultShell == "/bin/bash":
            self.shell_select.btnBash.setChecked(True)
        elif defaultShell == "/bin/zsh":
            self.shell_select.btnZSH.setChecked(True)
        elif defaultShell == "/bin/fish":
            self.shell_select.btnFish.setChecked(True)

        self.btnApply = self.shell_select.buttonBox.button(QDialogButtonBox.Apply)
        self.btnApply.clicked.connect(self.apply)

    def apply(self):
        if self.shell_select.btnBash.isChecked():
            self.shell = "/usr/bin/bash"
            subprocess.run(["pkexec", "chsh", "-s", self.shell, user])
        elif self.shell_select.btnFish.isChecked():
            self.shell = "/usr/bin/fish"
            subprocess.run(["pkexec", "chsh", "-s", self.shell, user])
        elif self.shell_select.btnZSH.isChecked():
            self.shell = "/usr/bin/zsh"
            subprocess.run(["pkexec", "chsh", "-s", self.shell, user])


def main():
    app = QApplication(["Welcome to Ubuntu Sway Remix!"])
    app.setDesktopFileName("ubuntu-sway-welcome")

    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
