import csv
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from gui import *

class Logic(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)


        self.ui.power_button.clicked.connect(self.toggle_power)
        self.ui.volume_up.clicked.connect(self.volume_up)
        self.ui.volume_down.clicked.connect(self.volume_down)
        self.ui.channel_up.clicked.connect(self.channel_up)
        self.ui.channel_down.clicked.connect(self.channel_down)
        self.ui.mute_button.clicked.connect(self.mute)

        # Channel buttons
        self.ui.channel_button_1.clicked.connect(lambda: self.change_channel(1))
        self.ui.channel_button_2.clicked.connect(lambda: self.change_channel(2))
        self.ui.channel_button_3.clicked.connect(lambda: self.change_channel(3))
        self.ui.channel_button_4.clicked.connect(lambda: self.change_channel(4))
        self.ui.channel_button_5.clicked.connect(lambda: self.change_channel(5))
        self.ui.channel_button_6.clicked.connect(lambda: self.change_channel(6))
        self.ui.channel_button_7.clicked.connect(lambda: self.change_channel(7))
        self.ui.channel_button_8.clicked.connect(lambda: self.change_channel(8))
        self.ui.channel_button_9.clicked.connect(lambda: self.change_channel(9))

        # State variables
        self.power_on = False
        self.volume = 50
        self.channel = 1

    def toggle_power(self):
        self.power_on = not self.power_on
        status = "ON" if self.power_on else "OFF"
        QMessageBox.information(self, "Power", f"TV turned {status}")

    def volume_up(self):
        if self.power_on:
            if self.volume:
                self.mute()
            self.volume = min(self.volume + 10, 100)
            QMessageBox.information(self, "Volume", f"Volume increased to {self.volume}")
        else:
            QMessageBox.warning(self, "Power Off", "Turn on the TV first!")

    def volume_down(self):
        if self.power_on:
            if self.volume:
                self.mute()
            self.volume = max(self.volume - 10, 0)
            QMessageBox.information(self, "Volume", f"Volume decreased to {self.volume}")
        else:
            QMessageBox.warning(self, "Power Off", "Turn on the TV first!")

    def channel_up(self):
        if self.power_on:
            self.channel = self.channel + 1 if self.channel < 9 else 1
            QMessageBox.information(self, "Channel", f"Channel changed to {self.channel}")
        else:
            QMessageBox.warning(self, "Power Off", "Turn on the TV first!")

    def channel_down(self):
        if self.power_on:
            self.channel = self.channel - 1 if self.channel > 1 else 9
            QMessageBox.information(self, "Channel", f"Channel changed to {self.channel}")
        else:
            QMessageBox.warning(self, "Power Off", "Turn on the TV first!")

    def mute(self):
        if self.power_on:
            self.volume = not self.volume
            if self.volume:
                QMessageBox.information(self, "Mute", "TV muted")
            else:
                QMessageBox.warning(self, "Power Off", "Turn on the TV first!")
        else:
            QMessageBox.warning(self, "Power Off", "Turn on the TV first!")
    def change_channel(self, channel):
        if self.power_on:
            self.channel = channel
            self.ui.progressBar.setValue(self.channel)
            QMessageBox.information(self, "Channel", f"Channel changed to {channel}")
        else:
            QMessageBox.warning(self, "Power Off", "Turn on the TV first!")

# https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/
# https://realpython.com/python-pyqt-gui-calculator/#dialogs


