from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow(app=app)
window.show()

app.exec()