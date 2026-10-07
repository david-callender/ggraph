from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFrame, QVBoxLayout


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

    def themeOutputLabel(self, isError):
        if isError:
            self.outputLabel.setProperty("class","label-error")
        else:
            self.outputLabel.setProperty("class","label-secondary")

        




