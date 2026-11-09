from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFrame, QVBoxLayout


class EquationLine(QFrame):
    def __init__(self) -> None:
        super().__init__()

        vLayout = QVBoxLayout()

        self.inputLine = QtWidgets.QLineEdit(
            "", alignment=QtCore.Qt.AlignmentFlag.AlignLeft
        )

        self.outputLabel = QtWidgets.QLabel(
            "", alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )

        vLayout.addWidget(self.inputLine, alignment=QtCore.Qt.AlignmentFlag.AlignTop)
        vLayout.addWidget(
            self.outputLabel, alignment=QtCore.Qt.AlignmentFlag.AlignBottom
        )

        self.setLayout(vLayout)

    def themeOutputLabel(self, isError: bool) -> None:
        if isError:
            self.outputLabel.setProperty("class", "label-error")
        else:
            self.outputLabel.setProperty("class", "label-secondary")
