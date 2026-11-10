import math
from typing import override

from PySide6 import QtWidgets
from PySide6.QtCore import QLineF
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QSizePolicy

from ggraph.settings_manager import SettingsManager


class GraphCanvas(QtWidgets.QWidget):
    def __init__(self, settings: SettingsManager, parent=None) -> None:
        super().__init__(parent)
        self.settings = settings
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.points: list[tuple[float, float]] = []

    @override
    def paintEvent(self, event) -> None:
        self.graph()
        painter = QPainter(self)

        if not self.settings.useSystemTheme():
            painter.fillRect(
                self.rect(), QColor("#" + self.settings.getColorBackground())
            )
            painter.setPen(QPen(QColor("#" + self.settings.getColorPrimary()), 3))

        if len(self.points) == 0:
            painter.end()
            return

        convertedPoints = self.convertGraphPointListToViewPointList(self.points)

        if len(convertedPoints) == 1:
            line = QLineF(
                convertedPoints[0][0],
                convertedPoints[0][1],
                convertedPoints[0][0],
                convertedPoints[0][1],
            )
            painter.drawLine(line)

            painter.end()
            return

        for i in range(len(self.points) - 1):
            line = QLineF(
                convertedPoints[i][0],
                convertedPoints[i][1],
                convertedPoints[i + 1][0],
                convertedPoints[i + 1][1],
            )
            painter.drawLine(line)

        painter.end()

    def convertGraphPointListToViewPointList(
        self, points: list[tuple[float, float]]
    ) -> list[tuple[float, float]]:

        viewWidth = self.width()
        viewHeight = self.height()
        minX = self.settings.getGraphMinX()
        maxX = self.settings.getGraphMaxX()
        graphWidth = maxX - minX
        minY = self.settings.getGraphMinY()
        maxY = self.settings.getGraphMaxY()
        graphHeight = maxY - minY

        newPoints = [(0.0, 0.0)] * len(points)
        for i in range(len(points)):
            newPoints[i] = self.convertGraphPointToViewPoint(
                points[i], minX, minY, graphWidth, graphHeight, viewWidth, viewHeight
            )
        return newPoints

    def convertGraphPointToViewPoint(
        self,
        point: tuple[float, float],
        minX: float,
        minY: float,
        graphWidth: float,
        graphHeight: float,
        viewWidth: float,
        viewHeight: float,
    ) -> tuple[float, float]:
        x = point[0]
        y = point[1]

        x = ((x - minX) / graphWidth) * viewWidth
        y = ((y - minY) / graphHeight) * viewHeight

        y = viewHeight / 2 - y

        return (x, y)

    def funcOfX(self, x: float) -> float:
        return 50 * math.sin(x / 60)

    def graph(self) -> None:
        steps = self.settings.getGraphHSteps()
        self.points = [(0, 0)] * steps

        minX = self.settings.getGraphMinX()
        maxX = self.settings.getGraphMaxX()
        graphWidth = maxX - minX
        minY = self.settings.getGraphMinY()

        for i in range(steps):
            x = (i / steps) * graphWidth + minX
            y = self.funcOfX(x) + minY
            self.points[i] = (x, y)
        print(self.points[-1])
