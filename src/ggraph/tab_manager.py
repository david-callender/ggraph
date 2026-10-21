from typing import assert_type

from PySide6.QtWidgets import QSizePolicy, QTabWidget

from ggraph.calculator_view import CalculatorView
from ggraph.graph_view import GraphView
from ggraph.settings_manager import SettingsManager
from ggraph.tab_interface import TabInterface


class TabManager(QTabWidget):
    def __init__(self, settings: SettingsManager):
        super().__init__()
        self.calculatorView = CalculatorView(settings)
        self.graphView = GraphView(settings)

        self.addTab(self.calculatorView, "Calculator")
        self.addTab(self.graphView, "graph")

        self.setDocumentMode(True)
        self.tabBar().setExpanding(True)
        self.setContentsMargins(10, 10, 10, 10)

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.currentChanged.connect(self.onTabSelected)

    def onTabSelected(self, index: int):
        print(index)
        for i in range(self.count()):
            widget = self.widget(i)
            if not isinstance(widget, TabInterface):
                raise TypeError("Widget is not a TabInterface")
            else:
                assert_type(widget, TabInterface)

            if i == index:
                widget.onFocused()
            else:
                widget.onUnfocused()
