from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from Node import Node

class OverlayWindow(QWidget, Node):
    def __init__(self, x:int, y:int, w:int, h:int, Data):
        super(QWidget, self).__init__()
        super(Node, self).__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.InitWidgets(Data)
        
    def InitWidgets(self, Data):
        #Создание Pie menu по json
        pass

    def show(self):
        return super().show()
    
if __name__ == "__main__":
    app = QApplication([])
    w = OverlayWindow()
    w.show()
    app.exec_()