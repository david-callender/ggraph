import os.path as osPath

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QFileSystemWatcher


class SettingsManager(QtCore.QSettings):
    def __init__(self,app: QtWidgets.QApplication):
        super().__init__("Social-Coding", "GGraph")
        self.app = app

        if self.allKeys().__len__() == 0:
            print("No config file found, creating default")
            self.createConfigFile()

        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(osPath.dirname(self.fileName()))
        self.watcher.addPath(self.fileName())
        self.watcher.directoryChanged.connect(self.reloadConfig)
        self.watcher.fileChanged.connect(self.reloadConfig)

        self.reloadConfig()

    def reloadConfig(self):
        self.sync()

        print("Reloading Config from File")

        if self.fileName() not in self.watcher.files():
            self.watcher.addPath(self.fileName())

        self.setupTheme()
            

    def getRoundingRadiusSmall(self):
        return self.value("ui/smallCornerRadius",5)

    def getRoundingRadiusMed(self):
        return self.value("ui/medCornerRadius",2)

    def getRoundingRadiusBig(self):
        return self.value("ui/bigCornerRadius",10)

    def getBorderRadiusBig(self):
        return self.value("ui/bigBorderRadius",3)

    def getBorderRadiusMed(self):
        return self.value("ui/medBorderRadius",2)

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


    def setupTheme(self):
        self.app.setStyleSheet(f"""
                QWidget {{
                    background-color: #{self.getColorBackground()};
                    border: {self.getBorderRadiusBig()}px solid #{self.getColorOnBackground()}; 
                    border-radius: {self.getRoundingRadiusBig()}px;        
                }}
                QFrame {{
                    background-color: #{self.getColorSurface()};
                    border: {self.getBorderRadiusSmall()}px solid #{self.getColorOnSurface()}; 
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
                QLabel[class="label-error"] {{
                    color: #{self.getColorOnSecondary()};
                    background-color: #{self.getColorError()};
                    border: {self.getBorderRadiusSmall()}px solid #{self.getColorOnSecondary()}; 
                    border-radius: {self.getRoundingRadiusSmall()}px;
                }}
                QLabel[class="label-secondary"] {{
                    color: #{self.getColorOnSurface()};
                    background-color: #{self.getColorSurface()};
                    border: {self.getBorderRadiusMed()}px solid #{self.getColorSecondary()}; 
                    border-radius: {self.getRoundingRadiusSmall()}px;
                }}
                QPushButton {{
                    color: #{self.getColorOnPrimary()};
                    background-color: #{self.getColorPrimary()};
                    border: {self.getBorderRadiusBig()}px solid #{self.getColorOnPrimary()}; 
                    border-radius: {self.getRoundingRadiusBig()}px;        
                }}

                /* ===================================================================
                   ScrollBar and its many bits
                   =================================================================== */
                QScrollBar:vertical {{
                    background-color: #{self.getColorSurface()};
                    border: none;
                    width: 12px;
                    margin: 0px;
                }}

                QScrollBar:horizontal {{
                    background-color: #{self.getColorSurface()};
                    border: none;
                    height: 12px;
                    margin: 0px;
                }}
                
                QScrollBar::handle:vertical,
                QScrollBar::handle:horizontal {{
                    background-color: #{self.getColorPrimary()};
                    border: {self.getBorderRadiusSmall()}px solid #{self.getColorOnPrimary()};
                    border-radius: {self.getRoundingRadiusSmall()}px;
                    margin: 0px;
                }}

                QScrollBar::handle:vertical {{
                    min-height: 20px;
                }}

                QScrollBar::handle:horizontal {{
                    min-width: 20px;
                }}

                /* Hover and Pressed States for Handle */
                QScrollBar::handle:vertical:hover,
                QScrollBar::handle:horizontal:hover {{
                    background-color: #{self.getColorSecondary()};
                    border-color: #{self.getColorOnSecondary()};
                }}

                QScrollBar::handle:vertical:pressed,
                QScrollBar::handle:horizontal:pressed {{
                    background-color: #{self.getColorOnSurface()};
                }}

                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
                    border: none;
                    background: none;
                    height: 0px;
                    width: 0px;
                }}

                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical,
                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
                    background: none;
                }}

                
            """)

    def createConfigFile(self):
        self.setValue("ui/smallCornerRadius",self.getRoundingRadiusSmall())
        self.setValue("ui/medCornerRadius",self.getRoundingRadiusMed())
        self.setValue("ui/bigCornerRadius",self.getRoundingRadiusBig())
        self.setValue("ui/bigBorderRadius",self.getBorderRadiusBig())
        self.setValue("ui/medBorderRadius",self.getBorderRadiusMed())
        self.setValue("ui/smallBorderRadius",self.getBorderRadiusSmall())
        self.setValue("ui/backgroundColor",self.getColorBackground())
        self.setValue("ui/surfaceColor",self.getColorSurface())
        self.setValue("ui/onSurfaceColor",self.getColorOnSurface())   
        self.setValue("ui/onBackgroundColor",self.getColorOnBackground())   
        self.setValue("ui/errorColor",self.getColorError())   
        self.setValue("ui/primaryColor",self.getColorPrimary())   
        self.setValue("ui/primaryOnColor",self.getColorOnPrimary())   
        self.setValue("ui/secondaryColor",self.getColorSecondary())   
        self.setValue("ui/secondaryOnColor",self.getColorOnSecondary())   
