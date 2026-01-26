#Создание и удаление окон через BufferManager
from PyQt5.QtWidgets import*

class Application(QApplication):
    def __init__(self):
        super().__init__([])
    def Launch(self):
        self.exec_()