from typing import assert_type

from PySide6.QtGui import QKeySequence, QShortcut
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
        self.onTabSelected(self.currentIndex())
        self.setupKeybinds()

    def onTabSelected(self, index: int) -> None:
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

    def setupKeybinds(self) -> None:
        # Next tab: Ctrl+Tab
        self.next_shortcut = QShortcut(QKeySequence("Ctrl+Tab"), self)
        self.next_shortcut.activated.connect(self.nextTab)

        # Previous tab: Ctrl+Shift+Tab
        self.prev_shortcut = QShortcut(QKeySequence("Ctrl+Shift+Tab"), self)
        self.prev_shortcut.activated.connect(self.previousTab)

    def nextTab(self) -> None:
        if self.count() > 0:
            self.setCurrentIndex((self.currentIndex() + 1) % self.count())

    def previousTab(self) -> None:
        if self.count() > 0:
            self.setCurrentIndex((self.currentIndex() - 1) % self.count())
