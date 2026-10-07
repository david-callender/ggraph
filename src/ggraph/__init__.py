import sys

from PySide6 import QtWidgets

import ggraph.CalculatorView
import ggraph.SettingsManager


def main() -> None:
    app = QtWidgets.QApplication([])
    settings = ggraph.SettingsManager.SettingsManager(app)

    widget = ggraph.CalculatorView.CalculatorView(settings)
    settings.setupTheme()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
