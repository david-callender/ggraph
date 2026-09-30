
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFrame, QVBoxLayout


class HistoryLine(QFrame):

    def __init__(self, inputtedString,outputtedString):
        super().__init__()


        self.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 5px solid #cccccc; 
                border-radius: 10px;        
            }
        """)

        vLayout = QVBoxLayout()
        
        self.inputLabel = QtWidgets.QLabel(
            inputtedString, alignment=QtCore.Qt.AlignmentFlag.AlignLeft
        )

        self.inputLabel.setStyleSheet("""
            QFrame {
                background-color: #f0f0f0;
                border: 0px solid #cccccc; 
                border-radius: 10px;        
            }
        """)

        self.outputLabel = QtWidgets.QLabel(
            outputtedString, alignment=QtCore.Qt.AlignmentFlag.AlignRight
        )

        self.outputLabel.setStyleSheet("""
            QFrame {
                background-color: #cccccc;
                border: 3px solid #a0a0a0; 
                border-radius: 10px;        
            }
        """)

        vLayout.addWidget(self.inputLabel,alignment = QtCore.Qt.AlignmentFlag.AlignTop)
        vLayout.addWidget(self.outputLabel,alignment = QtCore.Qt.AlignmentFlag.AlignBottom)

        self.setLayout(vLayout)




