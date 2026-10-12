import random
import sys

from PySide6 import QtCore, QtWidgets

from ggraph.interpreter import Env, interpret
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
    # F(x) = 2x
    f_func_body: list[Token] = [TokenNumLit(2), TokenVar("x"), TokenMul()]
    f_func_body.reverse()

    # G(x) = 5x + 2
    g_func_body: list[Token] = [
        TokenNumLit(5),
        TokenVar("x"),
        TokenMul(),
        TokenNumLit(2),
        TokenAdd(),
    ]
    g_func_body.reverse()

    # F(G(4))

    program: list[Token] = [
        TokenFuncDef("F", ["x"], f_func_body),
        TokenFuncDef("G", ["x"], g_func_body),
        TokenNumLit(4),
        TokenFuncCall("G", 1),
        TokenFuncCall("F", 1),
    ]

    program.reverse()

    print(interpret(program, Env(None)))

    # app = QtWidgets.QApplication([])

    # widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()

    # sys.exit(app.exec())
