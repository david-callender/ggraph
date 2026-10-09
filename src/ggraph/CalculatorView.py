from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QVBoxLayout

from ggraph.HistoryLine import HistoryLine
from ggraph.HistoryManager import HistoryManager


class CalculatorView(QtWidgets.QWidget):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings

        self.mathsBox = QtWidgets.QLineEdit("")
        self.historyManager = HistoryManager()
        self.submitMath = QtWidgets.QPushButton("Submit Math")
        self.historyScroller = QtWidgets.QScrollArea()
        self.historyHolder = QtWidgets.QFrame()
        self.scrollbar = self.historyScroller.verticalScrollBar()

        historyLayout = QVBoxLayout(self.historyHolder)
        historyLayout.addStretch()
        historyLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.historyScroller.setWidget(self.historyHolder)
        self.historyScroller.setWidgetResizable(True)

        self.submitMath.clicked.connect(self.parseMath)
        self.setupKeybinds()

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.historyScroller)
        layout.addWidget(self.mathsBox)
        layout.addWidget(self.submitMath)

        self.mathsBox.setFocus()


    @QtCore.Slot()
    def parseMath(self):
        text = self.mathsBox.text()

        parsedResult = (text + " I done thunked about this", False) # A tuple of a string representing the output, and a Boolean that is True if an error ocurred.

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

        self.submitMath.setShortcut(QKeySequence("Return"))
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

