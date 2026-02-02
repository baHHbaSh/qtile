from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from lib.Node import Node
from lib.Connection import Connection

class OverlayWindow(QWidget, Node):
    def __init__(self, NodeC:Node, Data:dict, WireC:Connection):
        super(QWidget, self).__init__()
        super(Node, self).__init__()
        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        x, y, w, h = NodeC.x, NodeC.y, NodeC.w, NodeC.h
        self.setGeometry(x - w / 2, y - h / 2, w, h)
        self.Wire = WireC
        self.InitWidgets(Data)
        
    def InitWidgets(self, Data:dict, Parent:Node):
        #Создание Pie menu по json
        pass

    def show(self):
        return super().show()
    
if __name__ == "__main__":
    app = QApplication([])
    w = OverlayWindow()
    w.show()
    app.exec_()