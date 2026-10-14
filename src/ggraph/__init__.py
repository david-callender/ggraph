import sys

from PySide6 import QtWidgets

from ggraph.calculator_view import CalculatorView
from ggraph.settings_manager import SettingsManager


def main() -> None:
    app = QtWidgets.QApplication([])
    settings = SettingsManager(app)

    widget = CalculatorView(settings)
    settings.setupTheme()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
