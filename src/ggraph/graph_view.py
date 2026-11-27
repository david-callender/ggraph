from typing import override

from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy

from ggraph.equation_line import EquationLine
from ggraph.graph_canvas import GraphCanvas
from ggraph.settings_manager import SettingsManager
from ggraph.tab_interface import TabInterface


class GraphView(TabInterface):
    def __init__(self, settings: SettingsManager) -> None:
        super().__init__()

        self.settings = settings

        self.graphScroller = QtWidgets.QScrollArea()
        self.graphHolder = GraphCanvas(self.settings)

        self.equationLine = EquationLine(self.graphHolder, 0)

        # self.graphLayout = QVBoxLayout(self.graphHolder)
        # self.graphLayout.addStretch()
        self.graphHolder.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        self.graphScroller.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )

        self.graphScroller.setWidget(self.graphHolder)
        self.graphScroller.setWidgetResizable(True)

        if self.width() < self.height():
            layout = QtWidgets.QHBoxLayout(self)
        else:
            layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.equationLine)
        layout.addWidget(self.graphScroller)

    @override
    def onFocused(self) -> None:
        self.equationLine.inputLine.setFocus()

    @override
    def onUnfocused(self) -> None:
        pass
