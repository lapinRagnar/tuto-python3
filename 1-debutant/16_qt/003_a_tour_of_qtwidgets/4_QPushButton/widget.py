from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget

class Widget(QWidget):
  def __init__(self):
    super().__init__()
    
    self.setWindowTitle('QPushButton')
    
    button = QPushButton('click me')
    button.clicked.connect(self.button_clicked)
    button.pressed.connect(self.button_pressed)
    button.released.connect(self.button_released)
    
    layout = QVBoxLayout()
    layout.addWidget(button)
    
    self.setLayout(layout)

  def button_clicked(self):
    print('button clicked')
    
  def button_pressed(self):
    print('button pressed')
    
  def button_released(self):
    print('button released')
    
