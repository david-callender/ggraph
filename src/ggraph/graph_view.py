from typing import override

from PySide6 import QtWidgets
from PySide6.QtWidgets import QSizePolicy

from ggraph.equation_line import EquationLine
from ggraph.graph_canvas import GraphCanvas
from ggraph.interpreter import Env, InterpreterError, interpret
from ggraph.lexer import Lexer, LexerError
from ggraph.parser import Parser, ParserError
from ggraph.settings_manager import SettingsManager
from ggraph.tab_interface import TabInterface


class GraphView(TabInterface):
    def __init__(self, settings: SettingsManager) -> None:
        super().__init__()

        self.settings = settings

        self.graphScroller = QtWidgets.QScrollArea()
        self.graphHolder = GraphCanvas(self.settings)

        # self.equationScroller = QtWidgets.QScrollArea()
        # self.equationHolder = QWidget()
        self.equationLine = EquationLine()

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

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.graphScroller)
        layout.addWidget(self.equationLine)

    @override
    def onFocused(self) -> None:
        pass

    @override
    def onUnfocused(self) -> None:
        pass

    def parseMath(self, input: str) -> tuple[str, bool]:
        try:
            l = Lexer(input)
            p = Parser(l).parse()
            p.reverse()
            env = Env(None)
            return (str(interpret(p, env)), False)
        except (LexerError, ParserError, InterpreterError, ZeroDivisionError) as e:
            return (str(e), True)
