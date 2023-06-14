from PySide6.QtWidgets import QApplication
import sys
from widget import Widget

app = QApplication(sys.argv)
w = Widget()
w.show()

app.exec()

