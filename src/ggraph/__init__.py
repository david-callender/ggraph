import random
import sys
import time

from PySide6 import QtCore, QtWidgets

from ggraph.interpreter import Env, interpret
from ggraph.lexer import Lexer
from ggraph.parser import Parser
from ggraph.tokens import (
    Token,
    TokenAdd,
    TokenFuncCall,
    TokenFuncDef,
    TokenMul,
    TokenNumLit,
    TokenVar,
)


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel(
            "Hello World", alignment=QtCore.Qt.AlignmentFlag.AlignCenter
        )

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


def main() -> None:
    time_start = time.time()
    l = Lexer("6 * (5 + 7) / 4 - 7 * 2 + 3 * 3")
    p = Parser(l)
    parsed = p.parse()
    print(parsed)
    parsed.reverse()
    for i in range(1000000):
        env = Env(None)
        result = interpret(parsed[::], env)
        assert result == 13

    time_delta = time.time() - time_start
    print(time_delta)

    # app = QtWidgets.QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    # sys.exit(app.exec())
