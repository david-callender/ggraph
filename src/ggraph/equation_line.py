from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFrame, QHBoxLayout


class EquationLine(QFrame):
    def __init__(self) -> None:
        super().__init__()

        hLayout = QHBoxLayout()

        self.inputLine = QtWidgets.QLineEdit(
            "", alignment=QtCore.Qt.AlignmentFlag.AlignLeft
        )
        # self.inputLine.keyPressEvent.connect

        self.typeDropBox = QtWidgets.QComboBox()
        self.typeDropBox.addItems(["Y=", "X=", "Implicit", "Def", "Auto"])

        hLayout.addWidget(
            self.typeDropBox, -1, alignment=QtCore.Qt.AlignmentFlag.AlignLeft
        )
        hLayout.addWidget(self.inputLine, 900)

        self.setLayout(hLayout)

    def themeOutputLabel(self, isError: bool) -> None:
        if isError:
            self.inputLine.setProperty("class", "label-error")
        else:
            self.inputLine.setProperty("class", "label-secondary")
