from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFrame, QVBoxLayout

import ggraph.SettingsManager


class HistoryLine(QFrame):

    def __init__(self, inputtedString,outputtedString):
        super().__init__()

        vLayout = QVBoxLayout()
        
        self.inputLabel = QtWidgets.QLabel(
            inputtedString, alignment=QtCore.Qt.AlignmentFlag.AlignLeft
        )

        self.outputLabel = QtWidgets.QLabel(
            outputtedString, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )

        vLayout.addWidget(self.inputLabel,alignment = QtCore.Qt.AlignmentFlag.AlignTop)
        vLayout.addWidget(self.outputLabel,alignment = QtCore.Qt.AlignmentFlag.AlignBottom)

        self.setLayout(vLayout)

    def themeOutputLabel(self, isError,settings: ggraph.SettingsManager.SettingsManager):
        if isError:
            settings.themeErrorLabel(self.outputLabel)
        else:
            settings.themeSecondaryLabel(self.outputLabel)
        




