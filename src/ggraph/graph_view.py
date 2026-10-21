from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QVBoxLayout

from ggraph.history_line import HistoryLine
from ggraph.history_manager import HistoryManager
from ggraph.interpreter import Env, InterpreterError, interpret
from ggraph.lexer import Lexer, LexerError
from ggraph.parser import Parser, ParserError
from ggraph.settings_manager import SettingsManager
from ggraph.tab_interface import TabInterface


class GraphView(TabInterface):
    def __init__(self, settings: SettingsManager) -> None:
        super().__init__()

        self.settings = settings

        self.mathsBox = QtWidgets.QLineEdit("")
        self.historyManager = HistoryManager()
        self.submitMathButton = QtWidgets.QPushButton("Graph Mode")
        self.historyScroller = QtWidgets.QScrollArea()
        self.historyHolder = QtWidgets.QFrame()
        self.scrollbar = self.historyScroller.verticalScrollBar()

        self.historyLayout = QVBoxLayout(self.historyHolder)
        self.historyLayout.addStretch()
        self.historyLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.historyScroller.setWidget(self.historyHolder)
        self.historyScroller.setWidgetResizable(True)

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.historyScroller)
        layout.addWidget(self.mathsBox)
        layout.addWidget(self.submitMathButton)

    def onFocused(self):
        print("graph focused")

    def parseMath(self, input: str) -> tuple[str, bool]:
        try:
            l = Lexer(input)
            p = Parser(l).parse()
            p.reverse()
            env = Env(None)
            return (str(interpret(p, env)), False)
        except (LexerError, ParserError, InterpreterError, ZeroDivisionError) as e:
            return (str(e), True)

    @QtCore.Slot()
    def submitMath(self) -> None:
        text = self.mathsBox.text()

        parsedResult = self.parseMath(
            text
        )  # A tuple of a string representing the output, and a Boolean that is True if an error ocurred.

        self.mathsBox.setFocus()

        newHistoryRow = HistoryLine(text, parsedResult[0])
        newHistoryRow.themeOutputLabel(parsedResult[1])
        self.historyLayout.addWidget(newHistoryRow)
        self.historyManager.addToCalcHistory(text)
        self.historyManager.addToCalcHistory(parsedResult[0])

        self.mathsBox.setText("")

        # Wait for the scrollbar max value to update, then scroll to the bottom
        QtCore.QTimer.singleShot(
            5, lambda: self.scrollbar.setValue(self.scrollbar.maximum())
        )

        print(text + ": " + parsedResult[0])

    def setupKeybinds(self) -> None:

        self.submitMathButton.setShortcut(QKeySequence("Return"))
        self.nextHistory = QShortcut(QKeySequence("Up"), self)
        self.previousHistory = QShortcut(QKeySequence("Down"), self)

        # Only activate up and down when the CalculatorView or its children are focuesed
        self.previousHistory.setContext(
            QtCore.Qt.ShortcutContext.WidgetWithChildrenShortcut
        )
        self.nextHistory.setContext(
            QtCore.Qt.ShortcutContext.WidgetWithChildrenShortcut
        )

        self.nextHistory.activated.connect(self.applyNextHistoryItem)
        self.previousHistory.activated.connect(self.applyPreviousHistoryItem)

    def applyNextHistoryItem(self) -> None:
        self.mathsBox.setText(self.historyManager.getNextHistoryItem())

    def applyPreviousHistoryItem(self) -> None:
        self.mathsBox.setText(self.historyManager.getPreviousHistoryItem())
