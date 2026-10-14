from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QVBoxLayout

from ggraph.history_line import HistoryLine
from ggraph.history_manager import HistoryManager
from ggraph.interpreter import Env, interpret
from ggraph.lexer import Lexer
from ggraph.parser import Parser


class CalculatorView(QtWidgets.QWidget):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings

        self.mathsBox = QtWidgets.QLineEdit("")
        self.historyManager = HistoryManager()
        self.submitMathButton = QtWidgets.QPushButton("Submit Math")
        self.historyScroller = QtWidgets.QScrollArea()
        self.historyHolder = QtWidgets.QFrame()
        self.scrollbar = self.historyScroller.verticalScrollBar()

        historyLayout = QVBoxLayout(self.historyHolder)
        historyLayout.addStretch()
        historyLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.historyScroller.setWidget(self.historyHolder)
        self.historyScroller.setWidgetResizable(True)

        self.submitMathButton.clicked.connect(self.submitMath)
        self.setupKeybinds()

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.historyScroller)
        layout.addWidget(self.mathsBox)
        layout.addWidget(self.submitMathButton)

        self.mathsBox.setFocus()

    def parseMath(self,input):
        l = Lexer(input)
        p = Parser(l).parse()
        p.reverse()
        env = Env(None)

        return (interpret(p,env).__str__() , False)



    @QtCore.Slot()
    def submitMath(self):
        text = self.mathsBox.text()

        parsedResult = self.parseMath(text) # A tuple of a string representing the output, and a Boolean that is True if an error ocurred.

        self.mathsBox.setFocus()

        newHistoryRow = HistoryLine(text,parsedResult[0])
        newHistoryRow.themeOutputLabel(parsedResult[1])
        self.historyHolder.layout().addWidget(newHistoryRow)
        self.historyManager.addToCalcHistory(text)
        self.historyManager.addToCalcHistory(parsedResult[0])

        self.mathsBox.setText("")

        # Wait for the scrollbar max value to update, then scroll to the bottom
        QtCore.QTimer.singleShot(5, lambda: self.scrollbar.setValue(self.scrollbar.maximum()))

        print(text + ": " + parsedResult[0])

    def setupKeybinds(self):

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


    def applyNextHistoryItem(self):
        self.mathsBox.setText(self.historyManager.getNextHistoryItem())

    def applyPreviousHistoryItem(self):
        self.mathsBox.setText(self.historyManager.getPreviousHistoryItem())

