from typing import override

from PySide6 import QtWidgets
from PySide6.QtCore import QLineF
from PySide6.QtGui import QColor, QPainter, QPen
from PySide6.QtWidgets import QSizePolicy

from ggraph.interpreter import Env, InterpreterError, interpret
from ggraph.lexer import Lexer, LexerError
from ggraph.parser import Parser, ParserError
from ggraph.settings_manager import SettingsManager


class GraphCanvas(QtWidgets.QWidget):
    def __init__(self, settings: SettingsManager, parent=None) -> None:
        super().__init__(parent)
        self.settings = settings
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.points: list[tuple[float, float | None]] = []
        self.inputStrings: list[str] = [""]

    def drawGraph(self) -> None:
        self.calculatePoints()
        painter = QPainter(self)

        if not self.settings.useSystemTheme():
            painter.fillRect(
                self.rect(), QColor("#" + self.settings.getColorBackground())
            )
        painter.setPen(
            QPen(
                QColor(self.getGraphColor(0)),
                self.settings.getGraphLineWidth(),
            )
        )

        if len(self.points) == 0:
            painter.end()
            return

        convertedPoints = self.convertGraphPointListToViewPointList(self.points)

        if len(convertedPoints) == 1:
            self.createLine(
                painter,
                convertedPoints[0][0],
                convertedPoints[0][1],
                convertedPoints[0][0],
                convertedPoints[0][1],
            )

            painter.end()
            return

        for i in range(len(self.points) - 1):
            self.createLine(
                painter,
                convertedPoints[i][0],
                convertedPoints[i][1],
                convertedPoints[i + 1][0],
                convertedPoints[i + 1][1],
            )

        painter.end()

    def createLine(
        self,
        painter: QPainter,
        x1: float,
        y1: float | None,
        x2: float,
        y2: float | None,
    ) -> None:
        if y1 is None or y2 is None:
            return
        line = QLineF(
            x1,
            y1,
            x2,
            y2,
        )
        painter.drawLine(line)

    @override
    def paintEvent(self, event) -> None:
        self.drawGraph()

    def convertGraphPointListToViewPointList(
        self, points: list[tuple[float, float | None]]
    ) -> list[tuple[float, float | None]]:

        viewWidth = self.width()
        viewHeight = self.height()
        minX = self.settings.getGraphMinX()
        maxX = self.settings.getGraphMaxX()
        graphWidth = maxX - minX
        minY = self.settings.getGraphMinY()
        maxY = self.settings.getGraphMaxY()
        graphHeight = maxY - minY

        newPoints: list[tuple[float, float | None]] = [(0.0, 0.0)] * len(points)
        for i in range(len(points)):
            newPoints[i] = self.convertGraphPointToViewPoint(
                points[i], minX, minY, graphWidth, graphHeight, viewWidth, viewHeight
            )
        return newPoints

    def convertGraphPointToViewPoint(
        self,
        point: tuple[float, float | None],
        minX: float,
        minY: float,
        graphWidth: float,
        graphHeight: float,
        viewWidth: float,
        viewHeight: float,
    ) -> tuple[float, float | None]:
        x = point[0]
        y = point[1]

        x = ((x - minX) / graphWidth) * viewWidth
        if y is None:
            return (x, y)
        y = ((y - minY) / graphHeight) * viewHeight

        y = viewHeight - y

        return (x, y)

    def parseMath(self, input: str) -> None:
        try:
            l = Lexer(input)
            p = Parser(l).parse()
            print(p)

            env = Env(None)
            for i in range(len(self.points)):
                x = self.points[i][0]
                env.vars["x"] = x
                try:
                    y = interpret(p[:], env)
                    if isinstance(y, complex):
                        y = None  # we can handle graphing complex points later for radial or something
                except (
                    LexerError,
                    ParserError,
                    InterpreterError,
                    ZeroDivisionError,
                    TypeError,
                ) as e:
                    print(e)
                    y = None
                self.points[i] = (x, y)
        except (LexerError, ParserError, InterpreterError, ZeroDivisionError) as e:
            print(e)

    def calculatePoints(self) -> None:
        steps = self.settings.getGraphHSteps()
        self.points = [(0, 0)] * steps

        minX = self.settings.getGraphMinX()
        maxX = self.settings.getGraphMaxX()
        graphWidth = maxX - minX

        for i in range(steps):
            x = (i / steps) * graphWidth + minX
            self.points[i] = (
                x,
                0,
            )  # 0 is a placeholder value here, until replaced with actual value

        self.parseMath(self.inputStrings[0])

    def getGraphColor(self, eqnId: int) -> str:
        if self.settings.useSystemTheme():
            eqnId = eqnId % 5
            match eqnId:
                case 0:
                    return "RED"
                case 1:
                    return "BLUE"
                case 2:
                    return "ORCHID"
                case 3:
                    return "GREEN"
                case 4:
                    return "PERU"
        else:
            eqnId = eqnId % 3
            match eqnId:
                case 0:
                    return "#" + self.settings.getColorPrimary()
                case 1:
                    return "#" + self.settings.getColorSecondary()
                case 2:
                    return "#" + self.settings.getColorOnSurface()
        return "HOTPINK"
