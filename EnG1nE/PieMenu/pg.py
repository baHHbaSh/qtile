"""import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Canvas")
        self.resize(600, 400)
        self.points = []  # для примера: сохраняем точки при клике

    def mousePressEvent(self, event):
        self.points.append(event.pos())
        self.update()  # вызывает paintEvent

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Прозрачный фон (если окно тоже прозрачное — см. ниже)
        painter.fillRect(self.rect(), Qt.transparent)

        # Примеры рисования
        painter.setPen(QPen(Qt.blue, 3))
        painter.drawLine(50, 50, 200, 150)

        painter.setBrush(QColor(255, 0, 0, 128))  # полупрозрачный красный
        painter.drawEllipse(250, 100, 100, 100)

        # Рисуем сохранённые точки
        painter.setPen(QPen(Qt.green, 5))
        for point in self.points:
            painter.drawPoint(point)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    canvas = Canvas()
    canvas.show()
    sys.exit(app.exec_())"""

import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5.QtCore import Qt, QPoint, QRectF
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QFont


class CircularMenu(QWidget):
    """Круговое меню с секторами"""
    
    def __init__(self, items=None, radius=190, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.radius = radius
        self.center = QPoint(radius, radius)
        self.items = items or []
        self.selected_index = -1
        
        # Размер виджета = диаметр круга + отступы
        self.setFixedSize(radius * 2 + 20, radius * 2 + 20)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Фоновое кольцо
        painter.setBrush(QBrush(QColor(40, 40, 40, 220)))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.center, self.radius, self.radius)
        
        # Отрисовка секторов
        if not self.items:
            return
            
        angle_step = 360.0 / len(self.items)
        for i, item in enumerate(self.items):
            start_angle = i * angle_step
            span_angle = angle_step
            
            # Подсветка выбранного сектора
            if i == self.selected_index:
                painter.setBrush(QBrush(QColor(70, 130, 180, 200)))
            else:
                painter.setBrush(QBrush(QColor(60, 60, 60, 230)))
            
            # Рисуем сектор
            painter.setPen(QPen(QColor(100, 100, 100), 2))
            painter.drawPie(
                self.center.x() - self.radius, 
                self.center.y() - self.radius,
                self.radius * 2, 
                self.radius * 2,
                int(start_angle * 16), 
                int(span_angle * 16)
            )
            
            # Текст в секторе (ИСПРАВЛЕНО: используем QRectF для центрирования)
            mid_angle = math.radians(start_angle + span_angle / 2)
            text_radius = self.radius * 0.6  # Расстояние от центра до текста
            
            text_x = self.center.x() + text_radius * math.cos(mid_angle)
            text_y = self.center.y() + text_radius * math.sin(mid_angle)
            
            # Создаём небольшой прямоугольник вокруг точки для центрирования текста
            text_rect = QRectF(text_x - 40, text_y - 15, 80, 30)
            
            painter.setPen(Qt.white)
            painter.setFont(QFont("Arial", 11, QFont.Bold))
            painter.drawText(text_rect, Qt.AlignCenter, item['text'])
    
    def mouseMoveEvent(self, event):
        # Определяем, над каким сектором находится курсор
        dx = event.x() - self.center.x()
        dy = event.y() - self.center.y()
        distance = math.hypot(dx, dy)
        
        if distance <= self.radius and self.items:
            angle = math.degrees(math.atan2(dy, dx))
            if angle < 0:
                angle += 360
            
            angle_step = 360.0 / len(self.items)
            self.selected_index = int(angle / angle_step) % len(self.items)
        else:
            self.selected_index = -1
        
        self.update()
    
    def mousePressEvent(self, event):
        if self.selected_index >= 0 and self.selected_index < len(self.items):
            item = self.items[self.selected_index]
            if 'callback' in item and callable(item['callback']):
                item['callback'](item)
            self.close()
        else:
            self.close()
    
    def showAt(self, global_pos):
        """Показать меню с центром в указанной точке"""
        self.move(global_pos.x() - self.center.x(), 
                 global_pos.y() - self.center.y())
        self.show()
        self.raise_()
        self.activateWindow()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Круговое меню - PyQt5")
        self.setGeometry(100, 100, 600, 400)
        
        # Кнопка для вызова меню
        self.btn = QPushButton("Показать круговое меню", self)
        self.btn.setGeometry(200, 150, 200, 50)
        self.btn.clicked.connect(self.show_menu)
        
        # Статусная метка
        self.status_label = QLabel("Выбор: нет", self)
        self.status_label.setGeometry(200, 220, 200, 30)
        self.status_label.setAlignment(Qt.AlignCenter)
        
        # Настройка меню
        self.menu_items = [
            {'text': '📁 Открыть', 'callback': self.action_open},
            {'text': '💾 Сохранить', 'callback': self.action_save},
            {'text': '✏️ Редактировать', 'callback': self.action_edit},
            {'text': '🗑️ Удалить', 'callback': self.action_delete},
            {'text': '⚙️ Настройки', 'callback': self.action_settings},
            {'text': '❓ Помощь', 'callback': self.action_help},
        ]
        
        self.circular_menu = CircularMenu(self.menu_items, radius=130, parent=self)
    
    def show_menu(self):
        # Показать меню в центре кнопки
        pos = self.btn.mapToGlobal(self.btn.rect().center())
        self.circular_menu.showAt(pos)
    
    def action_open(self, item):
        self.status_label.setText(f"Выбрано: {item['text']}")
    
    def action_save(self, item):
        self.status_label.setText(f"Выбрано: {item['text']}")
    
    def action_edit(self, item):
        self.status_label.setText(f"Выбрано: {item['text']}")
    
    def action_delete(self, item):
        self.status_label.setText(f"Выбрано: {item['text']}")
    
    def action_settings(self, item):
        self.status_label.setText(f"Выбрано: {item['text']}")
    
    def action_help(self, item):
        self.status_label.setText(f"Выбрано: {item['text']}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())