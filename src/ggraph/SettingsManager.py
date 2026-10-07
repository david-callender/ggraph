from PySide6 import QtCore, QtWidgets


class SettingsManager(QtCore.QSettings):
    def __init__(self):
        super().__init__("Social Coding", "GGraph")

    def getRoundingRadiusSmall(self):
        return self.value("ui/smallCornerRadius",5)

    def getRoundingRadiusMed(self):
        return self.value("ui/medlCornerRadius",2)

    def getRoundingRadiusBig(self):
        return self.value("ui/bigCornerRadius",10)

    def getBorderRadiusBig(self):
        return self.value("ui/bigBorderRadius",3)

    def getBorderRadiusMed(self):
        return self.value("ui/medgBorderRadius",2)

    def getBorderRadiusSmall(self):
        return self.value("ui/smallBorderRadius",1)

    def getColorBackground(self):
        return self.value("ui/backgroundColor","161217")

    def getColorSurface(self):
        return self.value("ui/surfaceColor","161217")

    def getColorOnSurface(self):
        return self.value("ui/onSurfaceColor","e8e0e8")   

    def getColorOnBackground(self):
        return self.value("ui/onBackgroundColor","e8e0e8")   

    def getColorError(self):
        return self.value("ui/errorColor","ffb4ab")   

    def getColorPrimary(self):
        return self.value("ui/primaryColor","deb8f7")   

    def getColorOnPrimary(self):
        return self.value("ui/primaryOnColor","402357")   

    def getColorSecondary(self):
        return self.value("ui/secondaryColor","2d2433")   

    def getColorOnSecondary(self):
        return self.value("ui/secondaryOnColor","d1c1d9")   


    def setupTheme(self, app:QtWidgets.QApplication):
        app.setStyleSheet(f"""
                QWidget {{
                    background-color: #{self.getColorBackground()};
                    border: {self.getBorderRadiusBig()}px solid #{self.getColorOnBackground()}; 
                    border-radius: {self.getRoundingRadiusBig()}px;        
                }}
                QFrame {{
                    background-color: #{self.getColorSurface()};
                    border: {self.getBorderRadiusMed()}px solid #{self.getColorOnSurface()}; 
                    border-radius: {self.getRoundingRadiusBig()}px;        
                }}
                QLineEdit {{
                    color: #{self.getColorOnSurface()};
                    background-color: #{self.getColorSurface()};
                    border: {self.getBorderRadiusSmall()}px solid #{self.getColorOnSurface()}; 
                    border-radius: {self.getRoundingRadiusSmall()}px;        
                }}
                QLabel {{
                    color: #{self.getColorOnSurface()};
                    background-color: #{self.getColorSurface()};
                    border: {self.getBorderRadiusSmall()}px solid #{self.getColorOnSurface()}; 
                    border-radius: {self.getRoundingRadiusSmall()}px;
                }}
                QPushButton {{
                    color: #{self.getColorOnPrimary()};
                    background-color: #{self.getColorPrimary()};
                    border: {self.getBorderRadiusBig()}px solid #{self.getColorOnPrimary()}; 
                    border-radius: {self.getRoundingRadiusBig()}px;        
                }}
                
            """)

    def themeSecondaryLabel(self, label: QtWidgets.QLabel):
        label.setStyleSheet(f"""
                QLabel {{
                    color: #{self.getColorOnSecondary()};
                    background-color: #{self.getColorSecondary()};
                    border: {self.getBorderRadiusSmall()}px solid #{self.getColorOnSecondary()}; 
                    border-radius: {self.getRoundingRadiusSmall()}px;
                }}
            """)

    def themeErrorLabel(self, label: QtWidgets.QLabel):
        label.setStyleSheet(f"""
                QLabel {{
                    color: #{self.getColorError()};
                    background-color: #{self.getColorSecondary()};
                    border: {self.getBorderRadiusSmall()}px solid #{self.getColorOnSecondary()}; 
                    border-radius: {self.getRoundingRadiusSmall()}px;
                }}
            """)
