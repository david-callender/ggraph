import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QKeySequence
from PySide6.QtWidgets import QVBoxLayout

import ggraph.HistoryLine


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.mathsBox = QtWidgets.QLineEdit("testing 123")
        self.submitMath = QtWidgets.QPushButton("Submit Math")
        self.historyScroller = QtWidgets.QScrollArea()
        self.historyHolder = QtWidgets.QFrame()


        self.historyScroller.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 1px solid #cccccc; 
                border-radius: 10px;        
            }
        """)

        historyLayout = QVBoxLayout(self.historyHolder)
        historyLayout.addStretch()
        historyLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.historyScroller.setWidget(self.historyHolder)
        self.historyScroller.setWidgetResizable(True)

        self.submitMath.clicked.connect(self.parseMath)
        self.submitMath.setShortcut(QKeySequence("Return"))

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.historyScroller)
        layout.addWidget(self.mathsBox)
        layout.addWidget(self.submitMath)


    @QtCore.Slot()
    def parseMath(self):
        text = self.mathsBox.text()
        parsedResult = text + " I done thunked about this"

        newHistoryRow = ggraph.HistoryLine.HistoryLine(text,parsedResult)
        self.historyHolder.layout().addWidget(newHistoryRow)

        print(text + ": " + parsedResult)


def main() -> None:
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
