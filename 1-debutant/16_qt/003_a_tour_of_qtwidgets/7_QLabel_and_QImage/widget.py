from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget

class Widget(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle("QLabel et QImage")
    self.resize(300, 300)
    
    image_label = QLabel()
    image_label.setPixmap(QPixmap("images/mon-profile.jpg").scaled(150, 150))

    
    layout = QVBoxLayout()
    layout.addWidget(image_label)
    
    self.setLayout(layout)