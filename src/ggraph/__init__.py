import sys

from PySide6 import QtWidgets

import ggraph.CalculatorView


def main() -> None:
    app = QtWidgets.QApplication([])

    widget = ggraph.CalculatorView.CalculatorView()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
