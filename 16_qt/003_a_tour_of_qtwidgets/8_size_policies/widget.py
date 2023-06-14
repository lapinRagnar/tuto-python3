from PySide6.QtWidgets import QWidget

class Widget(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Size Policies')
    self.resize(400, 300)
    
    