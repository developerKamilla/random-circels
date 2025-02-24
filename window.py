from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QColor, QPainter
from random import randint
from design import Ui_MainWindow

class Window(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paintEvent)
    
    def paintEvent(self, event=None) -> None:
        print('[Qt] paint event')
        qp: QPainter = QPainter(self)
        self.draw_circles(qp)
    
    def draw_circles(self, qp: QPainter) -> None:
        print('[Qt] drawing random circles')
        qp.setBrush(QColor(
            randint(0, 255),
            randint(0, 255),
            randint(0, 255)
        ))
        for i in range(randint(2, 14)):
            radius: int = randint(0, 200)
            qp.drawEllipse(
                randint(0, 600),
                randint(0, 450),
                radius,
                radius
            )
