from PySide6.QtWidgets import QSizePolicy, QTabWidget

from ggraph.calculator_view import CalculatorView
from ggraph.graph_view import GraphView
from ggraph.settings_manager import SettingsManager


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
