from abc import abstractmethod

from PySide6.QtWidgets import QWidget


class TabInterface(QWidget):
    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def onFocused(self):
        raise NotImplementedError("onFocused not set up")

    @abstractmethod
    def onUnfocused(self):
        raise NotImplementedError("onUnfocused not set up")
