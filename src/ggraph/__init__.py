import sys

from PySide6 import QtWidgets

from ggraph.settings_manager import SettingsManager
from ggraph.tab_manager import TabManager


def main() -> None:
    app = QtWidgets.QApplication([])
    settings = SettingsManager(app)

    widget = TabManager(settings)

    settings.setupTheme()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
