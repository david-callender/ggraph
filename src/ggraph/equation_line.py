from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFrame, QHBoxLayout

from ggraph.graph_canvas import GraphCanvas


class EquationLine(QFrame):
    def __init__(self, graphCanvas: GraphCanvas, myEqnId: int) -> None:
        super().__init__()

        self.graphInputStrings = graphCanvas.inputStrings
        self.onEqnUpdate = graphCanvas.update
        self.eqnId = myEqnId

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

        self.inputLine.textEdited.connect(self.updateMyGraphInputString)

    def updateMyGraphInputString(self) -> None:
        self.graphInputStrings[self.eqnId] = self.inputLine.text()
        self.onEqnUpdate()

    def themeOutputLabel(self, isError: bool) -> None:
        if isError:
            self.inputLine.setProperty("class", "label-error")
        else:
            self.inputLine.setProperty("class", "label-secondary")
