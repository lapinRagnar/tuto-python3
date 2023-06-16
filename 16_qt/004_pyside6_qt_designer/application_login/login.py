import sys

from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.mon_login import Ui_w_LoginForm

class LoginForm(qtw.QWidget, Ui_w_LoginForm):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.retranslateUi(self)

if __name__ == "__main__":
  app = qtw.QApplication(sys.argv)
  window = LoginForm()
  window.show()
  
  app.exec()